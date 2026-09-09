"""LU07.A06 - Unpure wird pure.

Eine kleine Lagerverwaltung mit globalem Zustand. Die Funktionen rechnen,
veraendern den Zustand und geben nebenbei etwas aus - alles gleichzeitig.

Ihre Aufgabe: einen pure funktionalen Kern bauen und den Zustand in eine
duenne Schale verlagern. Die Vorgaben stehen im README.
"""

lager = {}
protokoll = []


def einlagern(artikel, menge):
    """
    Legt Ware ins Lager und protokolliert den Vorgang.

    :param artikel: Bezeichnung des Artikels
    :param menge: eingelagerte Menge
    :return: None
    """
    global lager
    if artikel in lager:
        lager[artikel] += menge
    else:
        lager[artikel] = menge
    protokoll.append(f'+{menge} {artikel}')
    print(f'{artikel}: {lager[artikel]}')


def entnehmen(artikel, menge):
    """
    Entnimmt Ware aus dem Lager, sofern genug vorhanden ist.

    :param artikel: Bezeichnung des Artikels
    :param menge: gewuenschte Menge
    :return: True bei Erfolg, sonst False
    """
    global lager
    if lager.get(artikel, 0) < menge:
        print('zu wenig Bestand')
        return False
    lager[artikel] -= menge
    protokoll.append(f'-{menge} {artikel}')
    return True


def mit_einlagerung(bestand, artikel, menge):
    """
    TODO: Liefert einen NEUEN Bestand mit der zusaetzlichen Menge.

    Diese Funktion darf `bestand` nicht veraendern und nichts ausgeben.

    :param bestand: der bisherige Bestand als dict
    :param artikel: Bezeichnung des Artikels
    :param menge: einzulagernde Menge
    :return: der neue Bestand als dict
    """


def mit_entnahme(bestand, artikel, menge):
    """
    TODO: Liefert (neuer Bestand, erfolgreich?) als Tuple.

    Bei zu wenig Bestand bleibt der Bestand unveraendert und der zweite
    Wert ist False. Diese Funktion darf nichts ausgeben.

    :param bestand: der bisherige Bestand als dict
    :param artikel: Bezeichnung des Artikels
    :param menge: gewuenschte Menge
    :return: Tuple aus neuem Bestand und Erfolgskennzeichen
    """


def lauf():
    """
    Fuehrt den Beispielablauf aus und gibt Bestand und Protokoll zurueck.

    :return: Tuple aus Bestand und Protokoll
    """
    einlagern('maus', 5)
    einlagern('maus', 3)
    entnehmen('maus', 2)
    entnehmen('maus', 99)
    return lager, protokoll


if __name__ == '__main__':
    print(lauf())
