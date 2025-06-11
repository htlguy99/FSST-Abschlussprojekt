import socket
from funktionen import *
from funktionen import feld_groesse  

def server():
    host = '0.0.0.0'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"🟢 Server läuft. Warte auf Verbindung auf Port {port}...")
        conn, addr = s.accept()
        print("🔗 Verbunden mit:", addr)

        feld_server = spielfeld()
        schiff_setzen(feld_server)
        senden(conn, feld_server)

        feld_client = empfangen(conn)
        print("📦 Gegnerisches Feld empfangen.")

        while True:
            # Server schießt
            zeige_feld(feld_client, verdeckt=True)
            while True:
                try:
                    x, y = map(int, input("🎯 Dein Schuss (x y): ").split())
                    
                    if 0 <= x < feld_groesse and 0 <= y < feld_groesse:
                        break
                    print("❌ Nur Koordinaten 0–4!")
                except:
                    print("❌ Ungültige Eingabe!")

            senden(conn, (x, y))

            # Empfang aktualisiertes Gegnerfeld + Rückmeldung
            feld_client, status = empfangen(conn)
            print(f"🛠️ Gegnerisches Feld aktualisiert.")
            if status == "treffer":
                print("🚀 Treffer!")
            elif status == "verfehlt":
                print("💨 Verfehlt!")
            elif status == "doppelschuss":
                print("❗ Doppelschuss!")

            if verloren(feld_client):
                print("🏆 Du hast gewonnen!")
                senden(conn, "verloren")
                break
            else:
                senden(conn, "weiter")

            # Gegner schießt
            print("⏳ Warte auf gegnerischen Schuss...")
            data = empfangen(conn)
            if data == "verloren":
                print("💥 Du hast verloren.")
                break
            x, y = data
            pos = y * feld_groesse + x
            if feld_server[pos] == "S":
                feld_server[pos] = "X"
                schuss_status = "treffer"
                print("🚨 Treffer auf dein Schiff!")
            elif feld_server[pos] in ["X", "0"]:
                schuss_status = "doppelschuss"
                print("❗ Doppelschuss auf bereits getroffene Stelle.")
            else:
                feld_server[pos] = "0"
                schuss_status = "verfehlt"
                print("💨 Gegner hat verfehlt.")
            senden(conn, (feld_server, schuss_status))

            if verloren(feld_server):
                print("💥 Deine Schiffe sind alle versenkt. Du hast verloren!")
                senden(conn, "verloren")
                break

            # Frage nach einer neuen Runde
           

if __name__ == "__main__":
    server()
