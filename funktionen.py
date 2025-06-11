import pickle

feld_groesse = 10

def spielfeld():
    return ["~"] * (feld_groesse * feld_groesse)

# Mehr Schiffe
schiffe = {
    "Schlachtschiff": {"laenge": 5, "anzahl": 1},
    "Kreuzer": {"laenge": 4, "anzahl": 1},
    "Zerstörer": {"laenge": 3, "anzahl": 1},
    "U-Boot": {"laenge": 2, "anzahl": 1}
}

def zeige_feld(feld, verdeckt=False):
    print("  " + " ".join(str(i) for i in range(feld_groesse)))
    for y in range(feld_groesse):
        reihe = feld[y * feld_groesse:(y + 1) * feld_groesse]
        if verdeckt:
            reihe = ["~" if c == "S" else c for c in reihe]
        print(f"{y} " + " ".join(reihe))

def verloren(feld):
    return "S" not in feld

def schiff_setzen(feld):
    print("Setze deine Schiffe:")
    for name, info in schiffe.items():
        for i in range(info["anzahl"]):
            while True:
                zeige_feld(feld)
                eingabe = input(f"{name} (Länge {info['laenge']}) {i+1}, Koordinaten + Richtung (x y h/v): ").split()
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
                    break
                except ValueError:
                    print("❌ Ungültige Eingabe!")



def senden(conn, data):
    conn.sendall(pickle.dumps(data))

def empfangen(conn):
    return pickle.loads(conn.recv(4096))

def spielwiederholen():
    if verloren(spielfeld()):
        antwort = input("Neues Spiel starten? (j/n): ").strip().lower()
        if antwort in ["j", "ja"]:
            return True
        elif antwort in ["n", "nein"]:
            return False
        else:
            print("Ungültige Eingabe! Bitte 'j' oder 'n' eingeben.")

