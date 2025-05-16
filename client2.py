import socket, pickle
from Spiel_1 import *

name2 = input("Spieler 2, dein Name: ")
host = input("Server-IP eingeben (z.B. 127.0.0.1): ")
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((host, port))
    except:
        print("❌ Verbindung zum Server fehlgeschlagen.")
        exit()

    feld1 = pickle.loads(s.recv(4096))  # Empfange gegnerisches Feld
    feld2 = spielfeld()
    schiff_setzen(feld2, name2)
    s.sendall(pickle.dumps(feld2))      # Sende eigenes Feld
    s.sendall(pickle.dumps(name2))      # Sende Namen
    name1 = pickle.loads(s.recv(4096))  # Empfange Gegnernamen

    spieler = name2
    while True:
        if spieler == name2:
            feld1 = schiessen(feld1, name2)
            s.sendall(pickle.dumps(feld1))
            status = s.recv(1024)
            if status == b"verloren":
                print(f"{name2} gewinnt! 🏆")
                break
            spieler = name1
        else:
            print(f"\n{name1} ist dran...")
            feld2 = pickle.loads(s.recv(4096))
            s.sendall(pickle.dumps(feld2))
            if verloren(feld2):
                s.sendall(b"verloren")
                print(f"{name1} gewinnt! 🏆")
                break
            else:
                s.sendall(b"weiter")
                spieler = name2
