# LU07.A06 - Lösungshinweise

## Was der Umbau leistet

| Vorher | Nachher |
|---|---|
| `lager` und `protokoll` als Modulvariablen | Zustand als lokale Variable in `lauf()` |
| `einlagern` rechnet, mutiert und druckt | `mit_einlagerung` rechnet nur |
| Rückgabe `True`/`False`, Bestand als Nebenwirkung | Rückgabe `(bestand, erfolgreich)` |
| Test braucht Zurücksetzen der Globals | Test übergibt seinen eigenen Bestand |

## Die drei Tests, die den Unterschied belegen

* `test_einlagerung_ohne_seiteneffekt` — der übergebene Bestand bleibt unverändert.
  Das ist die Definition von «mutiert nicht».
* `test_lauf_ist_wiederholbar` — im Startzustand rot, weil die Globals zwischen
  zwei Durchläufen weiterleben.
* `test_kein_globaler_zustand` — prüft, dass `lager` und `protokoll` als
  Modulvariablen verschwunden sind.

## Häufige Fehler

**Bestand kopieren statt neu bauen.** `bestand.copy()` mit anschliessender
Mutation funktioniert zwar, ist aber kein funktionaler Stil. `{**bestand, artikel: ...}`
drückt in einer Zeile aus, was gemeint ist.

**Protokoll in den Kern verschoben.** Wer `protokoll.append(...)` in
`mit_einlagerung` lässt, hat den globalen Zustand nur umbenannt. Das Protokoll ist
eine Aufzeichnung dessen, was die Schale tut.

**`erfolgreich` ignoriert.** Wer `bestand, _ = mit_entnahme(...)` schreibt und die
Meldung weglässt, verändert die Ausgabe — `test_lauf_ausgabe` fängt das ab.

## Bezug zum Portfolio

Der Umbau ist ein vorzeigbarer Beleg für **D1I** und gleichzeitig für **A1I**
(immutable values) und **A1B** (pure function gegen Prozedur). In Flask ist dieses
Muster die Regel: Route als Schale, Berechnung als pure Funktion, die ohne
laufenden Server getestet werden kann.
