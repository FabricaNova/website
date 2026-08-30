#!/usr/bin/env python3
"""
Erzeugt preview.html aus index.html + styles.css + assets/.

preview.html ist eine einzige, in sich geschlossene Datei: CSS, Bilder und
Schriften stecken eingebettet darin. Damit lässt sich der Entwurf per Doppelklick
oder als E-Mail-Anhang ansehen, ohne Ordnerstruktur und ohne Webserver.

WICHTIG: preview.html niemals direkt bearbeiten — Änderungen gehören in
index.html oder styles.css. Danach dieses Skript ausführen:

    python3 build-preview.py

Getestet mit Python 3.9+ (nur Standardbibliothek).
"""

from __future__ import annotations

import base64
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_HTML = ROOT / "index.html"
SOURCE_CSS = ROOT / "styles.css"
TARGET = ROOT / "preview.html"

MIME = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".svg": "image/svg+xml",
    ".webp": "image/webp",
    ".woff2": "font/woff2",
}

# Der erweiterte Latin-Bereich bleibt in der Vorschau außen vor: er würde die
# Datei um rund 50 KB vergrößern und wird für deutsche Texte nie gebraucht.
SKIP_IN_PREVIEW = ("latin-ext",)


def data_uri(path: Path) -> str:
    mime = MIME.get(path.suffix.lower())
    if mime is None:
        raise ValueError(f"Unbekannter Dateityp: {path.name}")
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def resolve(rel: str) -> Path:
    return (ROOT / rel.split("?")[0].split("#")[0]).resolve()


def inline_css(css: str, missing: list[str]) -> str:
    """url('assets/…') durch Data-URIs ersetzen; latin-ext-Blöcke entfernen."""

    # Ganze @font-face-Blöcke für übersprungene Subsets herausnehmen.
    def drop_block(match: re.Match) -> str:
        block = match.group(0)
        return "" if any(s in block for s in SKIP_IN_PREVIEW) else block

    css = re.sub(r"@font-face\s*\{[^}]*\}\s*", drop_block, css)

    def repl(match: re.Match) -> str:
        quote, rel = match.group(1), match.group(2)
        target = resolve(rel)
        if not target.is_file():
            missing.append(rel)
            return match.group(0)
        return f"url({quote}{data_uri(target)}{quote})"

    return re.sub(r"url\((['\"]?)((?:assets|\./assets)/[^'\")]+)\1\)", repl, css)


def main() -> int:
    for path in (SOURCE_HTML, SOURCE_CSS):
        if not path.is_file():
            print(f"FEHLER: {path.name} nicht gefunden.", file=sys.stderr)
            return 1

    html = SOURCE_HTML.read_text(encoding="utf-8")
    css = SOURCE_CSS.read_text(encoding="utf-8")
    missing: list[str] = []

    css = inline_css(css, missing)

    # Schrift-Preloads entfernen — die Schriften stecken jetzt im CSS.
    html = re.sub(r'[ \t]*<link rel="preload"[^>]*>\n?', "", html)

    # Stylesheet-Verweis durch den eingebetteten Stil ersetzen.
    style_block = "<style>\n" + css.strip() + "\n</style>"
    html, hits = re.subn(
        r'<link rel="stylesheet" href="styles\.css">', style_block, html, count=1
    )
    if hits != 1:
        print("FEHLER: <link rel=\"stylesheet\" href=\"styles.css\"> nicht gefunden.", file=sys.stderr)
        return 1

    # Bild- und Icon-Pfade einbetten (src="…" und href="…").
    def repl_attr(match: re.Match) -> str:
        attr, rel = match.group(1), match.group(2)
        target = resolve(rel)
        if not target.is_file():
            missing.append(rel)
            return match.group(0)
        return f'{attr}="{data_uri(target)}"'

    html = re.sub(r'\b(src|href)="(assets/[^"]+\.(?:png|jpe?g|svg|webp))"', repl_attr, html)

    # Stand-Stempel in die Fußzeile: nur in der Vorschau, damit man am Handy oder
    # im Postfach sofort sieht, ob eine alte Datei geöffnet ist.
    stamp = datetime.now().strftime("%d.%m.%Y, %H:%M")
    html = html.replace(
        "<span>\u00a9 2026 Fabrica Nova</span>",
        '<span>\u00a9 2026 Fabrica Nova</span>\n      '
        f'<span class="preview-stamp">Vorschau &middot; Stand {stamp}</span>',
        1,
    )

    banner = (
        "<!--\n"
        f"  AUTOMATISCH ERZEUGT am {stamp} — nicht direkt bearbeiten.\n"
        "  Quelle: index.html + styles.css + assets/\n"
        "  Neu erzeugen mit:  python3 build-preview.py\n"
        "  Diese Datei ist in sich geschlossen (CSS, Bilder, Schriften eingebettet)\n"
        "  und funktioniert per Doppelklick ohne Webserver.\n"
        "-->\n"
    )
    html = html.replace("<!DOCTYPE html>\n", "<!DOCTYPE html>\n" + banner, 1)

    TARGET.write_text(html, encoding="utf-8")

    size_kb = TARGET.stat().st_size / 1024
    print(f"preview.html geschrieben: {size_kb:.0f} KB")
    if "data:font/woff2" in html:
        print("  Schriften eingebettet: ja")
    else:
        print("  WARNUNG: keine eingebetteten Schriften gefunden.")
    remaining = re.findall(r'(?:src|href)="(assets/[^"]+)"', html)
    if remaining:
        # Downloads (z. B. das Check-PDF) bleiben absichtlich Pfade — eingebettet
        # wären sie nicht mehr als Datei speicherbar. Diese Links funktionieren,
        # solange preview.html im Projektordner liegt.
        print("  Bewusst als Pfad belassen (Downloads):", ", ".join(sorted(set(remaining))))
    if missing:
        print("  FEHLENDE DATEIEN:", ", ".join(sorted(set(missing))))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
