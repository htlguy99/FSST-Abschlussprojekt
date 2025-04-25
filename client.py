import socket 
import os  


s = socket.socket()  
s.connect(("127.0.0.1", 12345))  

while True:
    nachricht = input("Client: ")  
    if nachricht == "bye":
        break
    s.send(nachricht.encode("utf-8"))  
    
    antwort = s.recv(30).decode("utf-8") 
    if antwort == "bye":
        break 
    print(f"Server: {antwort}")

s.close()  
print("Client gestoppt")