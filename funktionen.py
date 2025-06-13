"""
Titel: Funktionen-Code für Schiffe versenken
Autoren: Myron, Niklas und Volkan
"""

import pickle
from PIL import Image
import threading
import keyboard


feld_groesse = 10

def spielfeld():
    return ["~"] * (feld_groesse * feld_groesse)

# Schiffe mit Länge und Anzahl
#volkan
schiffe = {
    "🚢 Schlachtschiff": {"laenge": 1, "anzahl": 1},
    "🛳️ Kreuzer": {"laenge": 1, "anzahl": 1},
    "🚤 Zerstörer": {"laenge": 1, "anzahl": 1},
    "🛶 U-Boot": {"laenge": 1, "anzahl": 1}
}

#volkan
def name_spieler():
    name = input(" Gib deinen Spielernamen ein: ").strip()
    if not name:
        print("❌ Kein Name eingegeben. Bitte versuche es erneut.")
        return name_spieler()
    return name

#volkan
def zeige_feld(feld, verdeckt=False):
    # Spaltenkopf
    print("    " + "  ".join(f"{i}" for i in range(feld_groesse)))  # Zwei Leerzeichen statt einem
    for y in range(feld_groesse):
        reihe = feld[y * feld_groesse:(y + 1) * feld_groesse]
        if verdeckt:
            reihe = ["🌊" if c == "S" else ersetze_symbol(c) for c in reihe]
        else:
            reihe = [ersetze_symbol(c) for c in reihe]
        print(f"{y:2} " + "".join(f"{z:<2}" for z in reihe))


#volkan
def bewertung():
    print("Hat dir das Spiel gefallen? (ja/nein)")
    if input().strip().lower() == "ja":
        print("Danke fürs Spielen!")
        try:
            bild = Image.open("nmv.jpg")  # Stelle sicher, dass die Datei existiert
            bild.show()
        except Exception as e:
            print("Bild konnte nicht angezeigt werden:", e)
    else:
        print("Schade :( )")
#volkan
def zeige_beide_felder(eigenes_feld, gegnerisches_feld):
    print("\n Dein Feld".ljust(50) +  " Gegnerisches Feld") 
    print("\n Dein Feld".ljust(50) + " Gegnerisches Feld")
    # Kopfzeile für beide Felder (Spaltennummern)
    spaltenkopf= "   " + " ".join(f"{i:<3}" for i in range(feld_groesse)) # Zwei Leerzeichen zwischen den Feldern für bessere Trennung
    spaltenkopf2 = "   " + " ".join(f"{i:<3}" for i in range(feld_groesse)) # Zwei Leerzeichen zwischen den Feldern für bessere Trennung
    print(spaltenkopf + "      " + spaltenkopf2)  # Zwei Leerzeichen zwischen den Feldern für bessere Trennung

    # Zeilen
    for y in range(feld_groesse):
        eigene_reihe = [ersetze_symbol(z) for z in eigenes_feld[y * feld_groesse:(y + 1) * feld_groesse]]
        gegner_reihe = []
        for z in gegnerisches_feld[y * feld_groesse:(y + 1) * feld_groesse]:
            if z == "X":
                gegner_reihe.append("💥")
            elif z == "⭕":
                gegner_reihe.append("⭕")
            else:
                gegner_reihe.append("🌊")
        print(f"{y:<2} " + "".join(f"{z:<3}" for z in eigene_reihe) + "    " + f"{y:<2} " + "".join(f"{z:<3}" for z in gegner_reihe))


def spielchat():
    print("💬 Willkommen im Spielchat!")
    print("Tippe 'exit' zum Beenden.")
    while True:
        nachricht = input("Nachricht: ")
        if nachricht.lower() == "exit":
            print("Chat beendet.")
            break
        print(f"🗨️ {nachricht}")


#volkan
def spielanleitung():
    print("Spielanleitung:")
    print("1. Jeder Spieler platziert seine Schiffe auf einem 10x10 Feld.")
    print("2. Schiffe können horizontal oder vertikal platziert werden.")
    print("3. Ein Schiff kann nicht überlappen oder außerhalb des Feldes platziert werden.")
    print("4. Spieler schießen abwechselnd auf das gegnerische Feld.")
    print("5. Treffer werden mit '💥', verfehlte Schüsse mit '⭕' markiert.")
    print("6. Das Spiel endet, wenn alle Schiffe eines Spielers versenkt sind.")

#niklas
def ersetze_symbol(z):
    if z == "~":
        return "🌊"
    elif z == "S":
        return "🚢"
    elif z == "X":
        return "💥"
    elif z == "O":
        return "⭕"
    else:
        return z

#niklas
def verloren(feld):
    return "S" not in feld


#myron
def schiff_setzen(feld, name):
    print(f"{name} Setze deine Schiffe:")
    for name, info in schiffe.items():
        for i in range(info["anzahl"]):
            while True:
                zeige_feld(feld)
                eingabe = input(f"{name} (Länge {info['laenge']}) #{i+1} - Koordinaten + Richtung (x y h/v): ").split()
                if len(eingabe) != 3:
                    print("❌ Drei Eingaben nötig: x y h/v")
                    continue
                try:
                    x, y = map(int, eingabe[:2])
                    richtung = eingabe[2].lower()
                    if richtung not in ["h", "v"]:
                        print("❌ Richtung muss 'h' (horizontal) oder 'v' (vertikal) sein.")
                        continue

                    # Prüfen, ob Platz vorhanden ist
                    pos_liste = []
                    passt = True
                    for j in range(info["laenge"]):
                        nx = x + j if richtung == "h" else x
                        ny = y if richtung == "h" else y + j
                        if 0 <= nx < feld_groesse and 0 <= ny < feld_groesse:
                            pos = ny * feld_groesse + nx
                            if feld[pos] == "~":
                                pos_liste.append(pos)
                            else:
                                print("❌ Ein Feld ist schon belegt.")
                                passt = False
                                break
                        else:
                            print("❌ Schiff passt nicht aufs Feld.")
                            passt = False
                            break

                    if not passt:
                        continue

                    for pos in pos_liste:
                        feld[pos] = "S"
                    print("✅ Schiff platziert!")
                    break
                except ValueError:
                    print("❌ Ungültige Eingabe!")

def senden(conn, data):
    conn.sendall(pickle.dumps(data))

def empfangen(conn):
    return pickle.loads(conn.recv(4096))