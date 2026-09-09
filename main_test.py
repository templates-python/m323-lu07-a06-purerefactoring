"""LU07.A06 - Tests fuer den funktionalen Kern und die Schale.

Diese Tests sind im Startzustand teilweise ROT. Sie sind die Spezifikation:
Wenn alle gruen sind, ist der Kern pure und der Zustand liegt in der Schale.

Aendern Sie diese Datei nicht.
"""

import copy

import main


def test_lauf_ergebnis():
    """Der Beispielablauf liefert Bestand und Protokoll wie bisher."""
    assert main.lauf() == ({'maus': 6}, ['+5 maus', '+3 maus', '-2 maus'])


def test_lauf_ist_wiederholbar():
    """Zwei Ablaeufe hintereinander liefern dasselbe - kein Zustand bleibt haengen."""
    erster = copy.deepcopy(main.lauf())
    zweiter = copy.deepcopy(main.lauf())
    assert erster == zweiter


def test_lauf_ausgabe(capsys):
    """Die Ausgabe des Ablaufs bleibt unveraendert."""
    main.lauf()
    captured = capsys.readouterr()
    assert captured.out == 'maus: 5\nmaus: 8\nzu wenig Bestand\n'


def test_einlagerung_neuer_artikel():
    """Ein noch nicht vorhandener Artikel wird angelegt."""
    assert main.mit_einlagerung({}, 'maus', 5) == {'maus': 5}


def test_einlagerung_bestehender_artikel():
    """Eine vorhandene Menge wird erhoeht."""
    assert main.mit_einlagerung({'maus': 5}, 'maus', 3) == {'maus': 8}


def test_einlagerung_ohne_seiteneffekt():
    """Der uebergebene Bestand wird nicht veraendert."""
    original = {'maus': 5}
    main.mit_einlagerung(original, 'maus', 3)
    assert original == {'maus': 5}


def test_entnahme_erfolgreich():
    """Bei genug Bestand wird entnommen und True gemeldet."""
    assert main.mit_entnahme({'maus': 5}, 'maus', 2) == ({'maus': 3}, True)


def test_entnahme_zu_wenig_bestand():
    """Bei zu wenig Bestand bleibt alles gleich und False wird gemeldet."""
    assert main.mit_entnahme({'maus': 1}, 'maus', 99) == ({'maus': 1}, False)


def test_kern_ist_deterministisch():
    """Derselbe Aufruf liefert zweimal dasselbe Ergebnis."""
    bestand = {'maus': 5}
    assert main.mit_entnahme(bestand, 'maus', 2) == main.mit_entnahme(bestand, 'maus', 2)


def test_kern_gibt_nichts_aus(capsys):
    """Der funktionale Kern schreibt nicht auf die Konsole."""
    main.mit_einlagerung({}, 'maus', 5)
    main.mit_entnahme({'maus': 1}, 'maus', 99)
    assert capsys.readouterr().out == ''


def test_kein_globaler_zustand():
    """Nach dem Refactoring gibt es keine globalen Variablen lager und protokoll mehr."""
    assert not hasattr(main, 'lager')
    assert not hasattr(main, 'protokoll')
