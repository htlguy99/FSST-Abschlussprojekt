import socket
import pickle

"""Client-Code"""

def spielfeld():
    return ["~"] * 25

def zeige_feld(feld):
    print("  0 1 2 3 4")
    for i in range(5):
        print(f"{i} " + " ".join(feld[i * 5:(i + 1) * 5]))

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

def client():
    host = input("Server-IP eingeben: ")
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Verbunden mit Server.")

        feld_client = spielfeld()
        schiff_setzen(feld_client)

        senden(s, feld_client)
        feld_server = empfangen(s)
        print("Gegnerische Schiffe erhalten.")

        while True:
            # Server schießt
            print("Warte auf Schuss des Gegners...")
            data = empfangen(s)
            if data == "verloren":
                print("Du hast verloren!")
                break
            x, y = data
            pos = y * 5 + x
            if feld_client[pos] == "S":
                feld_client[pos] = "X"
                print("Dein Schiff wurde getroffen!")
            elif feld_client[pos] in ["X", "0"]:
                print("Doppelschuss!")
            else:
                feld_client[pos] = "0"
                print("Gegner hat verfehlt.")
            senden(s, feld_client)

            status = empfangen(s)
            if status == "verloren":
                print("Du hast gewonnen!")
                break

            # Jetzt Client schießt
            zeige_feld(["~" if c == "S" else c for c in feld_server])
            print("Dein Zug!")
            while True:
                try:
                    x, y = map(int, input("Schuss (x y): ").split())
                    if 0 <= x <= 4 and 0 <= y <= 4:
                        break
                    else:
                        print("Nur Koordinaten 0-4!")
                except:
                    print("Ungültig!")

            senden(s, (x, y))
            feld_server = empfangen(s)
            print("Gegnerisches Feld aktualisiert.")

    client()
