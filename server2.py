import socket, pickle
from Spiel_1 import *

name1 = input("Spieler 1, dein Name: ")

host = '0.0.0.0'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print("🟢 Server läuft. Warte auf Spieler 2 ...")
    conn, addr = s.accept()
    print("🔗 Verbunden mit:", addr)

    feld1 = spielfeld()
    feld2 = spielfeld()

    schiff_setzen(feld1, name1)
    conn.sendall(pickle.dumps(feld1))  # Sende eigenes Feld

    feld2 = pickle.loads(conn.recv(4096))  # Empfange Feld von Client
    name2 = pickle.loads(conn.recv(4096))  # Empfange Namen
    conn.sendall(pickle.dumps(name1))     # Sende eigenen Namen

    spieler = name1
    while True:
        if spieler == name1:
            feld2 = schiessen(feld2, name1)
            conn.sendall(pickle.dumps(feld2))
            if verloren(feld2):
                print(f"{name1} gewinnt! 🏆")
                conn.sendall(b"verloren")
                break
            conn.sendall(b"weiter")
            spieler = name2
        else:
            print(f"\n{name2} ist dran...")
            feld1 = pickle.loads(conn.recv(4096))
            status = conn.recv(1024)
            if status == b"verloren":
                print(f"{name2} gewinnt! 🏆")
                break
            spieler = name1
