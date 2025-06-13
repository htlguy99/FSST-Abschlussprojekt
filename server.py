"""
Titel: Server-Code für Schiffe versenken
Autoren: Myron, Niklas und Volkan
"""


import socket
from funktionen import *
from funktionen import feld_groesse 
from PIL import Image


# holt die lokale IP-Adresse des Servers
def lokale_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except socket.error as e:
        return f"Fehler beim Abrufen der IP: {e}"


def server():
    host = lokale_ip()
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f" Server läuft. Warte auf Verbindung auf {host} und Port {port}...")
        conn, addr = s.accept()
        print(" Verbunden mit:", addr)

        
        feld_server = spielfeld()
        name = name_spieler()
        print("Möchtest du eine spielanleitung sehen? (ja/nein)")
        if input().strip().lower() == "ja":
            spielanleitung()
        else:
            print("Ok viel Spaß beim Spielen!")
        print(f"Spielername: {name}")
        schiff_setzen(feld_server, name)
        senden(conn, feld_server)

        feld_client = empfangen(conn)
        print(" Gegnerisches Feld empfangen.")

        while True:
            zeige_beide_felder(feld_server, feld_client)
            while True:
                try:
                    x, y = map(int, input(" Dein Schuss (x y): ").split())
                    
                    if 0 <= x < feld_groesse and 0 <= y < feld_groesse:
                        break
                    print("❌ Nur Koordinaten 0-9!")
                except:
                    print("❌ Ungültige Eingabe!")
            zeige_beide_felder(feld_client, feld_server) 

            senden(conn, (x, y))

            # Empfang aktualisiertes Gegnerfeld + Rückmeldung
            feld_client, status = empfangen(conn)
            print(f" Gegnerisches Feld aktualisiert.")
            if status == "treffer":

                print("Treffer!")
            elif status == "verfehlt":
                print("Verfehlt!")
            elif status == "doppelschuss":
                print("Doppelschuss!")
                print(" Treffer!")
            elif status == "verfehlt":
                print(" Verfehlt!")
            elif status == "doppelschuss":
                print(" Doppelschuss!")

            if verloren(feld_client):
                print("Du hast gewonnen!")
                senden(conn, "verloren :( )")
                break
            else:
                senden(conn, "weiter")

            # Gegner schießt
            print(" Warte auf gegnerischen Schuss...")
            data = empfangen(conn)
            if data == "verloren":
                print(" Du hast verloren :( )")
                break
            x, y = data
            pos = y * feld_groesse + x
            if feld_server[pos] == "S":
                feld_server[pos] = "X"
                schuss_status = "treffer"
                print(" Treffer auf dein Schiff!")
            elif feld_server[pos] in ["X", "⭕"]:
                schuss_status = "doppelschuss"
                print(" Doppelschuss auf bereits getroffene Stelle.")
            else:
                feld_server[pos] = "⭕"
                schuss_status = "verfehlt"
                print("Gegner hat verfehlt.")
            senden(conn, (feld_server, schuss_status))

            if verloren(feld_server):
                print("Deine Schiffe sind alle versenkt. Du hast verloren!")
                senden(conn, "verloren")
                break
        bewertung()

server()