"""LU07.A06 - Loesung: funktionaler Kern und duenne Schale.

Der Kern (mit_einlagerung, mit_entnahme) ist pure: gleiche Eingabe, gleiches
Ergebnis, keine Mutation der Argumente, keine Ausgabe.
Zustand und Ausgabe leben ausschliesslich in der Schale (lauf).
"""


def mit_einlagerung(bestand, artikel, menge):
    """
    Liefert einen neuen Bestand mit der zusaetzlichen Menge.

    :param bestand: der bisherige Bestand als dict
    :param artikel: Bezeichnung des Artikels
    :param menge: einzulagernde Menge
    :return: der neue Bestand als dict
    """
    return {**bestand, artikel: bestand.get(artikel, 0) + menge}


def mit_entnahme(bestand, artikel, menge):
    """
    Liefert den neuen Bestand und ob die Entnahme moeglich war.

    :param bestand: der bisherige Bestand als dict
    :param artikel: Bezeichnung des Artikels
    :param menge: gewuenschte Menge
    :return: Tuple aus neuem Bestand und Erfolgskennzeichen
    """
    if bestand.get(artikel, 0) < menge:
        return bestand, False
    return {**bestand, artikel: bestand[artikel] - menge}, True


def lauf():
    """
    Fuehrt den Beispielablauf aus und gibt Bestand und Protokoll zurueck.

    Diese Funktion ist die Schale: hier leben Zustand und Ausgabe.

    :return: Tuple aus Bestand und Protokoll
    """
    bestand = {}
    protokoll = []

    bestand = mit_einlagerung(bestand, 'maus', 5)
    protokoll.append('+5 maus')
    menge = bestand['maus']
    print(f'maus: {menge}')

    bestand = mit_einlagerung(bestand, 'maus', 3)
    protokoll.append('+3 maus')
    menge = bestand['maus']
    print(f'maus: {menge}')

    bestand, erfolgreich = mit_entnahme(bestand, 'maus', 2)
    if erfolgreich:
        protokoll.append('-2 maus')

    bestand, erfolgreich = mit_entnahme(bestand, 'maus', 99)
    if not erfolgreich:
        print('zu wenig Bestand')

    return bestand, protokoll


if __name__ == '__main__':
    print(lauf())
