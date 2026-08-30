# Welle 2 — umgesetzte Änderungen

Grundlage: Design-Audit vom 13.08.2026, Maßnahmenblock „Welle 2 — Substanz und
Marke“. Umgesetzt in derselben Arbeitskopie wie Welle 1
(`fabrica-nova-site-welle1`); der Originalordner `fabrica-nova-site` bleibt
unverändert. Welle 1 ist in `WELLE-1-CHANGELOG.md` dokumentiert.

**Neu: `preview.html` wird jetzt automatisch erzeugt.** Siehe Abschnitt 8 —
nach jeder Änderung an `index.html` oder `styles.css` einmal
`python3 build-preview.py` ausführen.

## 1. Positionierung und Hero

- **Neue Headline: „Weniger Zettel. Mehr Marge.“** statt „Exzellenz im
  Mittelstand.“ — die alte Zeile war eine Kategorie-Aussage, die über jeder
  Beratungsseite stehen könnte. Die neue ist konkret, merkfähig und wird durch
  Projekt 2 belegt.
  <br>Zwei Alternativen stehen als Kommentar im Quelltext direkt darüber:
  „Aus Aufwand wird Marge.“ und „Vier Wochen bis zum ersten Effekt.“
  **Das ist eine redaktionelle Entscheidung — bitte gegenlesen.**
- Unterzeile benennt jetzt beide Zielgruppen („Handwerk und produzierenden
  Mittelstand“), eine dritte Zeile setzt das Tempoversprechen: „Erste messbare
  Effekte in Wochen, nicht in Quartalen.“
- Der redundante Kicker „FABRICA NOVA“ direkt unter dem Logo ist entfallen.
- **Zwei Handlungsaufrufe im Hero:** „Erstgespräch“ (Fläche) und „Projekte
  ansehen“ (leise Variante) — der erste Bildschirm hat jetzt einen Ausgang.

## 2. Typo-Skala und Raster

- **Genau fünf Textstufen** als Token in `:root` (`--t1` bis `--t5`) plus eine
  Display-Stufe (`--display`) für die Kennzahlen. Vorher lagen Hero-Unterzeile
  und Vorgehen-Text auf derselben Größe wie die H1 — es gab keine Hierarchie.
- **Linke Kanten fluchten:** Die Projektkarten haben keine horizontale
  Polsterung mehr (`padding-inline: 0`). Label, Überschrift und Karteninhalt
  beginnen an derselben Linie wie der Rest der Seite; der Salbeigrund läuft
  weiterhin über die volle Breite.
- Hervorhebungen im Vorgehen-Text nutzen nur noch Schriftgewicht plus eine
  Goldunterlegung. Das zusätzliche `font-size: 1.12em` hob die Wörter aus der
  Grundlinie und ließ die Zeilen wellig wirken.

## 3. Projekte: Situation → Hebel → Effekt

- Texte von vier Blöcken à 30–60 Wörtern auf **drei Blöcke à 12–17 Wörter**
  gekürzt, in der Reihenfolge **Situation → Hebel → Effekt**. Damit erzählt die
  Karte dieselbe Dramaturgie wie das Vorgehen (Diagnose, Zielbild, Umsetzung).
  Alle Fakten und Zahlen sind aus den Originaltexten übernommen, nichts ergänzt.
- Drei Spalten auf Desktop, zwei ab 900 px, eine ab 640 px.
- **Branche und Größe stehen jetzt als Label über dem Titel** — das ist der
  Spiegel, in dem sich die Zielgruppe erkennt.

## 4. Team: einheitliche Bildwelt

- **Duotone-Behandlung als Marken-Layer:** Die drei Porträts liegen auf
  cremefarbenem Grund, werden entsättigt und per `multiply` verrechnet, ein
  zweiter Ton hebt die Schatten leicht ins Petrol. Wirkung: die drei
  unterschiedlichen Hintergründe (weiß, grau, Verlauf) werden zu einem
  Papierton, die unterschiedlichen Lichtstimmungen fallen nicht mehr auf.
- **Kopfgrößen angeglichen** über eine Zoom-Variable pro Person
  (`--zoom: 1.02 / 1.14 / 1.55`), Werte jederzeit nachjustierbar.
- „Werde Teil des Teams“ ist jetzt ein **echter Link** auf den Kontaktabschnitt
  (vorher `aria-hidden`, kein Link, erst ab 1180 px sichtbar). Das
  Ausrufezeichen ist entfallen — es passte nicht zur ruhigen Tonalität.

> **Das bleibt eine Übergangslösung.** Sie ersetzt kein einheitliches Shooting:
> gleicher Hintergrund, gleiche Brennweite, Augen auf etwa 38 % der Bildhöhe,
> Format 3:4. Empfehlung weiterhin Werkstatt- oder Baustellenkontext statt
> Studio — das differenziert sofort gegen jede Strategieberatung.
> Zum Abschalten des Duotone: den markierten Block in `styles.css`
> (`.team-photo img`, `.team-photo::after`) und den Cremegrund in
> `.team-photo` entfernen.

## 5. Navigation

- **Vollständig:** Themenfelder, Vorgehen, Team, Projekte — plus CTA
  „Erstgespräch“. „Start“ ist entfallen, dafür ist die Bildmarke da.
- **Aktiver Punkt wandert mit** dem Scrollen (`IntersectionObserver`,
  `aria-current`). Vorher stand die Markierung statisch auf „Start“.
- **Mobiles Vollbildmenü** unter 860 px: Facetten-Schaltfläche, die sich zum
  Kreuz dreht, Menü mit fünf Zielen und CTA, schließt per Klick, per `Esc` und
  automatisch, wenn das Fenster breit genug wird.

## 6. Facettenmotiv und Gold

- Die Facette hat jetzt **eine einzige Definition** als CSS-Token
  (`--facet-clip`, `--facet-clip-s`) und wird von Karten, Fotos, Buttons und
  der Schaltfläche wiederverwendet.
- Die Marke in den Themenfeldern ist ein **echtes SVG mit geschlossener
  Kontur**. Vorher war es ein umrandetes Quadrat, dessen Rand vom `clip-path`
  aufgeschnitten wurde — es las sich als unfertiges Kästchen.
- **Drift-Animation entfernt.** Die beiden Flächen im Vorgehen-Hintergrund
  stehen still, sauber im Anschnitt, und blenden beim Laden einmalig ein.
- Gold wird nirgends mehr für Text oder Bedienzustände verwendet — nur für
  Flächen, Kanten und die Unterlegung im Vorgehen-Text.

## 7. Schriften, Meta, Favicon

- **Hanken Grotesk wird selbst gehostet** (`assets/fonts/`, Gewichte 300/400/
  600/700, Subsets latin und latin-ext mit `unicode-range`, woff2,
  `font-display: swap`, Preload für die zwei wichtigsten Schnitte).
  Der `@import` von `fonts.googleapis.com` ist entfallen — er übertrug die
  IP-Adresse jedes Besuchers in die USA (in Deutschland abgemahnt,
  LG München I, 3 O 17493/20). Lizenz: SIL Open Font License 1.1, Textdatei
  liegt bei den Schriften.
- **Meta-Angaben:** Titel auf 59 Zeichen und auf beide Zielgruppen umgestellt,
  `meta description`, Open-Graph- und Twitter-Card-Angaben, `theme-color`,
  `canonical`.
- **`assets/og-image.png`** (1200 × 630) neu erzeugt, in der echten Hausschrift
  und Hausfarbe — das ist die Fläche, die bei WhatsApp und LinkedIn erscheint.
- **Favicons** aus `fabrica-nova-icon.png` erzeugt: 32 px, 48 px,
  Apple-Touch-Icon 180 px.
- Rechtsseiten haben `robots: noindex, follow`.

**Offen:** In `canonical` und `og:url` steht die vermutete Domain
`https://www.fabrica-nova.de/` — vor dem Livegang gegen die echte tauschen
(`TODO`-Kommentar im Quelltext). Für ein in jeder Größe scharfes Favicon wäre
eine echte SVG-Fassung aus der Logo-Vektordatei besser als die PNG-Ableitung.

## 8. preview.html wird jetzt erzeugt, nicht gepflegt

`preview.html` ist eine in sich geschlossene Einzeldatei (CSS, Bilder und
Schriften eingebettet) — praktisch zum Weiterschicken, aber bisher eine zweite
Wahrheit, die von Hand nachgezogen werden musste.

Neu: **`build-preview.py`** erzeugt sie aus `index.html`, `styles.css` und
`assets/`.

```
python3 build-preview.py
```

- `preview.html` nie direkt bearbeiten — Änderungen in `index.html` oder
  `styles.css` machen und das Skript laufen lassen. Ein Warnhinweis steht jetzt
  auch als Kommentar oben in der Datei.
- Die Schriften stecken als Data-URI im Stil, deshalb funktioniert die Vorschau
  per Doppelklick ohne Webserver und ohne Internet. Der erweiterte
  Latin-Bereich wird in der Vorschau weggelassen (spart rund 50 KB, für
  deutsche Texte ohne Wirkung).
- Aktuelle Größe: 514 KB.
- Das Skript braucht nur Python 3.9+ und keine zusätzlichen Pakete.

## 9. Rechtliche Seiten

- **Footer war auf Impressum und Datenschutz komplett unsichtbar** — er ist auf
  der Startseite fixiert und per `translateY(100%)` ausgefahren, und auf den
  Unterseiten öffnete ihn kein Skript. Neu: Klasse `is-static`, damit er dort
  normal im Fluss steht.
- Das Entwurfsbanner war noch im Markup, obwohl sein CSS in Welle 1 entfernt
  wurde — es hätte als unformatierter Text über der Seite gestanden. Entfernt.
- **Impressum** um die üblichen Pflichtabschnitte ergänzt: Verantwortlich nach
  § 18 Abs. 2 MStV, Verbraucherstreitbeilegung, Haftung für Inhalte und Links,
  Urheberrecht (inkl. Schriftlizenz). Verweis auf § 5 DDG statt TMG.
- **Datenschutzerklärung** ergänzt: Hosting und Server-Logfiles mit
  Rechtsgrundlage Art. 6 Abs. 1 lit. f DSGVO, ausdrücklicher Hinweis auf die
  lokal gehosteten Schriften (keine Google-Fonts-Verbindung), keine Cookies und
  kein Tracking, Speicherdauer, TLS, vollständige Betroffenenrechte,
  Beschwerderecht bei der Aufsichtsbehörde.
- Alle offenen Pflichtfelder sind als <span style="color:#96305C">*[…]*</span>
  markiert und im Text durchsuchbar (`legal-ph`): 11 im Impressum, 9 im
  Datenschutz.

> **Nicht abgeschlossen, und das kann es hier auch nicht sein.** Firma,
> Rechtsform, Registerdaten, Vertretungsberechtigte, USt-ID, Telefon,
> Hosting-Anbieter und zuständige Aufsichtsbehörde liegen laut Entwurfsstand
> erst nach dem Notarprozess vor. Die Seiten sind als vollständige Vorlage
> angelegt; eine anwaltliche Prüfung vor Veröffentlichung ist zu empfehlen.
> Ich bin kein Anwalt — dieser Text ist keine Rechtsberatung.

## Prüfung

- `html-validate` ohne Beanstandung für `index.html`, `preview.html`,
  `impressum.html`, `datenschutz.html`; `csstree-validator` ohne Beanstandung
  für `styles.css`.
- Gerendert und geprüft bei 1680 × 950, 1440 × 820, 1280 × 600, 834 × 1112,
  844 × 390 und 390 × 844: kein horizontaler Scrollbalken, Kopfzeile passt
  überall in eine Zeile, keine fehlenden Bilder, keine JavaScript-Fehler.
- `preview.html` zusätzlich über `file://` geprüft (so wie sie per Doppelklick
  geöffnet wird): Schriften geladen, alle fünf Bilder vorhanden, Menü und
  Slider funktionsfähig.
- Kontrastwerte der neuen Farben nach WCAG 2.1 nachgerechnet: Labels 5,2:1,
  Case-Labels auf Salbei 4,7:1, Sekundärtext 5,7:1, Footer-Überschriften 5,7:1,
  Text auf der Goldunterlegung 8,6:1, Platzhaltermarkierung 6,8:1 — alle über
  der 4,5:1-Schwelle für kleinen Text.
- Interaktionen durchgeklickt: Themenfeld-Karten (Klick, `Esc`), Slider (Pfeile,
  Punkte, Zähler), Vollbildmenü (öffnen, schließen, Fensterbreite),
  mitwandernder Navigationspunkt.

## Was aus Welle 3 offen bleibt

Signaturmoment (gepinnte Sequenz, in der die Facette die drei Phasen aufbaut),
Kundenstimmen und regionale Verortung, Detailseiten je Projekt,
Inhaltsangebot („Zettelwirtschaft-Check“ als PDF gegen E-Mail), englische
Variante nur bei internationaler Akquise. Dazu die Datenpunkte, die niemand
außer euch liefern kann: Telefonnummer, Standort, Registerdaten,
Foto-Shooting, echte Domain.
