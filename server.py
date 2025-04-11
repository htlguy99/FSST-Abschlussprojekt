import socket
import os

# Überprüfen, ob die Datei mit der IP und dem Port existiert
if os.path.exists("ip.txt"):
    with open("ip.txt", "r") as file:
        data = file.read()
    host, port = data.split(":")
    port = int(port)
else:
    host = input("Gib die Server-IP ein: ")
    port = int(input("Gib den Port ein: "))
    with open("ip.txt", "w") as file:
        file.write(f"{host}:{port}")

print("Server wird gestartet")

# Socket erstellen und binden
s = socket.socket()
try:
    s.bind((host, port))
except Exception as e:
    print(f"Fehler beim Binden des Servers: {e}")
    exit()

s.listen(1)

print("Warte auf Verbindung...")
conn, addr = s.accept()
print(f"Verbunden mit {addr}")

while True:
    data = conn.recv(1024).decode()  
    if not data:
        break
    if data == "bye":
        break
    print(f"Client: {data}")

    antwort = input("Server: ")
    if antwort == "bye":
        break
    conn.send(antwort.encode())


conn.close()
s.close()
print("Server gestoppt")
