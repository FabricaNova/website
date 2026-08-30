# Korrekturen nach dem Durchklicken — 13.08.2026

Drei Rückmeldungen, ein gemeinsamer Auslöser: **das mobile Vollbildmenü lag als
unsichtbare Fläche über der ganzen Seite und hat jeden Klick abgefangen.**

Geändert: `index.html`, `styles.css`, `preview.html` (neu erzeugt).

## 1. Der eigentliche Fehler: unsichtbares Overlay über der Seite

`.nav-panel` (das mobile Menü) trägt im Markup das Attribut `hidden`. Dessen
`display: none` kommt aus dem Browser-Stylesheet und wurde von meiner eigenen
Regel `.nav-panel { display: flex }` überstimmt. Ergebnis: ein Element mit
`position: fixed`, `inset: 0`, `opacity: 0` und `z-index: 99` lag unsichtbar
über dem gesamten Seiteninhalt — bei **jeder** Fenstergröße.

Sichtbar war nichts, kaputt war viel: Slider-Pfeile, Punkte, „Details“,
„Fall im Detail“, die Hero-Buttons, die Kontaktzeilen — alles im Bereich unter
der Kopfzeile war nicht anklickbar. Nur die Kopfzeile selbst funktionierte,
weil sie mit `z-index: 100` darüber liegt. Deshalb ließ sich „Erstgespräch“
klicken, aber im Slider nichts.

**Behoben** mit einer Zeile im Reset:

```css
[hidden] { display: none !important; }
```

Das ist die Standardabsicherung gegen genau diesen Fehler und gilt jetzt für
jedes Element mit `hidden`, nicht nur für das Menü.

Nachgeprüft: An zwölf Bedienelementen wurde per Trefferpunkt-Test geprüft, ob
tatsächlich das Element selbst den Klick bekommt — auf Desktop und Handy alle
frei. In sechs Fenstergrößen liegt kein Overlay mehr über der Seite.

## 2. Laufbanner bei den Projekten ist zurück

Der automatische Durchlauf war in Welle 1 absichtlich abgeschaltet worden
(meine Begründung: ein selbstlaufender Wechsel unterbricht das Lesen). Da er
gewünscht ist, läuft er wieder — aber gebremst und höflich:

- **Intervall 8 Sekunden**, einstellbar im Markup:
  `<section class="case-slider" … data-interval="8000">`. Ein anderer Wert dort
  genügt, kein Skript anfassen.
- **Hält an**, sobald die Maus über dem Slider ist, etwas darin den Fokus hat,
  gewischt wird oder der Abschnitt nicht im Bild ist (`IntersectionObserver`).
  Nach dem Verlassen läuft er weiter.
- **Startet nicht**, wenn im Betriebssystem „Bewegung reduzieren“ aktiv ist.
- Jede manuelle Bedienung (Pfeil, Punkt, Wischen, Trackpad) setzt den Takt neu,
  damit die Folie nicht direkt nach dem Weiterklicken wechselt.
- Der Zähler `01 / 03` hat kein `aria-live` mehr — bei automatischem Wechsel
  hätte ein Screenreader alle acht Sekunden dazwischengesprochen.

Manuelles Blättern ist geprüft: Pfeil vor durch alle drei Folien und zurück
über den Anfang hinaus, Sprung über die Punkte, Zähler und sichtbare Folie
stimmen jeweils überein.

## 3. „Details“ führt jetzt zum passenden Referenzprojekt

| Themenfeld | Ziel |
|---|---|
| Prozesse & Digitalisierung | Projekt 1 — Fertigender Mittelstand & Serviceprovider |
| Unternehmensführung | Projekt 2 — Familiengeführte Schreinerei |
| Nachfolgeregelung & Übernahmen | Projekt 3 — Familiengeführtes Handwerksunternehmen |

Der Klick scrollt zum Abschnitt „Projekte“ **und stellt den Slider auf die
passende Folie**. Umgesetzt als echter Link (`href="#cases"` plus
`data-case="1|2|3"`): ohne JavaScript landet man immer noch beim richtigen
Abschnitt, nur ohne Vorauswahl.

Damit hat sich die Bedienlogik der Kacheln verschoben — vorher drehte der
Button die Karte, jetzt führt er weiter:

- **Zeigegerät:** Wer über die Kachel fährt, sieht die Rückseite mit dem
  Detailtext. „Details“ ist auf beiden Seiten sichtbar und führt zum Projekt.
- **Ohne Hover** (Touch-Tablets und Handys, jetzt über `@media (hover: none)`,
  nicht mehr nur unter 800 px Breite): kein Drehen, beide Ebenen stehen
  untereinander. Es bleibt nichts verborgen.
- **Tastatur:** Ein Tabstopp pro Kachel, der zum Projekt führt. Der zweite,
  gleichlautende Link auf der Rückseite ist aus Tab-Reihenfolge und
  Vorlesemodus genommen, damit nichts doppelt angekündigt wird. Jeder Link
  trägt zusätzlich den Projektnamen für Screenreader.

Nebeneffekt, den ich offen sagen sollte: Wer mit der Tastatur navigiert und
sehen kann, erreicht den Detailtext auf der Rückseite am Desktop nicht mehr —
das Drehen hängt am Hover. Weil seit Welle 2 der Nutzensatz vorn steht, ist
dort kein tragender Inhalt mehr versteckt. Wenn das stören soll, ist die
saubere Lösung, die Stichpunkte dauerhaft auf die Vorderseite zu holen und den
Flip ganz aufzugeben — sag Bescheid.

## 4. Zettelwirtschaft-Check öffnet sich jetzt

Der Button hatte das Attribut `download`. Damit lädt der Browser die Datei
still in den Download-Ordner, statt sie anzuzeigen — es sah aus, als würde
nichts passieren. Jetzt öffnet er das PDF in einem neuen Tab
(`target="_blank" rel="noopener"`), Beschriftung entsprechend:
**„Direkt öffnen (PDF, 2 Seiten)“**. Herunterladen kann man es aus der
PDF-Ansicht heraus weiterhin.

Hinweis: In `preview.html` ist das PDF nicht eingebettet (es soll speicherbar
bleiben). Der Link funktioniert dort, solange die Datei im Projektordner neben
`assets/` liegt — nicht, wenn `preview.html` einzeln verschickt wird.

## Prüfung

- `html-validate` und `csstree-validator` ohne Beanstandung.
- Sechs Fenstergrößen (1680 × 950 bis 844 × 390): kein Overlay über der Seite,
  kein horizontaler Scrollbalken, keine JavaScript-Fehler.
- Slider: manuelles Blättern vor/zurück/über Punkte, automatischer Wechsel
  beobachtet, Pause bei Mouseover bestätigt.
- „Details“ 1–3 einzeln geklickt: jeweils richtige Folie und Zähler.
- Rückseiten-Link nach Hover geklickt: springt korrekt.
- Mobiles Menü öffnet, schließt beim Klick auf einen Punkt, `hidden` wird
  wieder gesetzt.
- Alles zusätzlich in `preview.html` über `file://` geprüft: Blättern und
  „Details“-Sprung funktionieren dort ebenso.

---

## Ergänzung: Teamfotos färben sich beim Überfahren

Neu: Fährt man über eine Teamkarte, läuft die Farbe ins Foto zurück — die
Entsättigung fährt in 0,45 s auf null, der zweite Ton blendet aus.

- **Auslöser ist die ganze Karte**, nicht nur das Bild: das Foto färbt sich also
  auch, wenn man beim Lesen von Name und Profil darüber ist.
- Der `multiply`-Modus bleibt bewusst aktiv. Dadurch wird das ursprüngliche
  Weiß im Hintergrund weiterhin zum Papierton der Seite — das Foto bleibt auch
  in Farbe im Layout verankert und fällt nicht als weißer Kasten heraus.
- **Auf Touchgeräten unverändert:** die Regel steckt in
  `@media (hover: hover) and (pointer: fine)`. Ohne Zeigegerät gibt es keinen
  Hover-Zustand, und die einheitliche Bildwelt bleibt dort erhalten.
- Bei „Bewegung reduzieren“ im Betriebssystem schaltet es ohne Animation um.

Nebeneffekt, der die Sache gestalterisch trägt: Der Ruhezustand ist die
einheitliche Duotone-Bildwelt, der Hover zeigt den Menschen dahinter. Damit
wird aus der Übergangslösung für die drei ungleichen Vorlagen ein bewusster
Effekt. Falls später ein einheitliches Shooting kommt, kann der Ruhezustand
so bleiben — er funktioniert dann sogar besser.

Umgesetzt nur in `styles.css` (und damit in der neu erzeugten `preview.html`),
`index.html` blieb unverändert.

---

## Ergänzung: Footer hängt jetzt am Kontaktabschnitt

Der Footer war fixiert und fuhr nur über eine erlernte Scroll-Geste ein: eine
**neue** Abwärtsbewegung auf der letzten Sektion, mindestens 700 ms nach der
Ankunft dort und nach einer Eingabepause von 300 ms. Technisch elegant, in der
Bedienung eine Zumutung — man musste es wissen und dann mehrfach versuchen.

**Neu: der Footer ist ein normaler Block direkt unter dem Kontaktabschnitt.**

- `position: static`, keine Verschiebung, kein Skript. Der komplette
  Gesten-Mechanismus (rund 3.900 Zeichen JavaScript samt Wheel-, Touch- und
  Tastatur-Abfangen) ist entfallen. Damit fällt auch weg, dass die Seite am
  Ende Scroll-Eingaben verschluckt hat.
- **Der Kontaktabschnitt erzwingt keine volle Bildschirmhöhe mehr.** Dadurch
  liegen Kontaktangaben und Footer im selben Blick: Wer über „Erstgespräch“
  dorthin springt, sieht unten schon rund 250 px dunkle Fläche hereinragen —
  ein sichtbarer Hinweis, dass da noch etwas kommt. Eine normale Radbewegung
  bringt den Footer vollständig ins Bild.
- **Kein Snap-Ziel mehr am Seitenende** (`scroll-snap-align: none` auf dem
  Kontaktabschnitt). Sonst hätte das Snapping den Footer wieder nach oben
  weggezogen. Letzter Haltepunkt ist jetzt die Sektion „Stimmen“.
- **Goldene Haarlinie** (3 px) als Oberkante des Footers — dieselbe Kante wie
  auf den Projektkarten, damit der dunkle Block als Abschluss gesetzt wirkt und
  nicht als abgeschnittener Rest.
- Die Sonderklasse `is-static`, die den Footer auf den Unterseiten sichtbar
  machte, ist überflüssig geworden und wurde aus CSS und aus allen fünf
  Unterseiten entfernt.

Geprüft in sechs Fenstergrößen, jeweils mit echtem Mausrad bis zum Seitenende:
Footer überall vollständig sichtbar, Seitenende erreicht, „Impressum“ im Footer
anklickbar. Auf Impressum, Datenschutz und den Projektseiten steht der Footer
ebenfalls normal im Fluss. In `preview.html` identisch geprüft.

### Nachjustiert: Luft zwischen Angebot und Footer

Beides gemacht, in Maßen — der Bereich wirkte gedrückt, weil der Farbwechsel
auf die dunkle Fläche fast ohne Abstand kam.

- **Abstand unter dem Angebotsblock** von 44 px auf 95 px (Desktop) erhöht:
  `padding-bottom: clamp(3.5rem, 10vh, 7rem)` am Kontaktabschnitt. Skaliert mit
  der Fensterhöhe — 82 px auf einem 820er Laptop, 111 px auf dem Tablet, 84 px
  auf dem Handy.
- **Footer flacher:** Polsterung von `clamp(2.5rem, 6vh, 4rem)` auf
  `clamp(1.9rem, 4vh, 2.75rem)`, dazu die Abstände über der Copyright-Zeile
  gestrafft. Höhe damit von 326 px auf 273 px (Desktop), rund 16 Prozent
  weniger.

Netto bleibt die Gesamthöhe fast gleich, das Verhältnis kippt aber zugunsten des
hellen Bereichs. Beim Sprung auf „Kontakt“ ragt der Footer weiterhin sichtbar
herein (186 px auf dem Desktop, 90 px auf dem Laptop) — der Hinweis, dass unten
noch etwas kommt, bleibt also erhalten.

Beide Werte sind einzelne Zahlen in `styles.css`, falls du weiter nachjustieren
willst: `.snap-section.contact { padding-bottom }` für die Luft darüber,
`.site-footer { padding }` für die Footer-Höhe.

---

## Mobile Bedienung: acht Befunde, alle behoben

Geprüft in vier iPhone-Formaten (375 × 667, 390 × 844, 430 × 932 und
844 × 390 im Querformat) mit Touch-Events, iOS-Kennung und dreifacher
Pixeldichte.

**Einschränkung, die ich offen sagen muss:** In dieser Umgebung steht nur die
Chromium-Engine zur Verfügung, nicht WebKit. Ich habe also mit
Mobil-Emulation geprüft, nicht auf echtem iOS Safari. Die Befunde unten sind
entweder gemessen oder betreffen dokumentiertes iOS-Verhalten. Bitte einmal
auf dem Gerät gegenprüfen.

### 1. Das Laufbanner stand nach dem ersten Antippen für immer still

Der schwerste Befund, reproduzierbar gemessen. Touchgeräte feuern beim
Antippen ein **emuliertes `mouseenter` ohne späteres `mouseleave`**. Meine
Pause-bei-Mouseover-Logik setzte damit `paused = true` — und nichts hob das je
wieder auf. Nach der ersten Berührung der Projektkarte wechselte keine Folie
mehr.

Zweite Ursache derselben Sorte: Ein Tipp auf Pfeil oder Punkt hinterlässt den
**Fokus** auf dem Button, und die Pause-bei-Fokus-Logik hielt den Lauf ebenfalls
dauerhaft an.

Behoben: Die Mouseover-Pause wird nur noch auf Geräten mit echtem Zeigegerät
registriert (`matchMedia('(hover: hover)')`), die Fokus-Pause greift nur bei
**sichtbarem** Fokus (`:focus-visible`), also bei Tastaturbedienung. Nachgemessen
über je 11 Sekunden: nach Tipp auf Karte, Pfeil und Punkt läuft das Banner
weiter — und mit Tastaturfokus pausiert es weiterhin korrekt.

### 2. Tippziele waren zu klein

Gemessen gegen den iOS-Richtwert von 44 × 44 px:

| Element | vorher | jetzt |
|---|---|---|
| Slider-Punkte | 9 × 9 px | 44 × 44 px |
| Slider-Pfeile | 40 × 40 | 44 × 44 |
| Menü-Schaltfläche | 40 × 40 | 44 × 44 |
| „Details“ | 70 × 30 | 70 × 43 |
| „Fall im Detail“ | 116 × 24 | 116 × 43 |
| „Direkt öffnen (PDF)“ | 222 × 27 | 222 × 45 |
| „Erstgespräch“ in der Kopfzeile | 110 × 27 | 110 × 43 |

Optisch ändert sich nichts: Die sichtbare Punktscheibe bleibt 9 px groß und
steckt jetzt in einem `::before`, die Schaltfläche darum herum ist so groß, wie
ein Daumen sie braucht. Bei den Textlinks wächst nur die Fläche, nicht die
Schrift — und ausschließlich auf Geräten ohne Maus (`@media (hover: none)`).

### 3. Bedienzeile des Sliders lag unter einer bildschirmhohen Karte

Auf dem Handy ist die Projektkarte höher als der Bildschirm — Pfeile, Zähler
und Punkte kamen erst nach dem Durchscrollen der ganzen Karte. Unter 720 px
Breite steht die Bedienzeile jetzt **über** der Karte: Beim Ankommen sieht man
sofort „01 / 03“ und kann blättern. Gewischt werden kann weiterhin überall.

### 4. Der Farb-Hover der Teamfotos war auf dem iPhone unerreichbar

Ersatz mit denselben Mitteln, die dort natürlich sind: Im Team-Karussell zeigt
**die Karte in der Mitte** ihr Foto in Farbe, die Nachbarn bleiben monochrom.
Dazu eine **Positionsanzeige** aus drei Punkten unter dem Karussell — vorher gab
es keinen Hinweis darauf, dass rechts noch zwei Personen stehen. Der Anschnitt
der nächsten Karte ist etwas größer (78 statt 82 Prozent Breite), damit das
Wischen sich anbietet.

### 5. Menü sperrte das Scrollen am Body

`document.body.style.overflow = 'hidden'` ist auf iOS ein bekanntes Ärgernis:
Safari springt dabei gern an den Seitenanfang, und die Rückkehr landet nicht
mehr da, wo man war. Die Sperre ist entfallen; das Panel ist stattdessen selbst
scrollbar und per `overscroll-behavior: contain` gekapselt. Nachgemessen:
Scrollposition 1400 vor dem Öffnen, 1400 im Menü, 1400 nach dem Schließen.

### 6. Hover-Zustände blieben nach dem Antippen hängen

Auf iOS bleibt ein `:hover`-Zustand nach einem Tipp aktiv, bis woanders getippt
wird — der CTA blieb also dunkler, der Pfeil hervorgehoben. Alle
farbwechselnden Hover-Regeln stecken jetzt in `@media (hover: hover)`; die
`:focus-visible`-Zustände für die Tastatur bleiben davon unberührt.

### 7. Notch, abgerundete Ecken und Home-Bar

`env(safe-area-inset-*)` ergänzt: Der Seitenrand nutzt jetzt
`max(var(--gutter), env(safe-area-inset-left/right))`, der Footer bekommt unten
zusätzlichen Abstand für die Home-Bar, das Vollbildmenü ebenso. Im Querformat
lag der linke Rand vorher unter der Notch.

### 8. Querformat: erzwungene Bildschirmhöhe

Bei 390 px Fensterhöhe klebte der Inhalt direkt unter der Kopfzeile, und bei
kurzem Inhalt entstanden große leere Flächen. Unter 620 px Fensterhöhe werden
Sektionen jetzt nicht mehr auf Bildschirmhöhe gezwungen und der Inhalt oben
ausgerichtet. Die Headline steht dadurch 92 px unter der Kopfzeile statt 64.

### Dazu zwei Kleinigkeiten

- **Menü-CTA war unlesbar**, wenn man aus dem Kontaktabschnitt heraus das Menü
  öffnete: Der Button zeigt auf `#kontakt` wie der Menüpunkt „Kontakt“ und bekam
  deshalb die Farbe für den aktiven Zustand — hell auf dunkel, rund 1,6:1. Der
  CTA ist jetzt aus der Aktiv-Markierung ausgenommen.
- **Antippen** erzeugt statt des grellblauen Systemblitzes einen dezenten
  Marken-Ton (`-webkit-tap-highlight-color`), und die automatische
  Schriftvergrößerung beim Drehen ist abgeschaltet
  (`-webkit-text-size-adjust: 100%`).

### Gegengeprüft, dass am Desktop nichts kaputtging

Blättern per Pfeil, Punkt und Zähler, automatischer Lauf mit Pause bei
Mouseover, Pause bei Tastaturfokus, „Details“ 1–3 auf die richtige Folie,
Farb-Hover der Teamfotos, gepinnter Signaturmoment in allen drei Phasen,
Footer am Seitenende. `html-validate` und `csstree-validator` ohne Beanstandung.

---

## Projekte auf dem iPhone: abgedichtet statt geraten

Ich konnte den Fehler nicht reproduzieren — und das ist die wichtigste Aussage
zuerst: Ich habe **exakt die `preview.html` von deiner Platte** in den
Container geholt (byte-identisch mit meinem Stand) und bei 390 × 844,
375 × 667 und 844 × 390 mit Touch-Events geprüft. Pfeile 44 × 44 px, Tipp auf
den Pfeil → 02, Tipp auf Punkt 3 → 03, keine JavaScript-Fehler. In der
Emulation funktioniert die Datei.

Da hier nur Chromium zur Verfügung steht und nicht WebKit, kann die Ursache nur
etwas sein, das Safari anders macht. Statt weiter zu raten habe ich die drei
plausiblen Ursachen abgedichtet — jede einzeln ist eine echte, dokumentierte
Safari-Eigenheit.

### 1. `overflow-x: clip` kennt Safari erst ab Version 16

Der Überhang der Projekte-Bühne (`50vw`, damit das Salbeiband über die
Inhaltsbreite läuft) wurde bisher nur über `overflow-x: clip` am `<html>`
gekappt. Versteht Safari den Wert nicht, fällt die Deklaration weg — dann ist
die ganze Seite seitlich verschiebbar. Auf dem Handy verrutscht damit alles,
und ein Slider, dessen Folien per `translateX(-100%)` gesetzt werden, wirkt
zuverlässig kaputt.

Neu wird zusätzlich an der Sektion selbst gekappt: `#cases { overflow: hidden }`
— ein Wert, den jeder Browser seit Jahren kennt. Die Sektion enthält kein
`position: sticky`, hier ist `hidden` also unbedenklich.

### 2. `matchMedia(...).addEventListener` gibt es erst ab iOS 14

Auf älteren Geräten wirft diese Zeile einen `TypeError` — und alles, was im
selben Skriptblock **danach** steht, läuft nie. Im Slider stand danach: das
Wischen, der Sprung von den Themenfeldern und der Start des Laufbanners. Die
Pfeile hätten noch funktioniert, das Wischen nicht.

Alle vier Vorkommen laufen jetzt über einen Helfer `window.fnOnMedia()`, der
das alte `addListener` als Rückfallebene nutzt und Fehler schluckt. Dazu sind
`IntersectionObserver` und die `:focus-visible`-Prüfung in `try/catch` gefasst:
Komfortfunktionen dürfen die Kernbedienung nicht mitreißen. Und wenn ein
Browser `:focus-visible` nicht kennt (Safari vor 15.4), wird nach einem
Fingertipp jetzt **nicht** mehr pausiert.

### 3. Notausgang: Projekte funktionieren jetzt auch ganz ohne JavaScript

Das deckt den Fall ab, den ich nicht ausschließen kann: Läuft auf dem Gerät
kein Skript — Lockdown-Modus, Inhaltsblocker, eine als Datei geöffnete Seite mit
eingeschränkten Rechten, ein Skriptfehler —, dann bewegt nichts den
Schienenwagen. Man sieht das erste Projekt und kommt an die anderen zwei nicht
heran. Genau das beschriebene Symptom.

Ein Einzeiler im `<head>` setzt eine Markierung, sobald JavaScript läuft. Fehlt
sie, schaltet das CSS die Schiene auf **natives horizontales Wischen mit
Einrasten** um: alle drei Projekte erreichbar, ohne eine Zeile Skript. Pfeile
und Punkte werden dann ausgeblendet (sie bräuchten ein Skript) und stattdessen
steht dort „Zum Blättern seitlich wischen →“.

Nachgemessen mit abgeschaltetem JavaScript: drei Folien im Bild erreichbar,
Klon-Folie ausgeblendet, Hinweis sichtbar — in `index.html` und `preview.html`.

### 4. Stand-Stempel in der Vorschau

Damit Versionsverwechslung ausgeschlossen ist, steht in der Fußzeile von
`preview.html` jetzt „Vorschau · Stand TT.MM.JJJJ, HH:MM“. Nur in der Vorschau,
nicht auf der echten Seite. `build-preview.py` setzt den Stempel bei jedem Lauf.

**Damit lässt sich der Fehler jetzt eindeutig einordnen:** Steht im Abschnitt
Projekte auf dem iPhone der Hinweis „Zum Blättern seitlich wischen“, läuft dort
kein JavaScript — dann ist die Ursache gefunden und das Wischen funktioniert ab
jetzt. Erscheinen weiterhin Pfeile und Zähler, läuft das Skript, und es ist
etwas anderes.
