# Welle 1 — umgesetzte Änderungen

Grundlage: Design-Audit vom 13.08.2026. Diese Kopie (`fabrica-nova-site-welle1`)
enthält ausschließlich die Maßnahmen aus Welle 1. Der Originalordner
`fabrica-nova-site` ist unverändert.

Geändert wurden nur zwei Dateien: `index.html` und `styles.css`.
`preview.html`, `impressum.html`, `datenschutz.html`, `PROJEKT-DOKUMENTATION.md`
und alle Assets sind unangetastet übernommen.

## 1. Handlungsaufruf und Kontakt

- **Neu: CTA „Erstgespräch“** in der Kopfzeile (`.nav-cta`), verlinkt auf die neue
  Kontaktsektion. Angeschnittene Ecke als Facettenmotiv, damit der Button zur
  Marke gehört.
- **Neu: Sektion `#kontakt`** als sechste Fläche vor dem Footer — Einladung
  („Reden wir 30 Minuten. Ohne Agenda.“) plus Kontaktzeilen.
- Footer: `[E-Mail folgt]` durch die vorhandene Adresse `kontakt@fabrica-nova.de`
  ersetzt, zusätzlich Link „Erstgespräch anfragen“.
- Die Footer-Geste bleibt unverändert; der Footer ist jetzt aber nicht mehr der
  einzige Ort mit Kontaktdaten.

**Offen (Daten fehlen):** Telefonnummer und Standort stehen als sichtbar
markierte Platzhalter in `#kontakt` und im Footer, jeweils mit `TODO`-Kommentar
im Quelltext. Vor dem Livegang eintragen.

## 2. Team

- Name, Rolle und Kurzprofil stehen **dauerhaft sichtbar** unter jedem Foto
  (`.team-ident`). Das Hover-Overlay ist entfallen — es verdeckte das Gesicht und
  war auf Touchgeräten nie erreichbar.
- Gestrichelte Platzhalterrahmen der Fotos entfernt; der Facettenschnitt bleibt
  als Rahmung.
- CSS-Vererbungsfehler behoben: die Regel `.team-photo span` (Großbuchstaben,
  0,75 rem) stammte aus dem Platzhalterzustand und traf auch das Kurzprofil im
  Overlay. Regel gelöscht.
- Rollenbezeichnungen sind aus den Profiltexten abgeleitet und frei anpassbar:
  „Unternehmertum im Handwerk“, „Digitalisierung & Steuerung“, „Prozesse &
  Strategie“.

**Offen (Welle 2):** einheitliches Foto-Shooting, persönliche Kontaktwege
(E-Mail/LinkedIn) pro Person, „Werde Teil des Teams!“ als echter Link.

## 3. Themenfelder

- Jede Karte trägt jetzt einen **sichtbaren Nutzensatz** auf der Vorderseite
  (`.field-claim`) statt nur einer Überschrift.
- **Flip per Klick** statt nur per Hover: sichtbarer Schalter „Details“ mit
  `aria-expanded`, Rückseite mit „Zurück“, Schließen per `Esc`. Hover bleibt für
  Mausnutzer als Zugabe erhalten.
- Unter 800 px Breite **kein Flip**: beide Ebenen werden gestapelt gezeigt, die
  Schalter sind ausgeblendet. Damit ist der Inhalt auf jedem Gerät erreichbar.
- Das aufgeschnittene Rahmenquadrat (`.mark`) ist entfallen — es las sich als
  Renderfehler. Ein saubereres SVG-Motiv folgt in Welle 2.

## 4. Projekte

- **Autoplay entfernt.** Der Slider wechselte alle 5 Sekunden mitten im Lesen.
  Pfeile, Punkte, Tastatur, Touch-Swipe und Trackpad-Swipe funktionieren weiter.
- **Ergebnis als Kennzahl:** `−60 %`, `+5 %`, `3×` in großer Auszeichnung, mit
  einer Bezugszeile darunter, statt der Zahl mitten im Satz.
- **Bedienelemente sichtbar:** Pfeile als 40-px-Flächen mit Rahmen in einer
  Steuerzeile unter der Karte (vorher blasse 12-px-Dreiecke mitten im Text,
  1,79:1 Kontrast). Neu ein Zähler `01 / 03`.
- Aktiver Punkt in `--ink` statt Gold (Gold hatte auf Creme nur 1,99:1).

**Offen (Welle 2):** Texte auf etwa ein Drittel kürzen, Branchenlabel nach oben,
linke Kanten von Label und Kartentitel ausrichten.

## 5. Responsive Verhalten (abgeschnittene Inhalte)

- `min-height: 100svh` statt `100vh` (iOS-Safari rechnet `vh` inklusive
  Adressleiste).
- `scroll-snap-type: y proximity` statt `mandatory`, `scroll-snap-stop: always`
  entfernt. Sektionen dürfen jetzt höher als der Bildschirm sein, ohne dass
  Inhalt unerreichbar wird.
- Unter 800 px Fensterhöhe ist Snap ganz deaktiviert.
- Innere Scrollfläche der Projektkarten (`max-height: 44vh; overflow-y: auto`)
  entfernt — sie schnitt Text ab und war auf Touchgeräten nicht erkennbar.
- `overflow-x: clip` auf `html`: die Projekte-Bühne bricht über die volle Breite
  (50vw-Trick) und erzeugte bei sichtbarer vertikaler Scrollleiste einen
  horizontalen Scrollbalken.
- Kopfzeile auf kleinen Flächen: `.brand-mark` erhält `flex: 0 0 auto` — sonst
  schrumpfte die Wortmarke neben Navigation und CTA auf 0 px Breite. Unter 480 px
  entfällt der Menüpunkt „Start“ (die Bildmarke verlinkt dorthin).

Geprüft bei 1680×950, 1440×820, 1280×600, 834×1112, 844×390 und 390×844:
kein horizontaler Scrollbalken, alle Bedienelemente erreichbar, keine
JavaScript-Fehler.

## 6. Entwurfsbanner, Kontraste, Schriftstärke

- **Entwurfsbanner entfernt** (`.dev-notice`, `--notice-h: 0`) — es war das
  Erste, was Besucher sahen, in der lautesten Farbe der Palette.
- **Neue Farbtoken:** `--teal-ink: #3F6F76` für Labels auf Creme und Salbei
  (vorher 2,97:1 bzw. 2,67:1 — jetzt rund 4,6:1), `--teal-light: #8FBAC0` für
  Labels auf dunklem Grund, `--ink-75` für Sekundärtext in kleinen Größen
  (vorher 3,56:1, jetzt rund 5,4:1).
- Gold wird nicht mehr für Text oder Bedienzustände verwendet, nur noch für
  Flächen und Kanten.
- Grundschriftstärke von 300 auf 400 — 300 wirkte auf warmem Creme ausgewaschen,
  besonders unter Windows.

## 7. Nebenbefund behoben

`index.html` hatte ein überzähliges `</div>` in der Themenfelder-Sektion und ein
fehlendes `</div>` (`.cases-inner`) in der Projekte-Sektion. Beides korrigiert;
die Verschachtelung ist jetzt sauber (`html-validate` ohne Fehler).

## Nicht Teil von Welle 1

Schriften selbst hosten (DSGVO), Headline und Positionierung, Foto-Shooting,
Textkürzung in den Projekten, vollständige Navigation mit mitwanderndem
Aktivpunkt, mobiles Vollbildmenü, Impressum und Datenschutz, Meta-Angaben und
Favicon, Signaturmoment. Siehe Welle 2 und 3 im Audit.
