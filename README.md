# LU07.A06 - Unpure wird pure

Modul 323, LU07 Refactoring · Kompetenzfeld **D1I**

`main.py` enthält eine kleine Lagerverwaltung mit globalem Zustand. Die Funktionen
rechnen, verändern den Zustand und geben nebenbei etwas aus — alles gleichzeitig.
Ihre Aufgabe ist es, daraus einen **funktionalen Kern** und eine **dünne Schale**
zu machen.

## Ausgangslage

Führen Sie zuerst `pytest` aus. Sieben Tests sind rot. Das ist Absicht: Die Tests
sind hier die Spezifikation. Zwei davon lohnen sich genauer anzuschauen:

* `test_lauf_ist_wiederholbar` — zwei Durchläufe liefern verschiedene Ergebnisse,
  weil der globale Zustand zwischen den Aufrufen hängen bleibt.
* `test_lauf_ausgabe` — schlägt fehl, sobald vorher ein anderer Test gelaufen ist.
  Genau das meint «Tests hängen voneinander ab».

## Zu implementieren

```python
mit_einlagerung(bestand, artikel, menge) -> dict
mit_entnahme(bestand, artikel, menge)    -> (dict, bool)
```

Beide Funktionen sind **pure**:

* Sie verändern `bestand` nicht, sondern geben einen neuen zurück.
* Sie geben nichts auf der Konsole aus.
* Derselbe Aufruf liefert immer dasselbe Ergebnis.

`lauf()` ist die Schale. Dort — und nur dort — leben Zustand, Protokoll und
`print`. Am Schluss existieren die globalen Variablen `lager` und `protokoll`
nicht mehr; `einlagern` und `entnehmen` in ihrer alten Form auch nicht.

## Regeln

* `main_test.py` wird **nicht** verändert.
* Die Rückgabewerte und die Ausgabe von `lauf()` bleiben exakt gleich.
* Kein `global` im fertigen Code.

## Bewertung

| Teil | Punkte |
|---|---|
| Tests (`main_test.py`) | 14 |
| pylint (`main.py`) | 5 |

## Lokal prüfen

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest
python _run_pylint.py
```

## Leitfragen für die Reflexion

* Wie gibt eine Funktion gleichzeitig den neuen Bestand und «hat geklappt» zurück?
* Gehört das Protokoll in den Kern oder in die Schale? Warum?
* Was wird an der neuen Fassung einfacher zu testen als vorher?
