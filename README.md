# Python-Template (Classroom 50)

Vorlage für die Programmier-Aufgaben. Bewertet wird mit
[pygrader50](https://github.com/BZZ-Commons/pygrader50) über Classroom 50.

## Inhalt

| Datei | Zweck |
|---|---|
| `main.py` | Startcode |
| `main_test.py` | pytest-Fälle |
| `requirements.txt` | Pins für die lokale Entwicklung |
| `.python-version` | Python-Version (muss zu `runtime.python` in `assignments.json` passen) |
| `.gitignore` | schliesst PyCharm-Einstellungen und `.venv` aus |
| `.github/autograding/` | Bewertungs-Konfiguration, siehe unten |
| `.github/workflows/copyissues.yml` | kopiert Issues aus einem Quell-Repo, manueller Start |
| `_run_pylint.py` | lässt die Lernenden pylint lokal mit derselben Konfiguration laufen |

## Bewertung

Classroom 50 legt beim Annehmen der Aufgabe `.classroom50.yaml` und
`.github/workflows/autograde.yaml` im Studi-Repo an. Beide gehören **nicht** ins
Template. Bei jedem Push startet der Runner den Klassen-Default-Autograder aus
dem Config-Repo, der `pygrader50` installiert und im Checkout ausführt.

pygrader50 liest drei Dateien aus `.github/autograding/`:

### `unittests.json`

Ein Eintrag pro pytest-Fall. `function` ist der Name der Testfunktion in
`main_test.py`, `points` sind ganze Zahlen.

```json
[
  {
    "name": "test",
    "function": "test",
    "timeout": 10,
    "points": 1
  }
]
```

### `lint.json`

```json
{
  "files": ["main.py"],
  "ignore": [],
  "max": 5
}
```

`files` bestimmt, was gelintet wird; ist die Liste leer, sind es alle `*.py` im
Wurzelverzeichnis ausser den `ignore`-Mustern. `max` sind die Lint-Punkte:
vergeben wird `pylint-Note / 10 * max`, nach unten auf 0 begrenzt.

### `pylintrc`

pylint-Konfiguration. Die `evaluation`-Formel darin entscheidet, wie stark
Meldungen die Note drücken.

## Lokal prüfen

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest                           # dieselben Testfälle wie im Bewertungslauf
python _run_pylint.py            # pylint mit lint.json und pylintrc
```

`_run_pylint.py` liest `.github/autograding/lint.json` und lintet die dort
genannten Dateien mit `.github/autograding/pylintrc` — dieselbe Auswahl und
dieselbe Konfiguration wie die Bewertung. Es rechnet die pylint-Note aber nicht
in Punkte um; das macht erst pygrader50 mit `Note / 10 * max`.

## Neue Aufgabe ableiten

1. Repo aus diesem Template erzeugen, in der Organisation `templates-python`.
2. `main.py`, `main_test.py` und `README.md` durch die Aufgabe ersetzen.
3. `unittests.json` auf die echten Testfunktionen und Punkte setzen.
4. `lint.json` → `files` auf die zu lintenden Dateien, `max` auf die Lint-Punkte.
5. Zusätzliche Pakete in `requirements.txt` ergänzen — nicht die, welche die
   Lernenden selbst eintragen sollen (z. B. Flask).
6. Aufgabe in `assignments.json` des Config-Repos eintragen.

`requirements.txt` wird im Bewertungslauf **nicht** installiert; pygrader50
bringt pytest und pylint in gepinnter Version selbst mit. Die Datei ist für die
lokale Entwicklung da, deshalb müssen die Pins zur Engine passen.
