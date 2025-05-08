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

# Schiffgrößen (alle 1 Feld)
schiffe = {
    "A": 1,
    "B": 1,
}

# Schiffe setzen für einen Spieler
def schiff_setzen(feld, spieler_nummer):
    print(f"\nSpieler {spieler_nummer}, setze deine Schiffe:")
    for name, _ in schiffe.items():
        while True:
            print(f"Setze Schiff {name} (1 Feld)")

            try:
                x = int(input("x (0-4): "))
                y = int(input("y (0-4): "))
                if 0 <= x <= 4 and 0 <= y <= 4:
                    pos = y * 5 + x
                    if feld[pos] == "~":
                        feld[pos] = "S"
                        zeige_feld(feld)
                        break
                    else:
                        print("❗ Feld ist schon belegt!")
                else:
                    print("❗ Nur Zahlen von 0 bis 4!")
            except ValueError:
                print("❗ Bitte gültige Zahlen eingeben!")

# Schuss-Funktion für einen Spieler
def schiessen(feld, spieler_nummer):
    print(f"\nSpieler {spieler_nummer} schießt!")
    sicht_feld = ["~" if x == "S" else x for x in feld]
    zeige_feld(sicht_feld)

    while True:
        try:
            x = int(input("x (0–4): "))
            y = int(input("y (0-4): "))
            if 0 <= x <= 4 and 0 <= y <= 4:
                pos = y * 5 + x
                if feld[pos] == "S":
                    feld[pos] = "X"
                    print("🎯 Treffer!")
                elif feld[pos] in ["X", "0"]:
                    print("🔁 Hier wurde schon geschossen.")
                else:
                    feld[pos] = "0"
                    print("💨 Verfehlt!")
                break
            else:
                print("❗ Nur Zahlen von 0 bis 4!")
        except ValueError:
            print("❗ Bitte gültige Zahlen eingeben!")

# Überprüfen, ob noch Schiffe da sind
def verloren(feld):
    return "S" not in feld

# Spielstart
schiff_setzen(feld1, 1)
schiff_setzen(feld2, 2)

# Spielschleife
spieler = 1
while True:
    if spieler == 1:
        schiessen(feld2, 1)
        if verloren(feld2):
            print("🏆 Spieler 1 gewinnt!")
            break
        spieler = 2
    else:
        schiessen(feld1, 2)
        if verloren(feld1):
            print("🏆 Spieler 2 gewinnt!")
            break
        spieler = 1
