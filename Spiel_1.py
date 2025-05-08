# Spielfeld-Erstellung
def spielfeld():
    return ["~"] * 25

# Spielfelder für beide Spieler
feld1 = spielfeld()
feld2 = spielfeld()

# Funktion zum Anzeigen eines Spielfelds
def zeige_feld(feld):
    for i in range(5):
        print(" ".join(feld[i * 5:(i + 1) * 5]))
    print()


# Schiffgrößen (kann erweitert werden)
schiffe = {
    "A": 1,
    "B": 1,
}

# Schiffe setzen für einen Spieler
def schiff_setzen(feld, spieler_nummer):
    print(f"\nSpieler {spieler_nummer}, setze deine Schiffe:")

    for name, laenge in schiffe.items():
        while True:
            print(f"Setze Schiff {name} mit Länge {laenge}")

            # Eingabeprüfung direkt im Code
            while True:
                try:
                    x1 = int(input("x1 (0-4): "))
                    if 0 <= x1 <= 4:
                        break
                    else:
                        print("Nur Zahlen von 0 bis 4!")
                except ValueError:
                    print("Bitte eine Zahl eingeben!")

            while True:
                try:
                    y1 = int(input("y1 (0-4): "))
                    if 0 <= y1 <= 4:
                        break
                    else:
                        print("Nur Zahlen von 0 bis 4!")
                except ValueError:
                    print("Bitte eine Zahl eingeben!")

            while True:
                try:
                    x2 = int(input("x2 (0-4): "))
                    if 0 <= x2 <= 4:
                        break
                    else:
                        print("Nur Zahlen von 0 bis 4!")
                except ValueError:
                    print("Bitte eine Zahl eingeben!")

            while True:
                try:
                    y2 = int(input("y2 (0-4): "))
                    if 0 <= y2 <= 4:
                        break
                    else:
                        print("Nur Zahlen von 0 bis 4!")
                except ValueError:
                    print("Bitte eine Zahl eingeben!")

            pos1 = y1 * 5 + x1
            pos2 = y2 * 5 + x2

            if feld[pos1] == "~" and feld[pos2] == "~":
                feld[pos1] = "S"
                feld[pos2] = "S"
                zeige_feld(feld)
                break
            else:
                print("Eine Position ist schon belegt. Versuch's nochmal.")

# Schuss-Funktion für einen Spieler
def schiessen(feld, spieler_nummer):
    print(f"\nSpieler {spieler_nummer} schießt!")

    sicht_feld = ["~" if x == "S" else x for x in feld]
    zeige_feld(sicht_feld)

    # Eingabe x
    while True:
        try:
            x = int(input("x (0–4): "))
            if 0 <= x <= 4:
                break
            else:
                print("Nur Zahlen von 0 bis 4!")
        except ValueError:
            print("Bitte eine Zahl eingeben!")

    # Eingabe y
    while True:
        try:
            y = int(input("y (0-4): "))
            if 0 <= y <= 4:
                break
            else:
                print("Nur Zahlen von 0 bis 4!")
        except ValueError:
            print("Bitte eine Zahl eingeben!")

    pos = y * 5 + x

    if feld[pos] == "S":
        feld[pos] = "X"
        print("Treffer!")
    elif feld[pos] in ["X", "0"]:
        print("Hier wurde schon geschossen.")
    else:
        feld[pos] = "0"
        print("Verfehlt!")


# Überprüft, ob noch Schiffe vorhanden sind
def verloren(feld):
    return "S" not in feld


# Spielstart: Schiffe setzen
 
schiff_setzen(feld1, 1)
schiff_setzen(feld2, 2)

# Spielschleife
spieler = 1
while True:
    if spieler == 1:
        schiessen(feld2, 1)
        if verloren(feld2):
            print("Spieler 1 gewinnt!")
            break
        spieler = 2
    else:
        schiessen(feld1, 2)
        if verloren(feld1):
            print("Spieler 2 gewinnt!")
            break
        spieler = 1
