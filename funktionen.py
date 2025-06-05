import pickle

def spielfeld():
    return ["~"] * 25

def zeige_feld(feld, verdeckt=False):
    print("  0 1 2 3 4")
    for i in range(5):
        reihe = feld[i*5:(i+1)*5]
        if verdeckt:
            reihe = ["~" if c == "S" else c for c in reihe]
        print(f"{i} " + " ".join(reihe))

def verloren(feld):
    return "S" not in feld

def schiff_setzen(feld):
    print("Setze 2 Schiffe (jeweils Länge 1):")
    for i in range(2):
        while True:
            zeige_feld(feld)
            eingabe = input(f"Schiff {i+1} Koordinaten (x y): ").split()
            if len(eingabe) != 2:
                print("❌ Zwei Zahlen mit Leerzeichen eingeben!")
                continue
            try:
                x, y = map(int, eingabe)
                if 0 <= x <= 4 and 0 <= y <= 4:
                    pos = y * 5 + x
                    if feld[pos] == "~":
                        feld[pos] = "S"
                        break
                    else:
                        print("❌ Feld schon belegt.")
                else:
                    print("❌ Nur Koordinaten 0 bis 4.")
            except ValueError:
                print("❌ Ungültige Eingabe!")

def senden(conn, data):
    conn.sendall(pickle.dumps(data))

def empfangen(conn):
    return pickle.loads(conn.recv(4096))
