# Fabrica Nova — Website-Projekt: Entwicklungsdokumentation

Stand: 15. Juli 2026
Zweck dieses Dokuments: Vollständiger Kontext, damit die Website-Entwicklung in einer neuen Chat-Session (auch auf einem anderen Account) nahtlos fortgesetzt werden kann, ohne dass Informationen verloren gehen.

**⚠️ Strukturelle Änderung (15. Juli 2026):** Die Website wurde von einer Mehrseiten-Struktur (separate `team.html`/`cases.html`) auf eine **Single-Page-Struktur mit Scroll-Snapping** umgestellt. Details siehe Abschnitt 3 und 6a. Diese Änderung betrifft die Abschnitte weiter unten, die noch die alte Struktur beschreiben — dort wo relevant, ist der neue Stand ergänzt.

**Anleitung für den Neustart in einer neuen Session:**
Lade diese Datei zusammen mit dem kompletten Website-Ordner (zip) hoch und schreibe z. B.: *"Lies die PROJEKT-DOKUMENTATION.md und die Website-Dateien, wir setzen die Entwicklung fort."* Alles Nötige zur Entscheidung, Historie und zum aktuellen Stand steht unten.

---

## 1. Projektüberblick

- **Marke:** Fabrica Nova
- **Positionierung/Angebot:** "DIG HDW" = *"Digitales Handwerk"* — ein Sammelbegriff, **nicht** ausschließlich Digitalisierung. Umfasst zu gleichen Teilen: Prozessoptimierung, kaufmännische Beratung, und Digitalisierung dort, wo sie sinnvoll ist.
- **Zielgruppe:** Inhabergeführte Handwerksbetriebe, ca. 20–200 Mitarbeitende. Käufer: Geschäftsführer/Inhaber.
- **Rechtsform:** Firma befindet sich aktuell im Gründungsprozess beim Notar. Handelsregisterdaten, Firmenname (rechtlich), Vertretungsberechtigte, USt-ID, Geschäftsadresse, Telefon/E-Mail **liegen noch nicht vor**.
- **Ton/Markenpositionierung (wichtig, mehrfach vom Nutzer betont):**
  - Exklusiv, hochwertig, zurückhaltend — **kein** "Massentourismus"-Charakter
  - **Keine Preise, keine Preisandeutungen** irgendwo auf der Website
  - **Keine Verkaufs-Rhetorik**, keine klassischen CTAs ("Jetzt buchen", "Kostenloses Erstgespräch" o. ä.) — Kontakt wird nur ruhig/beiläufig als Information angeboten
  - Bewusst **wortarm/reduziert**, nicht textlastig
- **Sprachen:** Deutsch ist inhaltlich fertig. **Englische Version steht noch aus** (1:1-Strukturübersetzung, sobald deutscher Text final ist).

---

## 2. Bereitgestellte Ausgangsmaterialien (vom Nutzer hochgeladen)

| Datei | Inhalt | Verwendung |
|---|---|---|
| `Picture1.png` | Original-Logo mit grau-weißem Karo-Hintergrund (Transparenz-Anzeige fehlerhaft eingebettet) | Freigestellt → `assets/fabrica-nova-logo.png` (mit Schriftzug) und `assets/fabrica-nova-icon.png` (nur Symbol, für Hero-Grafik zugeschnitten) |
| `Business_Plan_20260514.docx` | Vollständiger Business Plan "DIG HDW — Angebotsschärfung Digitalisierung im Handwerk": Positionierung, Zielkunde, Leistungspakete (Digitalisierungs-Check / Fahrplan / Umsetzungsbegleitung), Preise, Business Model Canvas | Positionierungstexte und Themenfelder der Website basieren darauf. **Preise wurden bewusst NICHT übernommen** (explizite Vorgabe). Referenzcase "Schreinerei" stammt von hier (Glaubwürdigkeitsanker aus dem Business Plan). |
| `Team.pptx` | 3 Team-Mitglieder mit Rolle, Erfahrung, Referenzprojekten, privater Mobilnummer und E-Mail | Namen für Team-Seite übernommen. **Private Kontaktdaten (Mobil/E-Mail) bewusst NICHT auf der Website veröffentlicht** (Datenschutz-Entscheidung, vom Nutzer bestätigt) |

**Team-Mitglieder (Namen, für Team-Seite):**
1. Sebastian Ifland
2. Michael Axenbeck
3. Bastian Richter

*(Rollen/Erfahrungstexte aus dem PPTX liegen vor, wurden aber noch nicht auf der Seite verwendet — aktuell nur Name + Zitat-Platzhalter. Falls gewünscht, könnten Kurzrollen ergänzt werden — siehe Offene Punkte.)*

---

## 3. Aktuelle Dateistruktur

```
fabrica-nova-site/
├── index.html              EINZIGE Hauptseite: Hero → Themenfelder → Vorgehen → Team → Projekte
│                            als Scroll-Snap-Sektionen (siehe Abschnitt 6a). Keine separaten
│                            team.html/cases.html mehr — wurden entfernt und als Sektionen
│                            in index.html integriert.
├── impressum.html            Weiterhin separate Seite, rechtlich unvollständig
├── datenschutz.html          Weiterhin separate Seite, rechtlich unvollständig
├── styles.css                 Gemeinsames Stylesheet (Design-Tokens, Layout, Responsive, Slider-Logik-CSS, Snap-Mechanik)
├── preview.html               NUR für Chat-Vorschau: identischer Inhalt wie index.html, aber
│                              mit eingebettetem CSS + Logo (base64), damit es als einzelne
│                              Datei ohne Ordnerkontext im Chat-Vorschaufenster rendert.
│                              Nicht für Deployment gedacht — immer aus index.html neu generieren.
├── PROJEKT-DOKUMENTATION.md   Dieses Dokument
└── assets/
    ├── fabrica-nova-logo.png  Vollständiges Logo (Symbol + Schriftzug), transparent
    └── fabrica-nova-icon.png  Nur das Symbol, ohne Schriftzug (für Hero-Grafik)
```

**Navigation:** Header-Links sind jetzt Anker-Links (`#hero`, `#team`, `#cases`) statt Datei-Links. Von `impressum.html`/`datenschutz.html` aus zeigen die Nav-Links auf `index.html#team` etc. (Datei + Anker kombiniert), da diese beiden Seiten weiterhin eigenständig sind.

---

## 4. Design-System

### Farben (aus Original-Vorgabe des Nutzers, alle Hex-Werte)

| Variable | Hex | Verwendung |
|---|---|---|
| `--ink` | `#003A41` | Haupttext, Überschriften |
| `--deep` | `#2C3932` | Dunkelste Fläche (Footer) |
| `--paper` | `#FDF6EA` | Seitenhintergrund |
| `--sage` | `#ECEBE3` | Ruhige Sekundärfläche (Karten, Cases-Banner) |
| `--teal` | `#68989E` | Gedämpfter Akzent, Linien, Case-2-Kennung |
| `--gold` | `#BFB360` | Signatur-Akzent (genau 1× pro Ansicht besonders eingesetzt), Case-1-Kennung |
| `--wine` | `#BF6093` | Case-3-Kennung, Dev-Warnbanner |
| `--plum` | `#400023` | Bisher ungenutzt, für spätere Verwendung reserviert |

### Typografie

- **Ursprünglicher Wunsch des Nutzers:** Aptos (Headings) / Aptos Light (Body)
- **Problem:** Aptos ist eine proprietäre Microsoft-Schrift, nicht frei als Web-Font lizenzierbar
- **Lösung:** **Hanken Grotesk** (Google Fonts, freie Lizenz) — Light für Fließtext, Semibold/Bold für Headings. Bewusst dieselbe Zwei-Gewichte-Logik wie der ursprüngliche Wunsch, nur mit lizenzfreier Schrift. Eingebunden über Google Fonts CDN in `styles.css` (benötigt Internetverbindung beim Laden — offline/lokal ohne Netz fällt auf System-Sans-Serif zurück, sieht dann etwas anders aus, funktioniert aber).

### Signatur-Element ("Facet"-Motiv)

Aus dem Logo abgeleitet: die Wortmarke FN hat einen charakteristischen diagonalen Schnitt/abgeschrägte Ecke. Dieses Motiv wird als wiederkehrendes Gestaltungselement genutzt:
- Trennlinie zwischen Hero und Themenfelder (goldene Raute auf der Linie)
- Foto-Platzhalter auf der Team-Seite (abgeschnittene Ecke unten rechts)
- Große dekorative Fläche rechts im Hero (mit Icon darin)
- `.facet-card`-Klasse in CSS für weitere zukünftige Verwendung

---

## 5. Seiteninhalte (aktueller finaler Stand, Deutsch)

### Landing Page (`index.html`)

- **Kicker:** "Fabrica Nova"
- **H1:** "Exzellenz im Mittelstand."
- **Subline (2–3× größer als ursprünglich, wichtig für Konsistenz bei Änderungen):** "Beratung für kleine und mittlere Unternehmen & Handwerksbetriebe."
- **Hero-Grafik:** Facettierte Fläche rechts mit dem Icon-only-Logo mittig
- **Themenfelder (3 Kacheln, bewusst NICHT verändern laut Nutzer-Feedback):**
  1. Prozesse — "Struktur statt Zettelwirtschaft."
  2. Kaufmännische Steuerung — "Kalkulation und Ressourcen im Blick."
  3. Digitalisierung — "Wo sie wirklich etwas verbessert."
- **Vorgehen-Abschnitt** (mit animiertem, dezentem Facetten-Hintergrund, siehe Abschnitt 6):
  > Wir glauben an spürbare Effekte und arbeiten deshalb nach einem Prinzip: **Veränderung**.
  >
  > Diagnose, Zielbild und Umsetzung sind die drei grundlegenden Phasen aller unserer Projekte. Dabei gilt immer **Pragmatismus** und **Lösungsorientierung** für schnelle, messbare **Effekte**.

  Die fett/größer gesetzten Wörter (`<strong class="emph">`) sind: Veränderung, Pragmatismus, Lösungsorientierung, Effekte — exakte Nutzervorgabe.

### Team-Seite (`team.html`)

- 3 Karten: Foto + Name + Kurzprofil (erscheint als Overlay bei Hover/Fokus).
- **Fotos:** Michael Axenbeck und Sebastian Ifland seit 23. Juli eingebaut, Bastian Richter am 27. Juli ergänzt — **alle drei Team-Fotos sind jetzt vorhanden** (kein "Foto folgt"-Platzhalter mehr).
- **Bewusst keine erfundenen Zitate** — echte Personen, keine Wörter in den Mund legen
- **Bewusst keine privaten Kontaktdaten** (Mobilnummer/E-Mail aus dem PPTX) — Datenschutz-Entscheidung

**Foto-Aufbereitung (wichtig für zukünftige Team-Fotos):** Die Foto-Box zeigt per `object-fit: cover; object-position: 50% 8%` nur ein liegendes Kopf-Schulter-Band oben. Michael/Sebastian sind hohe Porträts (900×1350, Gesicht ≈ 15 % der Bildhöhe). Bastians Zulieferung war ein enger, quadratischer Headshot (400×400, Gesicht ≈ 50 % der Höhe) — unverändert eingesetzt wäre sein Gesicht ca. doppelt so groß erschienen. Deshalb wurde sein Foto in eine 900×1350-Leinwand mit hell angeglichenem Hintergrund (an Michaels helles Grau) gesetzt und weich eingeblendet, sodass das Gesicht in gleicher Größe wie bei den anderen erscheint und nicht angeschnitten wird. **Merke:** Neue Team-Fotos entweder als hohes Porträt (2:3) mit viel Kopf-/Schulterraum liefern, oder analog aufbereiten (`assets/team/team-bastian-richter.jpg` ist das Referenzbeispiel).

### Projekte-Seite (`cases.html`)

- Überschrift: "Ausgewählte Projekte." (bewusst ohne Zusatz "anonymisiert" — wurde entfernt)
- **Slider** mit genau einem Case sichtbar, automatischem Wechsel alle 5 Sekunden, Pfeil-Navigation, Punkt-Navigation
- **Case 1 (echt, aus Business Plan, Gold-Akzent):** Schreinerei, 45 Mitarbeitende — Herausforderung: manuelle Zeiterfassung/verspätete Rechnungsstellung — Ansatz: Prozessaufnahme, Software-Shortlist, begleitete Einführung — Ergebnis: Platzhalter (konkrete Kennzahl fehlt noch)
- **Case 2 (echt, Teal-Akzent, ergänzt 27. Juli 2026):** Familiengeführte Schreinerei (~50 Mitarbeiter, >5 Mio. € Umsatz) — Controlling-/Digitalisierungs-Case: Analyse der Auftrags-/Rechnungsdaten deckte nicht abgerechnete Aufträge auf (verlorene Zettel), gesamter Ablauf digitalisiert (eine Software für Materialwirtschaft, Auftragsplanung, Aufmaß, Dokumentation, Kundenunterschrift), Ergebnis: bis zu 5 % Umsatz. Platzhalter-Badge entfernt. Layout wie Case 1 (2-spaltige Details) — dafür wurde die frühere accent-2-Sonderregel (`.case-details` 1-spaltig, `max-width: 62ch`) auf 2 Spalten umgestellt, damit der längere Text ohne Scrollen passt.
- **Case 3 (echt, Wein-Akzent, ergänzt 27. Juli 2026):** Familiengeführtes Handwerksunternehmen (~30 Mitarbeiter, >6 Mio. € Umsatz) — Buy-and-Build/Übernahme-Case: Wachstumsstrategie mit Übernahme eines geschäftsfeldnahen Betriebs, Synergien auf Marge und Portfolio, „dreifacher Ergebniseffekt". Platzhalter-Badge entfernt. **Wichtig:** Die frühere accent-3-Sonder-Umsortierung der Detailblöcke (`order`-Regeln, war nur für die 2-Block-Platzhalter gedacht) wurde entfernt, sonst wäre bei vier Blöcken die Lesereihenfolge durcheinandergeraten — accent-3 zeigt jetzt natürliche Reihenfolge, 2-spaltig wie Case 1/2.
- Da Case 3 der textreichste ist (langer Ansatz-Block), wurden `.case-details` global leicht gestrafft (`line-height` 1.55→1.45, Zeilen-`gap` 1.25rem→1rem), damit alle Cases ohne Scrollen in einen Screen passen (konservativ ab ~767px Fensterhöhe; real etwas darunter).
- Grauer Banner läuft mit weichem Farbverlauf links/rechts in die Seiten-Hintergrundfarbe aus

### Impressum / Datenschutz (`impressum.html`, `datenschutz.html`)

- Beide klar als **unvollständig** markiert (roter/wein-farbener Hinweisbalken oben auf jeder Seite: "Entwurf — Platzhalterinhalte, nicht zur Veröffentlichung")
- Impressum: wartet auf Handelsregisterdaten vom Notar
- Datenschutz: Basiert auf dem Stand "keine Tracking-Tools, kein Kontaktformular" — muss bei Go-Live nochmal geprüft werden, falls sich das ändert

---

## 6. Technische Umsetzung

**Stack:** Reines statisches HTML/CSS/JavaScript (Vanilla, keine Frameworks, kein Build-Prozess, kein Backend). Bewusste Entscheidung wegen "so lean wie möglich" (Nutzer-Vorgabe ganz am Anfang des Projekts).

### Cases-Slider — Funktionsweise

- 3 echte Slides + 1 Klon des ersten Slides am Ende (für nahtlosen Vorwärts-Loop)
- **Wichtiger Design-Grundsatz (aus einem behobenen Bug gelernt, siehe unten):** Der unveränderte HTML-Zustand (bevor JavaScript läuft) muss bereits den korrekten ersten echten Case zeigen. Niemals einen Platzhalter-Klon an den Anfang des Tracks stellen.
- Vorwärts-Navigation: nahtlos animiert (Klon-Trick)
- Rückwärts-Navigation: normal animiert, außer beim Sprung vom ersten zum letzten Case — dort ein bewusster, nicht-animierter Sprung (kein zweiter Klon nötig, robuster)
- Pausiert automatisch bei Hover/Maus über den Slider
- Respektiert `prefers-reduced-motion`: kein Autoplay, aber manuelle Navigation (Punkte/Pfeile) funktioniert weiterhin
- Auf Mobile (≤720px) wandern die Pfeile von den Seitenrändern in eine Reihe unter den Slider (neben die Punkte), um Überlappung mit dem Textinhalt zu vermeiden
- **Wisch-Navigation (ergänzt 27. Juli 2026):** Zusätzlich zu Pfeilen/Punkten kann per Wischen geblättert werden. (a) **Touch/Mobil:** horizontaler Swipe links→nächster, rechts→vorheriger Case (Schwelle 40px). Die Geste erkennt beim ersten Move, ob sie horizontal oder vertikal ist; nur bei horizontaler wird `preventDefault` gesetzt, damit der vertikale Seiten-Scroll (Snap) unbeeinträchtigt bleibt. (b) **Trackpad/PC:** horizontales Zwei-Finger-Wischen (`wheel` mit dominantem `deltaX`) blättert; ein Schwellenwert (±50 akkumuliert) plus Cooldown (600ms) verhindert Mehrfachauslösung durch Momentum, und `preventDefault` unterdrückt zugleich die Browser-Zurück/Vor-Geste. Rein vertikale Gesten werden ignoriert (kein Konflikt mit Footer-Schranke, die auf `deltaY` reagiert). Beide Handler sind auf das `.case-slider`-Element begrenzt und nutzen die bestehende `next()`/`prev()`-Logik. Per Node-Simulation getestet.

### Vorgehen-Abschnitt — Hintergrund-Animation

- 2 dezente, facettierte Formen (Teal + Gold, sehr niedrige Opazität) driften in einer CSS-Keyframe-Schleife (6s / 4.5s, nach mehrfacher Beschleunigung auf Nutzerwunsch)
- Reine CSS-Animation, kein JavaScript nötig
- Automatisch deaktiviert bei `prefers-reduced-motion: reduce`

### Responsive / Mobile

- Breakpoints: 900px (Hero-Grafik wird ausgeblendet), 800px (Themenfelder/Team einspaltig), 720px (Cases einspaltig, Slider-Pfeile in Reihe), 640px (Header/Logo verkleinert)

### Bekannte, bereits behobene Bugs (wichtig für zukünftige Änderungen — nicht wiederholen)

1. **CSS-Selektor-Bug:** `.case-card .accent-1` (Nachfahren-Selektor) statt `.case-card.accent-1` (zusammengesetzter Selektor) — Akzentfarben wurden nicht angezeigt. Fix: immer auf zusammengesetzte Selektoren achten, wenn zwei Klassen am selben Element sitzen.
2. **Flexbox-Sizing-Bug (mobil):** Als `.case-slider` auf Mobile zu `display:flex` wurde, fehlte `min-width:0` auf `.case-track`. Dadurch hat sich der Track auf die ungebremste Inhaltsbreite (>900px) aufgebläht, obwohl der Bildschirm nur 375px breit war — Text wurde abgeschnitten/verschoben dargestellt. **Merke:** Bei verschachtelten Flex-Containern immer `min-width: 0` auf die Zwischenebenen setzen.
3. **Slider-Default-Zustand-Bug:** Ursprünglich stand ein Platzhalter-Klon am Anfang des Tracks (für einen nahtlosen beidseitigen Loop). Lief JavaScript aus irgendeinem Grund nicht (z. B. Sicherheitseinstellungen bei lokal geöffneten Dateien), zeigte die Seite einen Platzhalter statt des echten ersten Case. Fix: Klon nur noch am Ende, echter erster Case steht direkt im unveränderten HTML.
4. **Kein Bug, sondern Nutzer-Missverständnis:** `preview.html` (Chat-Vorschau, alle Seiten in einer Datei) wurde mit der echten Mehrseiten-Struktur verwechselt. Landing Page zeigt in der echten Struktur korrekt KEINE Cases/Team-Inhalte — die liegen auf eigenen Unterseiten, erreichbar über die Header-Navigation.

---

## 6a. Single-Page-Struktur mit Scroll-Snap (Umstellung 15. Juli 2026)

Auf Nutzerwunsch umgebaut: statt separater Seiten sind Team und Projekte jetzt Sektionen auf `index.html`. Beim Scrollen "rastet" die Seite abschnittsweise ein (CSS `scroll-snap`), jede Sektion füllt exakt eine Bildschirmhöhe.

### Struktur
5 Sektionen mit Klasse `.snap-section`, jede `id="..."` für Anker-Navigation: `#hero`, `#themenfelder`, `#vorgehen`, `#team`, `#cases`. Footer danach ist NICHT snap-gebunden (freies Ende der Seite).

### Wie es technisch funktioniert
- `html.snap-page { scroll-snap-type: y mandatory; }` — **wichtig:** muss auf `<html>` sitzen, NICHT auf `<body>` (siehe Bug-Log unten). Klasse nur auf `index.html`, damit Impressum/Datenschutz normal frei scrollen.
- `.snap-section { min-height: 100vh; scroll-snap-align: start; scroll-snap-stop: always; display:flex; align-items:center; padding-top: var(--header-h); }` — flex-zentriert den Inhalt vertikal, damit unterschiedlich hoher Content (Hero vs. Team-Grid) trotzdem mittig sitzt.
- Respektiert `prefers-reduced-motion` (Snap wird deaktiviert, normales Scrollen bleibt möglich).

### Fixierter Header + Dev-Notice-Banner
Da der Header bei Scroll-Snap sonst beim Springen zwischen Sektionen "verschwinden" würde, ist er jetzt `position: fixed`. Der Dev-Notice-Banner ("Entwurf...") sitzt ebenfalls fixiert, direkt darüber gestapelt. Beide zusammen ergeben `--header-h` (CSS-Variable, `calc(--notice-h + --bar-h)`), die als `padding-top` in jede Sektion einfließt, damit der Inhalt nicht unter der fixierten Leiste verschwindet.
**Wichtig:** `--notice-h` und `--bar-h` sind einzeln in `:root` definiert; bei Anpassungen (z. B. Logo-Größe im Header) IMMER diese Basiswerte ändern, nie `--header-h` direkt überschreiben (das ist ein berechneter Wert).

### Layout-Anpassungen für "immer genau ein Screen"
- Logo im Header wurde von 108px auf 40px verkleinert (Header ist jetzt dauerhaft sichtbares Overlay über allen Sektionen, nicht mehr nur einmalig oben auf einer frei scrollbaren Seite — bei 108px wäre zu viel permanenter Platzverbrauch entstanden). **Nutzer wurde das vorab als Trade-off angekündigt.**
- Team-Foto-Höhe: von `aspect-ratio: 4/5` (bezogen auf Kartenbreite) auf `height: clamp(120px, 26vh, 260px)` (bezogen auf Bildschirmhöhe) umgestellt — sonst wird die Sektion auf schmalen/hohen Layouts zu groß.
- **Mobile Team-Sektion (≤800px):** 3 gestapelte Karten passen NICHT in einen Screen (getestet: 1189px Inhalt bei 844px Viewport). Lösung: Auf Mobile wird `.team-grid` zu einer horizontal swipebaren Reihe (`overflow-x:auto; scroll-snap-type:x mandatory;`, jede Karte `flex:0 0 82%` mit Peek-Effekt zur nächsten Karte) — pro Screen ist dann nur eine Person sichtbar, swipebar zur nächsten. Kein JS nötig, reines CSS.
- Cases-Card-Padding und Vorgehen-Textabstände wurden leicht gestrafft (siehe `styles.css`), damit der Inhalt bei Viewport-Höhen ab ca. 700px zuverlässig ohne Überlauf passt.
- Facet-Divider (Trennlinie zwischen Hero und Themenfelder) ist jetzt ein `::before`/`::after`-Pseudo-Element auf der Themenfelder-Sektion selbst statt ein eigenes Flow-Element (passt so besser in die Snap-Logik).

### Bekannte, bereits geprüfte Nicht-Probleme
- Bei Playwright-Tests zeigte die `#vorgehen`-Sektion rechnerisch ein "Overflow" von genau 50px unabhängig von der Viewport-Höhe. Ursache: Die dekorativen Facetten-Formen im Hintergrund (`.approach-bg`) ragen absichtlich leicht über die Section-Box hinaus und werden per `overflow: hidden` unsichtbar abgeschnitten — `scrollHeight` zählt das trotzdem mit, obwohl visuell nichts überläuft. **Kein echter Bug, durch Screenshot bestätigt.**
- Automatisierte Mausrad-Scroll-Simulation (Playwright `mouse.wheel`) verhält sich in Headless-Chromium nicht wie eine echte Trackpad-/Mausrad-Geste. Zum Testen von Scroll-Snap-Verhalten zuverlässiger: `window.scrollTo({top, behavior:'instant'})` und dann prüfen, ob `window.scrollY` exakt auf einem Sektionsvielfachen landet.

### Bug-Log dieser Umstellung (nicht wiederholen)
1. **`scroll-snap-type` auf `body` statt `html`:** Hat gar nicht funktioniert (Scrollen lief normal weiter, kein Einrasten). Grund: Der Browser scrollt technisch das `<html>`-Element (`document.scrollingElement`), nicht `<body>`, sofern kein Quirks-Mode/spezielles Overflow-Setup vorliegt. **Merke:** `scroll-snap-type` für Viewport-Scrolling immer auf `html` setzen.
2. **Dev-Notice-Banner im normalen Fluss über fixiertem Header:** Erzeugte einen 38px-Versatz zwischen tatsächlichem Sektionsanfang und erwartetem `document-y = 0`, wodurch beim Testen zunächst fälschlich ein Layout-Fehler vermutet wurde (siehe unten). Fix: Notice-Banner ebenfalls `position: fixed`, mit dem Header zusammen eine feste Gesamthöhe (`--header-h`) bilden.
3. **Scheinbarer visueller Fehler beim ersten Testdurchlauf** (Themenfelder-Sektion wirkte auf Screenshots leer oben und abgeschnitten unten): Fehlalarm durch `scroll-behavior: smooth` — der Screenshot wurde mitten in der Scroll-Animation aufgenommen, nicht nach deren Ende. Für Tests/Debugging: entweder `behavior:'instant'` beim programmatischen Scrollen verwenden, oder deutlich länger warten (>1s) nach einem Sprung.

### Footer als eigener Snap-Punkt
Der Footer war zunächst NICHT Teil der Snap-Sektionen (nur natürliche Höhe, kein `min-height:100vh`). Problem: Da der Footer kürzer als ein Bildschirm ist, konnte der Browser ihn nie bündig einrasten lassen — beim Scrollen über die letzte Sektion hinaus blieb immer ein Rest der vorherigen Sektion sichtbar, und der Footer "flackerte" beim Scrollen rein/raus statt stabil zu bleiben. **Fix:** Footer bekam ebenfalls die `.snap-section`-Klasse (volle Bildschirmhöhe, Inhalt vertikal zentriert, dunkler Hintergrund füllt den ganzen Screen). Jetzt: Scrollen von Projekte nach unten zeigt ausschließlich den vollflächigen Footer, bleibt dort stabil, und Scrollen nach oben zeigt wieder ausschließlich Projekte — beides exakt, kein Übergangs-Zwischenzustand.

### Footer als Bottom-Sheet-Overlay (Anpassung 15. Juli 2026, zweite Iteration)
Erste Version (voller Screen, siehe oben) wurde auf Nutzerwunsch nochmal geändert: Der Footer ist jetzt kein eigener Snap-Screen mehr, sondern ein **fixiertes Bottom-Sheet**, das nur ca. ein Drittel der Bildschirmhöhe einnimmt und sich über den unteren Teil der Projekte-Sektion schiebt, statt sie zu ersetzen.

**Funktionsweise:** `#site-footer` ist `position: fixed; bottom:0;` mit `height: clamp(260px, 34vh, 400px)`, standardmäßig per `transform: translateY(100%)` unterhalb des sichtbaren Bereichs geparkt. Da der Footer dadurch nicht mehr Teil des normalen Dokumentflusses ist, endet die Seite jetzt wieder exakt bei 5×100vh (Cases ist die letzte Sektion).

Ein kleines JavaScript (`wheel`/`touchmove`/`keydown`-Listener) erkennt, wenn der Nutzer **bereits am Ende der Seite ist** (`window.scrollY` am Maximum, sprich: Cases-Sektion aktiv) **und weiter nach unten scrollt** — dann bekommt der Footer die Klasse `.is-open`, was ihn per CSS-Transition nach oben einschiebt (`translateY(0)`). Scrollt der Nutzer wieder nach oben (oder verlässt die Cases-Sektion auf anderem Weg), wird `.is-open` entfernt, der Footer schiebt sich zurück raus.

**Wichtig für zukünftige Anpassungen:**
- Footer-Höhe ändern: `.site-footer { height: ... }` in `styles.css`, nicht die JS-Logik anfassen.
- Die JS-Logik nutzt einen einfachen Schwellenwert-Vergleich (`atLastSection()`), keine Section-IDs außer `#cases` — falls weitere Sektionen nach Cases ergänzt werden, muss diese Funktion angepasst werden.
- Mobile: Footer-Inhalt (Grid + Copyright-Zeile) wurde separat verdichtet (`@media max-width:640px`), da die Sheet-Höhe auf kleinen Screens knapper ist als die ursprüngliche volle Footer-Höhe vorsah.

### Footer-Feinschliff (dritte Iteration)
Zwei weitere Bugs nach der Bottom-Sheet-Umstellung gefunden und behoben:
1. **Inhaltsbreite wich von den anderen Sektionen ab.** Ursache: `.site-footer` ist `display:flex` (für vertikale Zentrierung) — dadurch verhält sich das innere `.wrap` als Flex-Kind, dessen `max-width` + `margin:auto`-Zentrierung ohne explizite `width:100%` nicht mehr greift (Flex-Kinder schrumpfen sich standardmäßig auf ihren Inhalt, statt die Zeile zu füllen). Fix: `.site-footer .wrap { width: 100%; }` ergänzt.
2. **Hochscrollen sprang direkt zu Team statt nur den Footer zu schließen.** Ursache: Der `wheel`-Event zum Schließen des Footers und die native Scroll-Snap-Navigation zur vorherigen Sektion liefen gleichzeitig auf denselben Scroll-Impuls. Fix: Die Event-Listener (`wheel`, `touchmove`, `keydown`) sind jetzt nicht mehr `passive`, und rufen gezielt `e.preventDefault()` auf, wenn sie den Footer öffnen oder schließen — dadurch wird genau dieser eine Scroll-Impuls "verbraucht" und wirkt sich nicht zusätzlich auf die native Sektionsnavigation aus. Erst ein zweiter, separater Scroll-Impuls (nachdem der Footer bereits zu ist) navigiert regulär zu Team.

### Footer-Feinschliff (vierte Iteration) — Momentum/Fling-Problem
Nutzer beobachtete: (a) schnelles Runterscrollen von Team landete manchmal direkt bei Projekte UND öffnete sofort den Footer; (b) Hochscrollen vom offenen Footer aus landete trotzdem bei Team statt nur bei Projekte zu stoppen.

**Ursache:** Eine einzelne physische Scroll-Geste (Trackpad-Schwung, Mausrad-Kick) erzeugt intern viele einzelne `wheel`-Events nacheinander (Momentum/Inertia), nicht nur eines. Das Skript reagierte auf jedes davon einzeln, wodurch mehrere Effekte innerhalb einer einzigen, vom Nutzer als "eine Aktion" wahrgenommenen Geste ausgelöst wurden.

**Fix — zwei-teiliger Cooldown-Mechanismus (`blockUntil`-Timestamp, 600ms):**
1. **Beim Ankommen an der letzten Sektion** (per `scroll`-Event erkannt: Übergang von "nicht letzte Sektion" zu "letzte Sektion"): sofort 600ms Cooldown starten. Verhindert, dass die Restbewegung derselben Abwärts-Geste, die den Sektionswechsel Team→Projekte ausgelöst hat, unmittelbar auch noch den Footer öffnet.
2. **Beim Schließen des Footers:** ebenfalls 600ms Cooldown starten. Verhindert, dass die Restbewegung derselben Aufwärts-Geste, die den Footer geschlossen hat, unmittelbar auch noch zu Team weiterschickt.
   **Wichtig:** Das Öffnen selbst braucht KEINEN Cooldown (der bestehende `!open`-Guard reicht, da fortgesetztes Runterscrollen bei bereits offenem Footer ohnehin nichts weiter auslöst). Ein Cooldown beim Öffnen hätte ein unmittelbar folgendes, bewusstes Schließen fälschlich mitblockiert — das wurde in einem ersten Fixversuch getestet und korrigiert.
3. Während eines aktiven Cooldowns (`isBlocked()`) werden alle `wheel`/`touchmove`-Events per `preventDefault()` komplett geschluckt, damit auch das Consumieren des Scroll-Ziels zuverlässig ist, nicht nur der interne State.

**Getestet mit synthetisch erzeugten `WheelEvent`s** (`window.dispatchEvent(new WheelEvent(...))`), da Playwrights `mouse.wheel()`-Simulation in dieser Umgebung generell keine zuverlässigen Scroll-Bewegungen erzeugt (bereits an früherer Stelle in diesem Dokument vermerkt).

### Footer-Schranke (fünfte Iteration, 27. Juli 2026) — Momentum öffnete den Footer beim Ankommen
Problem: Beim Scrollen von Team auf Projekte öffnete sich in ~90 % der Fälle sofort der Footer, weil die Restbewegung (Momentum) derselben Geste, die auf Projekte gesprungen ist, direkt weiter nach unten „drückte". Der bisherige 600ms-Cooldown reichte nicht — Momentum dauert oft länger.

**Neue Logik (ersetzt den zeitbasierten Cooldown):** Der Footer öffnet jetzt nur noch bei einer **neuen, bewussten Abwärts-Geste**, erkannt an zwei Bedingungen:
1. **Gesten-Lücke (`GESTURE_GAP_MS` = 300ms):** Ein `wheel`/`touchmove`-Event zählt nur dann als Beginn einer neuen Geste, wenn davor ≥300ms Ruhe war. Momentum-Events folgen dichter (~16–50ms) und gelten damit als dieselbe Geste — sie können den Footer nie öffnen.
2. **Verweildauer (`DWELL_MS` = 700ms):** Zusätzlich muss man mindestens 700ms auf der Projekte-Sektion gewesen sein, bevor der Footer überhaupt öffnen darf. Damit ist garantiert, dass die Projekte-Seite immer zuerst allein sichtbar ist.

Schließen unverändert per Hochscrollen; die Restbewegung der Schließ-Geste wird über dasselbe Gesten-Lücken-Prinzip „aufgebraucht" (`consumeUpUntilGap`), sodass ein Hochscrollen erst den Footer schließt und erst eine zweite Geste zu Team navigiert. **Getestet** mit einer Node-Zustandssimulation (Momentum-Burst vs. bewusste Zweitgeste, alle Szenarien bestanden), da echtes Scroll-Verhalten headless nicht zuverlässig simulierbar ist. Stellschrauben bei Bedarf: `GESTURE_GAP_MS` und `DWELL_MS` im zweiten `<script>`-Block.

### Projektbeschreibung ohne internen Scroll (27. Juli 2026)
`.case-details` hatte `max-height: min(34vh, 260px); overflow-y: auto;` — der längste Case (Case 1, vier Detailblöcke) überschritt die 260px minimal und bekam eine interne Scrollleiste. Auf Nutzerwunsch entfernt: Die Box wächst jetzt auf ihre Texthöhe (kein innerer Scroll). Zum Ausgleich wurden Vertikalabstände leicht gestrafft (`.case-card` padding/gap, `.case-dots` margin-top), damit Case 1 auf üblichen Laptop-/Desktop-Höhen (ab ~730px Viewport-Höhe) in einen Screen passt. **Mobile-Fallback:** Im `@media (max-width: 720px)`-Block bleibt ein begrenzter Scroll (`max-height: 44vh; overflow-y:auto`), weil ein langer Case auf einem Telefon sonst nicht ohne zu kleine Schrift auf einen Screen passt. Änderung in `styles.css` und im Inline-`<style>` von `preview.html` synchron.

### Themenfelder — Flip-Karten & Hover-Text (27. Juli 2026)
Die Themenfelder-Sektion besteht aus drei `.field-card`-Flip-Karten (Vorderseite: Icon + Titel; Rückseite `.flip-back`: `<h4>` + zwei `<li>`-Bullets, erscheint bei Hover/Fokus/Tap). Aktuelle Titel/Rückseiten:
1. **Prozesse & Digitalisierung** → „Struktur statt Zettelwirtschaft"
2. **Unternehmensführung** → „Ressourcen im Blick"
3. **Nachfolgeregelung & Übernahmen** → „Gestärkt in die Zukunft" (Rückseite am 27. Juli mit echtem Text gefüllt, vorher `tbd`-Platzhalter).

**Kartenhöhe / kein Scrollen:** Der längste Bullet in Kachel 3 ist deutlich länger als die der anderen. Da die Flip-Karten eine feste Höhe brauchen (die absolut positionierten Vorder-/Rückseiten füllen die Kartenhöhe), wurde `.field-card height` von `clamp(210px, 32vh, 300px)` auf `clamp(300px, 38vh, 350px)` erhöht und die `.flip-back`-Innenabstände leicht reduziert (`1.5rem`→`1.25rem`), sodass der komplette Text ohne interne Scrollleiste sichtbar ist. Über eine Zeilenumbruch-Messung geprüft: passt auf allen üblichen Desktop-Auflösungen (inkl. breit-flacher Fenster wie 1920×720). `overflow-y:auto` bleibt als Sicherheitsnetz. **Merke:** Neue/längere Bullet-Texte in den Kacheln immer gegen diese feste Höhe prüfen; ggf. Höhe erneut anpassen statt Text scrollen zu lassen.

## 7. Deployment-Plan (noch nicht ausgeführt)

- **Domain:** registriert bei **Strato**
- **Aktuelles Hosting:** **Squarespace** (nicht Strato-Webhosting, wurde in dieser Session korrigiert) — geschlossenes CMS, kein Datei-Upload für komplett eigenen Code möglich
- **E-Mail:** läuft über **Microsoft 365**, verknüpft mit der Domain
- **Geplanter Weg (Option B, mit Nutzer abgestimmt):**
  1. Neue Seite bei einem kostenlosen statischen Hoster deployen (Vercel, Netlify oder Cloudflare Pages)
  2. Bei Strato die DNS-Einträge (A-/CNAME-Records) auf den neuen Hoster umstellen
  3. **Kritisch:** MX-Records (und SPF/DKIM-TXT-Records) für Microsoft 365 dabei **unverändert lassen** — sonst funktioniert die E-Mail nicht mehr
  4. Squarespace-Abo erst kündigen, wenn die neue Seite live und geprüft ist
- **Blocker vor Go-Live:** Impressum und Datenschutzerklärung müssen mit echten Daten vervollständigt sein (rechtliche Pflicht, Notarprozess muss abgeschlossen sein)

---

## 8. Offene Aufgaben / TODOs

- [x] Team-Fotos einfügen — **erledigt** (Michael, Sebastian: 23. Juli; Bastian: 27. Juli)
- [ ] Echte Zitate der 3 Team-Mitglieder einholen und einfügen
- [ ] Case 2 und Case 3 mit echten (anonymisierten) Projektinhalten füllen
- [ ] Case 1: konkrete Ergebnis-Kennzahl ergänzen (aktuell Platzhalter)
- [ ] Impressum: Firmenname, Rechtsform, Adresse, Handelsregisternummer, Vertretungsberechtigte, USt-ID (nach Notar-Abschluss)
- [ ] Datenschutzerklärung: Verantwortliche Stelle eintragen, ggf. anpassen falls doch Tools/Tracking eingesetzt werden
- [ ] Kontaktdaten (Telefon, E-Mail) im Footer ergänzen (aktuell "[folgt]"-Platzhalter)
- [ ] Englische Sprachversion (1:1-Struktur, sobald deutscher Text final)
- [ ] Deployment durchführen (siehe Abschnitt 7)
- [ ] Optional/besprochen, aber noch nicht spezifiziert: Hover-Tooltips ("Sprechblasen") an ausgewählten Stellen — Nutzer wollte später darauf zurückkommen, konkrete Stelle noch nicht festgelegt

---

## 9. Entscheidungs-Log (chronologische Kurzfassung aller Feedback-Runden)

1. Erstbriefing: Lean, gesetzliche Mindestanforderungen, keine Backend, 3 Seiten (Landing/Cases/Team), Referenz Stern Stewart & Co. (nur Struktur/Stil-Inspiration, keine Markenübernahme)
2. Rechtliche Angaben: alle in Bearbeitung (Notar) — Platzhalter-Strategie festgelegt
3. Content-Vorgaben: Cases anonymisiert (3 Stück, davon 1 mit echtem Hintergrund aus Business Plan), Team mit Zitat statt Biografie, DE+EN, nur Mailto/Telefon als Kontakt (kein Formular)
4. Design-Assets erhalten: Logo (musste freigestellt werden — Karo-Hintergrund war eingebrannt, keine echte Transparenz), Farbpalette (8 Hex-Werte), Aptos-Wunsch (durch Hanken Grotesk ersetzt, Lizenzgrund)
5. Erste Korrektur: DIG HDW umfasst nicht nur Digitalisierung, sondern auch Management-/Prozessthemen — Positionierung entsprechend breiter gefasst
6. Ton-Korrektur: keine Preise, keine Verkaufs-Rhetorik, Exklusivität statt Massenware, CTA "Kostenloses Erstgespräch" abgeschwächt bis entfernt
7. Struktur-Korrektur: Landing Page wortarm/reduziert, "Vorgehen"-Abschnitt auf einen Satz eingedampft
8. Deployment-Recherche: zunächst Strato-Baukasten angenommen, dann korrigiert zu Squarespace — beide erlauben keinen eigenen Datei-Upload, Empfehlung auf externen statischen Hoster + DNS-Umstellung bei Strato, MX-Records für Microsoft 365 beachten
9. Design-Feedback-Runde 1: Logo 3× größer, neue Hero-Headline/Subline, Trennlinien-Bug behoben, Ausrichtungs-Bug bei "Vorgehen" behoben, neuer Vorgehen-Text mit Hervorhebungen, Hintergrund-Animation eingebaut
10. Design-Feedback-Runde 2: Animation schneller, Cases als Slider umgebaut
11. Design-Feedback-Runde 3: Animation nochmal schneller, weicher Farbverlauf am Cases-Banner, Pfeil-Navigation ergänzt, Frage zu Hover-Tooltips beantwortet (grundsätzlich möglich, noch nicht spezifiziert)
12. Design-Feedback-Runde 4: Cases-Überschrift gekürzt, Hero-Grafik mit Icon-only-Logo gefüllt, Mobile-Optimierung nachgezogen (mehrere echte Bugs gefunden und behoben, siehe Abschnitt 6)
13. Fehlermeldung "Cases fehlen" — zunächst als Slider-Default-Bug fehlinterpretiert und entsprechend gehärtet (siehe Bug 3 in Abschnitt 6); tatsächliche Ursache war ein Missverständnis der Seitenstruktur (siehe Bug 4) — beides bleibt behoben/dokumentiert, da beides echte Verbesserungen waren
14. Strukturumstellung auf Single-Page mit Scroll-Snap: Team und Projekte wurden von eigenständigen Seiten zu Sektionen auf `index.html` umgebaut (Vorbild war die bisherige `preview.html`-Logik). Impressum/Datenschutz bleiben separate Seiten. Scroll-Verhalten: abschnittsweises Einrasten statt freiem Scrollen, jede Sektion exakt eine Bildschirmhöhe. Mehrere nicht-triviale technische Probleme dabei gelöst (siehe Abschnitt 6a) — u. a. `scroll-snap-type` gehört auf `<html>`, nicht `<body>`; fixierter Header + Dev-Notice mussten zu einer gemeinsamen Höhe zusammengefasst werden; Team-Sektion brauchte auf Mobile eine horizontale Swipe-Lösung statt vertikalem Stapeln, um in einen Screen zu passen
15. (27. Juli 2026) Team-Foto Bastian Richter eingefügt (dritte Karte, vorher "Foto folgt"). Quadratischer Headshot wurde auf Porträt-Format mit gematchtem hellen Hintergrund aufbereitet, damit die Gesichtsgröße zu Michael/Sebastian passt (Details siehe Abschnitt 5, "Foto-Aufbereitung"). Änderung wurde parallel in `index.html` (Pfad-Referenz) und `preview.html` (base64-Einbettung) eingepflegt. **Arbeitsweise ab dieser Session:** Änderungen werden gezielt in die bestehenden Dateien eingearbeitet (kein neuer Ordner je Iteration), `index.html`/`styles.css` und `preview.html` werden synchron gehalten, und diese Doku wird bei jeder Änderung mitgepflegt.
16. (27. Juli 2026) Zwei Verfeinerungen im Projekte-Bereich: (a) Footer-Schranke neu gebaut — Footer öffnet nicht mehr durch das Momentum der Ankunfts-Geste, sondern nur durch eine bewusste zweite Abwärts-Geste nach ≥700ms Verweildauer (Details in Abschnitt 6a, "fünfte Iteration"). (b) Interner Scroll in der Projektbeschreibung entfernt, Textbox wächst auf Inhaltshöhe, Abstände gestrafft, Mobile-Scroll-Fallback erhalten (Abschnitt 6a, "Projektbeschreibung ohne internen Scroll").
17. (27. Juli 2026) Themenfelder-Kachel 3 „Nachfolgeregelung & Übernahmen": Hover-Rückseite mit echtem Text gefüllt (Überschrift „Gestärkt in die Zukunft" + zwei Bullets), Platzhalter `tbd` ersetzt. Kartenhöhe einheitlich erhöht, damit der längere Text ohne Scrollen passt (Details in Abschnitt 6a, „Themenfelder — Flip-Karten & Hover-Text").
18. (27. Juli 2026) Zweiter echter Referenz-Case eingefügt (Slide 2, Teal-Akzent): familiengeführte Schreinerei / Controlling im Handwerk, Ergebnis bis zu 5 % Umsatz. Ersetzt den bisherigen „Exemplary Content"-Platzhalter; Felder/Struktur wie Case 1. accent-2-Detail-Layout von 1- auf 2-spaltig umgestellt. Text vom Nutzer wörtlich übernommen (nur Typografie an den Rest der Seite angeglichen: Gedankenstriche „—", geschütztes Leerzeichen vor „%", „Kunden-unterschrift"→„Kundenunterschrift"). Slider unverändert 3 Slides + Klon.
19. (27. Juli 2026) Dritter echter Referenz-Case eingefügt (Slide 3, Wein-Akzent): familiengeführtes Handwerksunternehmen, Buy-and-Build/Übernahme, „dreifaches Wachstum". Platzhalter ersetzt. accent-3-Detail-Umsortierung (`order`-Regeln) entfernt (hätte bei 4 Blöcken die Reihenfolge zerwürfelt). Da Case 3 textreich ist, `.case-details` global leicht gestrafft (line-height/gap), damit alle Cases scrollfrei passen. Nutzertext wörtlich; nur Typografie/Grammatik minimal angeglichen (Gedankenstrich, Komma in „Was machen, um zu wachsen?"). Offen/zu bestätigen: „das Rational der Übernahme" (evtl. „Rationale" gemeint?) — bewusst unverändert gelassen.
20. (27. Juli 2026) Wisch-Navigation für den Cases-Slider ergänzt: Touch-Swipe (Mobil) und horizontales Trackpad-Wischen (PC), zusätzlich zu Pfeilen/Punkten. Details in Abschnitt 6, „Cases-Slider — Funktionsweise". Nur JS (beide `<script>`-Blöcke bzw. der Slider-Block in `index.html`/`preview.html`), kein CSS/HTML geändert.

---

## 10. Kontext, der in einer neuen Session sonst verloren geht

- Der Nutzer bevorzugt: kurze, direkte Antworten, Annahmen explizit benennen, vor größeren/irreversiblen Schritten Rückfrage halten, am Ende jeder Aufgabe geänderte/erstellte Dateien auflisten
- Der Nutzer ist bei Web-Entwicklung nach eigener Aussage "weitgehend unerfahren" — Erklärungen sollten entsprechend eingeordnet, nicht zu technisch-implizit sein
- Alle Preis-Informationen aus dem Business Plan sind bewusst **nirgendwo** auf der Website — bei zukünftigen Content-Ergänzungen darauf achten, dass das so bleibt, sofern nicht explizit anders gewünscht
