import socket

# IP und Port direkt abfragen (oder fix setzen)
host = input("Gib die Server-IP ein (172.20.10.2): ")
port = int(input("Gib den Port ein (12345): "))

print("Server wird gestartet...")

server = socket.socket()
server.bind((host, port))
server.listen(1)

print(f"Warte auf Verbindung auf {host}:{port}...")
conn, addr = server.accept()
print(f"Verbunden mit {addr}")

while True:
    empfangen = conn.recv(1024).decode()
    if empfangen.lower() == "bye":
        print("Client hat die Verbindung beendet.")
        break

    print(f"Client: {empfangen}")
    antwort = input("Server: ")
    conn.send(antwort.encode())

    if antwort.lower() == "bye":
        print("Verbindung wird beendet.")
        break

conn.close()
server.close()
