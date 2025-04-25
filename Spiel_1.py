
def Spielfeld():
    return ["~"] * 25 

# Dictionary für die Schiffe
SHIPS = {'A': 2, 'B': 3, 'C': 4}

Spielfeld[7] = "A"  
Spielfeld[8] = "A"  
Spielfeld[12] = "B" 
Spielfeld[13] = "B"  
Spielfeld[14] = "B"  
Spielfeld[17] = "C"  
Spielfeld[18] = "C"  
Spielfeld[19] = "C"  
Spielfeld[20] = "C"  

# Funktion zum Anzeigen des Spielfeldes
def zeige_feld():
    for i in range(5):
        print(" ".join(Spielfeld[i*5:(i+1)*5]))
    print()

def schiff_setzen(x,y):
    # Hier wird das Schiff gesetzt, wenn der Platz frei ist
    if Spielfeld[x*5 + y] == "~":
        Spielfeld[x*5 + y] = "X"  # Beispiel: Schiff setzen
        return True
    else:
        print("Platz ist bereits belegt!")
        return False


