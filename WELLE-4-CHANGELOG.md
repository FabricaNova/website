# Welle 4 — Inhalts- und Kontaktdaten-Update (30.08.2026)

Auftrag: gezielte Text-, Layout- und Rechtsangaben-Änderungen. Bearbeitet wurden
`index.html`, `styles.css`, `impressum.html`, `datenschutz.html` und
`projekt-3.html`; `preview.html` anschließend mit `python3 build-preview.py`
neu erzeugt. `preview.html` **nie direkt bearbeiten** — Quelle ist index/styles.

## Menüleiste
- Logo-Bild im Header durch die Text-Wortmarke **„Fabrica Nova"** ersetzt
  (Klasse `.wordmark`), Größe `1.25rem` (kleine Screens `1.05rem`) — bewusst
  etwas größer als die Nav-Reiter (`0.85rem`). Auf allen Seiten (Startseite,
  Impressum, Datenschutz, Projekt-1/2/3).

## Startseite (Hero)
- H1: „Weniger Zettel. Mehr Marge." → **„Unternehmensführungs- / und
  Prozessberatung"** (Umbruch vor „und").
- Lede: „Prozess- und Führungsberatung" → **„Pragmatische Lösungen** für Handwerk
  und produzierenden Mittelstand."
- Zeile „Erste messbare Effekte in Wochen, nicht in Quartalen" entfernt.
- Rechte Grafik: statt Icon-ohne-Schriftzug auf grauer Facettenfläche jetzt das
  **Logo mit Schriftzug ohne Hintergrund** (graue Box, Innenrahmen und Facetten-
  Clip entfernt; `.hero-facet` zeigt nur noch das Logo).
- `og:title`/`og:description` an den neuen Hero angeglichen (Social-Preview).

## Vorgehen
- In das dritte (dunkelgrüne) Facettenquadrat `pf-3` wurde das **Fabrica-Nova-
  Zeichen (ohne Schriftzug)** mittig eingefügt (`.pf-logo`). Das Icon ist selbst
  `--ink` (dunkelgrün), daher auf der dunklen Fläche hell eingefärbt
  (`filter: brightness(0) invert(1)`). Erscheint mit Phase 3 der Sequenz.

## Team
- Michael Axenbeck: Rolle „Unternehmertum im Handwerk" → **„Unternehmertum &
  Handwerk"**; Bio → **„Über 10 Jahre kaufmännischer Geschäftsführer im
  Handwerk."**
- Dr. Sebastian Ifland: „… IT & finanzieller Steuerung." → **„… IT &
  kaufmännische Steuerung."**
- Bastian Richter: → **„Über 6 Jahre internationale Strategie- und
  Prozessberatung, 2 Jahre Prokurist im Handwerk."**

## Stimmen
- Der komplette Abschnitt „Stimmen" (Platzhalter-Zitate) wurde entfernt. Es gab
  keinen Menüpunkt darauf; die Scroll-Spy-Navigation liest die Sektionen
  dynamisch, daher keine JS-Anpassung nötig.

## Projekte / Cases
- Case 2 (Schreinerei), Effekt: „deutlich weniger" → **„reduzierter"**
  Verwaltungsaufwand.
- Case 3 (Übernahme), Hebel: Vergangenheit → generalistischer Ton — „erweitert,
  zentralisiert, zusammengeführt" → **„erweitern, zentralisieren,
  zusammenführen"**.
- Detailseite `projekt-3.html`: Ansatz-Absatz in **Soll-/Zukunftsform** gebracht
  („Das Ergebnis sieht … vor", „erweitert", „wirken sich … aus", „führt zu").
  Abschnitt **„Umgesetzte Hebel" → „Ausgearbeitete Hebel"**, Text ebenfalls
  generalisiert.
- Offen gelassen (unverändert, zur Klärung): „das Rational der Übernahme" im
  Fazit — evtl. „Rationale" gemeint.

## Kontakt / Rechtliches
- E-Mail überall auf **info@fabricanova.de** geändert. *Hinweis:* Diese Domain
  (`fabricanova.de`, ohne Bindestrich) weicht von der bisher hinterlegten
  Website-Domain `fabrica-nova.de` (canonical/OG-URLs) ab — bitte bestätigen.
- Telefon: alle Platzhalter entfernt (Kontaktblock, alle Footer, Impressum,
  Datenschutz).
- Kontakt-Abschnitt: Angebots-Label „Vorab, ohne Gespräch" → **„Für kleine
  Betriebe"**; Standort **„München, Unterföhring"** eingetragen.
- **Impressum** mit echten Daten gefüllt: Fabrica Nova GmbH, Alte Münchner
  Straße 45, 85774 Unterföhring; vertreten durch Michael Axenbeck, Dr. Sebastian
  Ifland, Bastian Richter; Amtsgericht München, HRB 315496; Verantwortlich für
  den Inhalt entsprechend. USt-IdNr-Abschnitt entfernt (besteht noch nicht).
  Hinweisbanner auf „vor Livegang anwaltlich prüfen" abgeschwächt.
- **Datenschutz** (über den Auftrag hinaus, aus Konsistenz): „Verantwortlicher"
  mit denselben Firmendaten gefüllt, Telefon entfernt, Banner angepasst. Weiter
  offen und bewusst als Platzhalter belassen: Hosting-Anbieter, zuständige
  Aufsichtsbehörde, Löschfrist, Stand-Datum.

## Nicht verifiziert
- Rein visuell (Header-Wortmarke, Hero-Logo ohne Box, Icon auf pf-3) konnte in
  dieser Session **nicht im Browser gerendert** werden (Chrome-Extension nicht
  verbunden). Bitte in `preview.html` gegenprüfen.

## Nachtrag (30.08.2026)

- **Header-Wortmarke als Grafik:** Der ausgeschriebene Text „Fabrica Nova" wurde
  durch die **Logo-Schrift als Bild** ersetzt (`assets/fabrica-nova-wordmark.png`,
  aus `fabrica-nova-logo.png` extrahiert) — gleiche geometrische Schrift wie im
  Logo (u. a. „A" ohne Querbalken). Höhe `clamp(14px, 2vw, 22px)`. Auf allen
  Seiten.
- **Download-PDF aktualisiert** (`assets/Fabrica-Nova-Zettelwirtschaft-Check.pdf`):
  E-Mail → `info@fabricanova.de`, Telefon-Platzhalter entfernt. Umgesetzt als
  **chirurgische Bearbeitung der bestehenden PDF** (Kontaktzeile überdeckt und
  neu gesetzt, exakt gleiche Schrift/Größe/Position) — bewusst NICHT über
  weasyprint neu gerendert, weil dessen Seitenumbruch die Fragen 08/09 auf Seite 1
  abgeschnitten hätte. Alle 12 Fragen und das Layout bleiben unverändert. Die
  Quelle `_quellen/zettelwirtschaft-check.src.html` wurde parallel angepasst.
- **Vorgehen-Icon (pf-3):** Farbe von hell/weiß auf die **Hintergrundfarbe des
  Abschnitts (`--sage`, #ECEBE3)** geändert — wirkt wie aus dem dunklen Quadrat
  ausgestanzt. Zuerst als CSS-Maske umgesetzt; die wurde jedoch nicht in jedem
  Renderer dargestellt (nur das grüne Quadrat war sichtbar). Fix: fertig in Sage
  eingefärbtes PNG (`assets/fabrica-nova-icon-sage.png`) als normales
  `<img class="pf-logo">` — zuverlässig in jedem Renderer.
- **Adresse korrigiert:** „Alte Münchener Straße" → **„Alte Münchner Straße"** in
  Impressum und Datenschutz (jede Fundstelle).

## Mobile-Optimierung (31.08.2026) — Desktop unverändert

Alle Änderungen ausschließlich in `@media (max-width: 640px)`; die Desktop-
Darstellung bleibt exakt gleich.

- **Hero-H1 wurde abgeschnitten:** „Unternehmensführungs-" ist bei voller
  H1-Größe (`--t1`, min 2.5rem ≈ 40px) breiter als ein Handy-Screen. Auf Mobil
  jetzt `font-size: clamp(1.6rem, 7.4vw, 2.4rem)` (per Schriftmessung so gewählt,
  dass das Wort ab 320px Breite auf eine Zeile passt) plus `hyphens: auto` als
  Fallback.
- **Footer „Kontakt"/„Rechtliches" nicht auf gleicher Höhe:** Ursache war
  `display:flex; justify-content:space-between; flex-wrap:wrap` — die Spalten
  brachen auf verschiedene Zeilen um. Auf Mobil jetzt festes 2-Spalten-Raster
  (`display:grid; grid-template-columns:1fr 1fr; align-items:start`), die Marke
  spannt oben über die volle Breite, darunter beide Spalten oben bündig.
- **Absicherung gegen abgeschnittene lange Titel** (z. B.
  „Handwerksunternehmen"): `overflow-wrap: break-word; hyphens: auto` für
  Case-/Projekt-Überschriften auf Mobil (wirkt nur, wenn ein Wort sonst
  überliefe — kein Effekt auf Desktop).
- **Nicht selbst gerendert:** Ein Headless-Browser ließ sich in dieser Session
  nicht einrichten. Die Fixes sind CSS-seitig hergeleitet/berechnet — bitte am
  Handy gegenprüfen.

## Team-Foto Bastian Richter neu (03.09.2026)

Neues Porträt (enger Kopf-Schulter-Shot, 1534×1536, dunkelgrauer Verlaufs-
hintergrund) an die beiden anderen angeglichen und ersetzt:

- **Hintergrund freigestellt und auf hell (~232) ersetzt** — der Original-
  Hintergrund war mit ~120–157 deutlich dunkler als bei Michael (~220) und
  Sebastian (~243) und hätte im Duotone-Layer ein dunkles Tile ergeben. Da der
  ML-Freisteller (rembg) offline nicht ladbar war, per Heuristik: neutrale (gering
  gesättigte) Flächen im mittleren Helligkeitsband, dann nur die **vom Bildrand
  zusammenhängenden** Bereiche ersetzt (Flood-Fill) — so blieb der dunkle Anzug
  (gleiche Helligkeit wie der BG) erhalten.
- **Auf 900×1350 gerahmt** wie Michael/Sebastian (Gesichtsgröße ~15 % der Höhe,
  gleiche Kopfposition), damit alle drei im selben Kopf-Schulter-Ausschnitt sitzen.
- **`--zoom` der dritten Karte von 1.55 auf 1.06** gesenkt (das alte, weit
  entfernte Foto brauchte starken Zoom; das neue nicht mehr). Endergebnis über die
  komplette Render-Pipeline (Cover + object-position + zoom + Graustufen) simuliert
  und mit Michael/Sebastian verglichen — Kopfgrößen und Bildwelt stimmen überein.
- `index.html` musste **nicht** geändert werden (gleicher Dateiname).

**Nachbesserung (03.09.2026):** Die erste Fassung hatte noch Farbfehler an Kopf/Sakko
und einen ausgeschnitten/unscharf wirkenden Körper (heuristische Maske + weiches
Einblenden). Neu freigestellt mit **GrabCut** (OpenCV, seeded mit rand­zusammen­hängender
BG-Maske + Vordergrund-Kern), Kante median-geglättet, scharf auf einheitlich hellen
Hintergrund gesetzt (kein Feather-Dissolve mehr). Ergebnis: saubere Haar-/Anzugkanten,
kein Halo, natürlicher Studio-Look. `--zoom` bleibt 1.06. Nur
`assets/team/team-bastian-richter.jpg` ersetzt + `preview.html` neu gebaut.

**Finale Lösung — ohne Freistellen (03.09.2026):** Auch nach der GrabCut-Version
blieb an der unteren Kante eine sichtbare „Ausschneide-Spur" (auf Mobil, wo die
höhere Foto-Box weiter nach unten reicht). Deshalb ganz ohne Freistellen gelöst:
Bastians **echtes Foto mit durchgehendem Hintergrund** wird auf die Breite
eingepasst und die Belichtung moderat angehoben (Gamma-Kurve; sein Foto war mit
Gesicht ~105 / BG ~120 deutlich dunkler als Michael ~157/229). Dadurch sitzt der
untere Bildabschluss **unterhalb** des in der Karte sichtbaren Bereichs (Desktop
wie Mobil) — es gibt gar keine Schnittkante mehr, nur echtes Foto mit realem
Hintergrund. Kein Halo, kein Cutout. `--zoom` der dritten Karte auf **1.00**
(das eingepasste Foto hat die passende Kopfgröße). Ergebnis über die Render-
Pipeline für Desktop- und Mobile-Box geprüft und mit Michael/Sebastian verglichen.
