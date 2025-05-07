import random

GROESSE = 5
flotte = [3, 2]

# Spielfelder initialisieren
def neues_meer():
    return [[0 for _ in range(GROESSE)] for _ in range(GROESSE)]

def zeige_meer(meer, verdeckt=False):
    symbole = ["~", "S", "°", "T"]  # Wasser, Schiff, verfehlt, getroffen
    for y in reversed(range(GROESSE)):
        zeile = ""
        for x in range(GROESSE):
            feld = meer[x][y]
            if verdeckt and feld == 1:
                zeile += symbole[0] + " "  # Schiff verstecken
            else:
                zeile += symbole[feld] + " "
        print(zeile)

def setze_schiff(meer, x, y, richtung, laenge):
    x -= 1
    y -= 1
    if richtung:  # waagerecht
        if x + laenge > GROESSE or any(meer[x+i][y] != 0 for i in range(laenge)):
            return False
        for i in range(laenge):
            meer[x+i][y] = 1
    else:  # senkrecht (nach oben)
        if y + laenge > GROESSE or any(meer[x][y+i] != 0 for i in range(laenge)):
            return False
        for i in range(laenge):
            meer[x][y+i] = 1
    return True

def schiessen(meer, x, y):
    x -= 1
    y -= 1
    if meer[x][y] == 1:
        meer[x][y] = 3
        print("Treffer!")
    elif meer[x][y] == 0:
        meer[x][y] = 2
        print("Wasser!")
    else:
        print("Hier hast du schon geschossen!")

def alle_versenkt(meer):
    return all(feld != 1 for reihe in meer for feld in reihe)

def spieler_schiff_setzen(meer, laenge):
    while True:
        try:
            x = int(input("x: "))
            y = int(input("y: "))
            richtung = input("Waagerecht? (j/n): ").lower() == "j"
            if setze_schiff(meer, x, y, richtung, laenge):
                break
            else:
                print("Ungültige Platzierung!")
        except:
            print("Eingabefehler. Versuche es nochmal.")

def computer_schiff_setzen(meer, laenge):
    while True:
        x = random.randint(1, GROESSE)
        y = random.randint(1, GROESSE)
        richtung = random.choice([True, False])
        if setze_schiff(meer, x, y, richtung, laenge):
            break

def spieler_zug(meer):
    while True:
        try:
            x = int(input("x: "))
            y = int(input("y: "))
            if meer[x-1][y-1] in [2, 3]:
                print("Hier hast du schon hingeschossen!")
            else:
                schiessen(meer, x, y)
                break
        except:
            print("Ungültige Eingabe!")

def computer_zug(meer):
    while True:
        x = random.randint(1, GROESSE)
        y = random.randint(1, GROESSE)
        if meer[x-1][y-1] not in [2, 3]:
            print(f"Computer schießt auf {x}, {y}")
            schiessen(meer, x, y)
            break

# Hauptprogramm
meer_spieler = neues_meer()
meer_computer = neues_meer()

print("Platziere deine Schiffe!")
for laenge in flotte:
    print(f"Schiff mit Länge {laenge}:")
    spieler_schiff_setzen(meer_spieler, laenge)

print("Computer platziert Schiffe...")
for laenge in flotte:
    computer_schiff_setzen(meer_computer, laenge)

spieler_dran = True
while True:
    if spieler_dran:
        print("\n--- Dein Zug ---")
        spieler_zug(meer_computer)
        zeige_meer(meer_computer, verdeckt=True)
        if alle_versenkt(meer_computer):
            print("Du hast gewonnen!")
            break
    else:
        print("\n--- Computer ist dran ---")
        computer_zug(meer_spieler)
        zeige_meer(meer_spieler)
        if alle_versenkt(meer_spieler):
            print("Der Computer hat gewonnen!")
            break
    spieler_dran = not spieler_dran
