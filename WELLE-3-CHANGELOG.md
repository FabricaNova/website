# Welle 3 — umgesetzte Änderungen

Grundlage: Design-Audit vom 13.08.2026, Maßnahmenblock „Welle 3 —
Erinnerbarkeit und Vertrieb“. Der Ordner heißt jetzt
`fabrica-nova-site-v2` (vorher `fabrica-nova-site-welle1`), weil er inzwischen
alle drei Wellen enthält. Der Originalordner `fabrica-nova-site` ist unverändert.

Vorgeschichte: `WELLE-1-CHANGELOG.md`, `WELLE-2-CHANGELOG.md`.
`preview.html` wurde nach jeder Änderung mit `python3 build-preview.py` neu
erzeugt und liegt aktuell bei 531 KB.

## 1. Der Signaturmoment — das eine Bild, das man weitererzählt

Die Sektion „Vorgehen“ ist jetzt eine **gepinnte Sequenz**: die Fläche bleibt
stehen, während die drei Projektphasen und der Facettenaufbau in drei Schritten
erscheinen.

- **Diagnose** → die Kontur einer Facette (den Prozess sehen)
- **Zielbild** → eine halbtransparente Fläche legt sich darüber
- **Umsetzung** → der volle Petrol-Ton mit Goldkante (die Wirkung)

Drei Phasen, drei Plattenlagen, ein Motiv — dasselbe, das in Logo, Buttons,
Fotorahmen und Karten steckt. Die Bewegung ist bewusst ruhig und dauert genau so
lange, wie man zum Lesen der drei Zeilen braucht. Keine Parallaxe, kein Zoom,
kein Zähler.

Die Phasen sind neu benannt und mit je einer Zeile belegt (vorher standen
„Diagnose, Zielbild und Umsetzung“ nur im Fließtext) — damit sind sie zitierfähig
und decken sich mit der Struktur der Projektkarten
(Situation → Hebel → Effekt).

**Robust gebaut, nicht als Effekt:**

- Ohne JavaScript sind alle drei Phasen und alle drei Facetten sichtbar.
  Der Inhalt hängt nie an der Animation (geprüft mit deaktiviertem JavaScript).
- Bei `prefers-reduced-motion: reduce` wird nicht sequenziert.
- Unter 861 px Breite oder 620 px Höhe wird nicht gepinnt: die Sektion ist dann
  eine normale, vollständig sichtbare Fläche. Auf dem Handy stehen alle drei
  Phasen untereinander.
- Die Sektion ist absichtlich **kein** Snap-Ziel, damit Snap-Scrolling und
  Pinning sich nicht in die Quere kommen. Der Menüpunkt wird trotzdem
  mitmarkiert (der Observer beobachtet jetzt `section[id]`).

**Dabei einen echten Fehler gefunden und behoben:** `body { overflow-x: hidden }`
aus Welle 1 machte den Body zum Scroll-Container (`overflow-y` wird dabei
implizit zu `auto`) und setzte damit **jedes `position: sticky`** auf der Seite
außer Kraft — der Signaturmoment blieb zunächst nicht stehen. Das Abschneiden
übernimmt jetzt `overflow-x: clip` auf `<html>`; `clip` erzeugt keinen
Scroll-Container. Kein horizontaler Scrollbalken in allen sechs geprüften
Fenstergrößen.

## 2. Projekt-Detailseiten

Neu: `projekt-1.html`, `projekt-2.html`, `projekt-3.html`.

- Jede Karte im Slider hat einen Link **„Fall im Detail“**.
- Auf der Detailseite steht der **vollständige Originaltext**
  (Herausforderung, Ansatz, Fazit, umgesetzte Hebel) — genau der, der vor
  Welle 2 im Slider stand. Nichts ergänzt, nichts erfunden: der Slider zeigt
  jetzt die kurze Fassung, die Detailseite die lange.
- Kennzahl in der Kopfzeile mit der Akzentfarbe des jeweiligen Projekts,
  darunter Vor-/Zurück-Navigation zwischen den Fällen und ein Abschluss-CTA
  („Klingt das nach Ihrem Betrieb?“).
- Eigene Meta-Angaben, Open Graph und `canonical` je Seite. Die Seiten sind
  indexierbar (im Gegensatz zu Impressum und Datenschutz) — sie sind der
  inhaltliche Grund, warum jemand die Seite über Google findet.
- Der Link in der geklonten Slider-Folie steht auf `tabindex="-1"`, damit er
  nicht doppelt in der Tab-Reihenfolge auftaucht.

## 3. Kundenstimmen — als Struktur, nicht als Text

Neue Sektion `#stimmen` mit drei Zitatkarten, direkt vor dem Kontakt.

> **Die drei Zitate sind leere Platzhalter und sichtbar als solche markiert**
> (gestrichelter Rahmen, roter Hinweis „Platzhalter — echtes Zitat einsetzen“).
> Erfundene Kundenstimmen wären ein Vertrauensbruch, und genau bei dieser
> Zielgruppe der schnellste Weg, Glaubwürdigkeit zu verlieren. Hier gehören
> echte, freigegebene Sätze hinein — anonymisiert ist völlig in Ordnung
> („Geschäftsführer, Schreinerei, ~50 Mitarbeitende“).

In jedem Platzhalter steht, was an dieser Stelle am besten wirkt: ein Satz über
die Veränderung im Alltag, einer über die Zusammenarbeit, einer mit einer Zahl.
Reicht es nur für ein Zitat: die anderen Karten löschen, das Raster trägt auch
eine oder zwei. Liegt zum Livegang keines vor: Sektion entfernen — sie steht
nicht im Menü, es entstehen keine toten Links.

**Regionale Verortung** als Schlusszeile der Sektion, mit Platzhalter für das
Einsatzgebiet. Bei KMU zählt Nähe mehr als Prestige.

## 4. Inhaltsangebot: der Zettelwirtschaft-Check

Im Kontaktabschnitt neu: ein niedrigschwelliger Einstieg für alle, die noch
nicht sprechen wollen — **zwölf Fragen zum Selbstcheck**, als zweiseitiges PDF
in der Hausschrift und Hausfarbe.

- **Datei:** `assets/Fabrica-Nova-Zettelwirtschaft-Check.pdf` (2 Seiten, 37 KB)
- **Inhalt:** vier Blöcke — Vom Auftrag zur Baustelle, Zeit und Material,
  Abrechnung, Steuerung — je drei Fragen mit Ja/Teils/Nein-Kästchen, dazu eine
  Auswertung in drei Punktebändern.
- **Zwei Wege:** „Per E-Mail anfordern“ (vorbereitete Mail mit Betreff und
  Textgerüst) und direkter Download. Absichtlich **kein** hartes Gate: ein
  Formular bräuchte Backend, Einwilligung und einen zusätzlichen Abschnitt in
  der Datenschutzerklärung — und schreckt bei dieser Zielgruppe mehr Leute ab,
  als es Adressen bringt. Der Versand nach Anfrage passiert von Hand, was zu
  einer Boutique passt.
- **Quelle zum Weiterbearbeiten:** `_quellen/zettelwirtschaft-check.src.html`.
  Im Browser öffnen → Drucken → „Als PDF speichern“, A4, ohne Ränder,
  Hintergrundgrafiken an. Die Datei ist auf `noindex` gesetzt; der Ordner
  `_quellen/` gehört nicht ins Deployment.

> **Inhaltlich ein Entwurf zur Freigabe.** Die zwölf Fragen stammen aus den
> Mustern, die in euren eigenen Projekten dokumentiert sind (verlorene Zettel,
> Aufmaß, Abrechnung, Nachkalkulation) — aber es ist euer fachliches Wort nach
> außen. Bitte einmal durchgehen und die Tonalität abgleichen. Der Fußzeilen-
> Hinweis „Entwurf zur Freigabe“ auf Seite 2 muss vor dem Versand raus.

## 5. Englische Variante — bewusst nicht gebaut

Die Empfehlung aus dem Audit lautete „nur, wenn international akquiriert wird“.
Die Zielgruppe sind deutsche KMU in Industrie und Handwerk, die Fallstudien und
die Tonalität sind auf diesen Markt geschrieben. Eine zweite Sprachfassung
verdoppelt den Pflegeaufwand und bringt hier keinen Interessenten mehr. Falls
international akquiriert wird, ist der richtige Weg keine gespiegelte Website,
sondern eine englische Seite für genau diesen Zweck.

## Prüfung

- `html-validate` ohne Beanstandung für `index.html`, `preview.html`,
  `projekt-1/2/3.html`, `impressum.html`, `datenschutz.html`;
  `csstree-validator` ohne Beanstandung für `styles.css`.
- Sechs Fenstergrößen geprüft (1680 × 950, 1440 × 820, 1280 × 600, 834 × 1112,
  844 × 390, 390 × 844): kein horizontaler Scrollbalken, Kopfzeile passt überall
  in eine Zeile, keine fehlenden Bilder, keine JavaScript-Fehler.
- Signaturmoment in allen vier Zuständen durchgemessen: gepinnt (Fläche bleibt
  bei `top: 0` stehen), Phasenwechsel 1 → 2 → 3 an den vorgesehenen
  Scrollpunkten, ohne JavaScript alles sichtbar, bei reduzierter Bewegung nicht
  sequenziert, auf Tablet und Handy nicht gepinnt.
- Detailseiten und PDF über HTTP abgerufen (PDF: Status 200,
  `application/pdf`, 2 Seiten).
- `preview.html` zusätzlich über `file://` geprüft: Schriften geladen, Bilder
  vorhanden, Sequenz aktiv. Die Links auf Detailseiten und PDF sind relativ —
  sie funktionieren, solange `preview.html` im Projektordner liegt, nicht als
  einzeln verschickte Datei.

## Was jetzt noch offen ist — und nur von euch kommen kann

| Was | Wo es fehlt |
|---|---|
| Telefonnummer | Kontaktsektion, Footer, Impressum, Datenschutz, Check-PDF |
| Standort und Einsatzgebiet | Kontaktsektion, Stimmen-Schlusszeile |
| Firma, Rechtsform, Registerdaten, USt-ID, Vertretungsberechtigte | Impressum |
| Hosting-Anbieter, Aufsichtsbehörde, Löschfristen | Datenschutz |
| Echte Domain | `canonical` und `og:url` in vier Dateien |
| Zwei bis drei freigegebene Kundenzitate | Sektion „Stimmen“ |
| Einheitliches Foto-Shooting | Team (Duotone ist die Übergangslösung) |
| Freigabe der Headline „Weniger Zettel. Mehr Marge.“ | Startbildschirm, OG-Angaben, Check-PDF |
| Freigabe des Check-Inhalts | `assets/Fabrica-Nova-Zettelwirtschaft-Check.pdf` |

Alle offenen Textstellen sind im Quelltext als `TODO`-Kommentar und in der
Anzeige rot-kursiv als <span style="color:#96305C">*[…]*</span> markiert.
Eine anwaltliche Prüfung der Rechtsseiten vor Veröffentlichung ist zu empfehlen
— ich bin kein Anwalt, das ist keine Rechtsberatung.
