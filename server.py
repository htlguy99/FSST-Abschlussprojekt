import socket
import pickle

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

def server():
    host = '0.0.0.0'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"🟢 Server gestartet. Warte auf Verbindung auf Port {port}...")
        conn, addr = s.accept()
        print("🔗 Verbunden mit:", addr)

        feld_server = spielfeld()
        schiff_setzen(feld_server)
        senden(conn, feld_server)

        feld_client = empfangen(conn)
        print("📦 Gegnerische Schiffe erhalten.")

        while True:
            # Server schießt
            zeige_feld(["~" if c == "S" else c for c in feld_client])
            print("🎯 Dein Zug!")
            while True:
                try:
                    x, y = map(int, input("Schuss (x y): ").split())
                    if 0 <= x <= 4 and 0 <= y <= 4:
                        break
                    else:
                        print("Nur Koordinaten 0-4!")
                except:
                    print("Ungültige Eingabe!")

            senden(conn, (x, y))
            feld_client = empfangen(conn)
            print("🛠️ Gegnerisches Feld aktualisiert.")

            if verloren(feld_client):
                print("🏆 Du hast gewonnen!")
                senden(conn, "verloren")
                break
            else:
                senden(conn, "weiter")

            # Client schießt
            print("⏳ Warte auf gegnerischen Schuss...")
            data = empfangen(conn)
            if data == "verloren":
                print("💥 Du hast verloren!")
                break
            x, y = data
            pos = y * 5 + x
            if feld_server[pos] == "S":
                feld_server[pos] = "X"
                print("🚨 Dein Schiff wurde getroffen!")
            elif feld_server[pos] in ["X", "0"]:
                print("❗ Doppelschuss!")
            else:
                feld_server[pos] = "0"
                print("💨 Gegner hat verfehlt.")
            senden(conn, feld_server)


server()