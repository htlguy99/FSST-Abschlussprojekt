def namen():
    name1 = input("Spieler 1 gib deinen Namen ein: ")
    name2 = input("Spieler 2 gib deinen Namen ein: ")
    print(f"{name1} gegen {name2}, möge der bessere gewinnen ;) !")
    return name1, name2



def spielfeld():
    return ["~"] * 25

feld1 = spielfeld()
feld2 = spielfeld()

# Funktion zum Anzeigen eines Spielfelds
def zeige_feld(feld):
    for i in range(5):
        print(" ".join(feld[i * 5:(i + 1) * 5]))
    print()


schiffe = {
    "A": 1,
    "B": 1,
}

def schiff_setzen(feld, name):
    print(f"\n{name}, setze deine Schiffe:")
    for schiff_name, _ in schiffe.items():
        while True:
            print(f"Setze Schiff {schiff_name} (Länge 1)")
            zeige_feld(feld)
            print("Bitte x und y Koordinaten eingeben (0-4)")

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
                        print("Feld ist schon belegt!")
                else:
                    print(" Nur Zahlen von 0 bis 4!")
            except ValueError:
                print("Bitte gültige Zahlen eingeben! (0 bis 4)")

def schiessen(feld, name):
    print(f"\nSpieler {name} schießt!")
    sicht_feld = ["~" if x == "S" else x for x in feld]
    zeige_feld(sicht_feld)

    while True:
        try:
            x_input = input("x (0-4): ")
            y_input = input("y (0-4): ")
            x = int(x_input)
            y = int(y_input)
            if 0 <= x <= 4 and 0 <= y <= 4:
                pos = y * 5 + x
                if feld[pos] == "S":
                    feld[pos] = "X"
                    print("Treffer!")
                elif feld[pos] in ["X", "0"]:
                    print("Hier wurde schon geschossen.")
                else:
                    feld[pos] = "0"
                    print("Verfehlt!")
                break
            else:
                print("Nur Zahlen von 0 bis 4!")
        except ValueError:
            print("Bitte gültige Zahlen eingeben! (0 bis 4)")

# Überprüfen, ob noch Schiffe da sind
def verloren(feld):
    return "S" not in feld

# Spielstart
name1, name2 = namen()
print("Das Spiel beginnt!")
schiff_setzen(feld1, name1)
schiff_setzen(feld2, name2)

# Spielschleife
spieler = 1
while True:
    if spieler == 1:
        schiessen(feld2, name1)
        if verloren(feld2):
            print(f"{name1} gewinnt!")
            break
        spieler = 2
    else:
        schiessen(feld1, name2)
        if verloren(feld1):
            print("f {name2} gewinnt!")
            break
        spieler = 1
