import socket
from funktionen import *
from funktionen import feld_groesse  # ganz oben einfügen




def client():
    host = input("🔌 Server-IP eingeben: ")
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
        except ConnectionRefusedError:
            print("❌ Verbindung fehlgeschlagen. Ist der Server gestartet?")
            return

        print("✅ Verbunden mit Server.")

        feld_client = spielfeld()
        schiff_setzen(feld_client) 

        senden(s, feld_client)
        feld_server = empfangen(s)
        print("📦 Gegnerisches Feld erhalten.")

        while True:
            # Warten auf Schuss des Servers
            print("⏳ Warte auf Schuss des Gegners...")
            data = empfangen(s)
            if data == "verloren":
                print("💥 Du hast verloren!")
                break
            x, y = data
            pos = y * feld_groesse + x

            if feld_client[pos] == "S":
                feld_client[pos] = "X"
                schuss_status = "treffer"
                print("🚨 Dein Schiff wurde getroffen!")
            elif feld_client[pos] in ["X", "0"]:
                schuss_status = "doppelschuss"
                print("❗ Doppelschuss!")
            else:
                feld_client[pos] = "0"
                schuss_status = "verfehlt"
                print("💨 Gegner hat verfehlt.")
            senden(s, (feld_client, schuss_status))

            status = empfangen(s)
            if status == "verloren":
                print("Du hast verloren :( )")
                break
            elif status != "weiter":
                print(f"Unbekannter Status: {status}")

            # Jetzt Client schießt
            zeige_feld(feld_server, verdeckt=True)
            print("🎯 Dein Zug!")
            while True:
                try:
                    x, y = map(int, input("Schuss (x y): ").split())
                    
                    if 0 <= x < feld_groesse and 0 <= y < feld_groesse:
                        break
                    else:
                        print("Nur Koordinaten 0-4!")
                except:
                    print("Ungültige Eingabe!")

            senden(s, (x, y))

            feld_server, schuss_status = empfangen(s)
            print(f"🛠️ Gegnerisches Feld aktualisiert.")
            if schuss_status == "treffer":
                print("🚀 Treffer!")
            elif schuss_status == "verfehlt":
                print("💨 Verfehlt!")
            elif schuss_status == "doppelschuss":
                print("❗ Doppelschuss!")

            if verloren(feld_server):
                print("💥 Du hast verloren.")
                senden(s, "verloren")
                break  
            


                


            

if __name__ == "__main__":
    client()
