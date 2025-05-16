def namen():
    name1 = input("Spieler 1 gib deinen Namen ein: ")
    name2 = input("Spieler 2 gib deinen Namen ein: ")
    print(f"{name1} gegen {name2}, möge der bessere gewinnen ;) !")
    return name1, name2

def spielfeld():
    return ["~"] * 100

feld1 = spielfeld()
feld2 = spielfeld()

# Funktion zum Anzeigen eines Spielfelds
def zeige_feld(feld):
    print("X 0 1 2 3 4 5 6 7 8 9")
    for i in range(10):
        print(f"{i} ", end="")
        print(" ".join(feld[i * 10:(i + 1) * 10]))
    print()

schifflänge = {
    "Schlachtschiff": 5,
    "Kreuzer": 4,
    "Zerstörer": 3,
    "U-Boot": 2
}

def will_weiterspielen():
    antwort = input("Möchtet ihr nochmal spielen? (ja/nein): ")
    return antwort.lower() == "ja"

def schiff_setzen(feld, name):
    print(f"\n{name}, setze deine Schiffe:")
    for schiff_name, laenge in schifflänge.items():
        while True:
            print(f"Setze {schiff_name} (Länge {laenge})")
            zeige_feld(feld)
            
            # Startposition
            while True:
                try:
                    x = int(input("Start x (0-9): "))
                    y = int(input("Start y (0-9): "))
                    if 0 <= x <= 9 and 0 <= y <= 9:
                        break
                    print("Koordinaten müssen zwischen 0 und 9 liegen!")
                except ValueError:
                    print("Bitte gültige Zahlen eingeben!")
            
            # Richtung
            richtung = input("Richtung (h für horizontal, v für vertikal): ").lower()
            if richtung not in ['h', 'v']:
                print("Ungültige Richtung! Bitte 'h' oder 'v' eingeben.")
                continue
            
            # Prüfen ob Schiff platziert werden kann
            gueltig = True
            felder = []
            
            for i in range(laenge):
                if richtung == 'h':
                    if x + i >= 10:
                        gueltig = False
                        break
                    pos = y * 10 + (x + i)
                else:  # vertikal
                    if y + i >= 10:
                        gueltig = False
                        break
                    pos = (y + i) * 10 + x
                
                if pos >= len(feld) or feld[pos] != "~":
                    gueltig = False
                    break
                felder.append(pos)
            
            if gueltig:
                # Schiff setzen
                for pos in felder:
                    feld[pos] = "S"
                zeige_feld(feld)
                break
            else:
                print("Ungültige Position! Schiff würde über den Rand gehen oder überlappt mit einem anderen Schiff.")

def schiessen(feld, name):
    print(f"\nSpieler {name} schießt!")
    sicht_feld = ["~" if x == "S" else x for x in feld]
    zeige_feld(sicht_feld)

    while True:
        try:
            x_input = input("x (0-9): ")
            y_input = input("y (0-9): ")
            x = int(x_input)
            y = int(y_input)
            if 0 <= x <= 9 and 0 <= y <= 9:
                pos = y * 10 + x
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
                print("Nur Zahlen von 0 bis 9!")
        except ValueError:
            print("Bitte gültige Zahlen eingeben! (0 bis 9)")

def verloren(feld):
    return "S" not in feld

# Hauptspielschleife
while True:
    # Spielstart
    feld1 = spielfeld()
    feld2 = spielfeld()
    name1, name2 = namen()
    print("Das Spiel beginnt!")
    
    schiff_setzen(feld1, name1)
    schiff_setzen(feld2, name2)

    # Spielrunden
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
                print(f"{name2} gewinnt!")
                break
            spieler = 1

    # Weiterspielen?
    if not will_weiterspielen():
        print("Danke fürs Spielen!")
        break
