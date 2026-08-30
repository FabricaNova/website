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
