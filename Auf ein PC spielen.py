import cv2

# Lade das vortrainierte Haar-Cascade-Modell für die Gesichtserkennung
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Starte die Webcam
cap = cv2.VideoCapture(0)

# Überprüfe, ob die Webcam erfolgreich geöffnet wurde
if not cap.isOpened():
    print("Fehler: Webcam konnte nicht geöffnet werden.")
    exit()

# Parameter für die Gesichtserkennung
scaleFactor = 1.1
minNeighbors = 5
minSize = (30, 30)

try:
    while True:
        # Lese einen Frame von der Webcam
        ret, frame = cap.read()
        if not ret:
            print("Fehler beim Lesen des Frames von der Kamera.")
            break

        # Konvertiere das Bild in Graustufen (erforderlich für Haar-Cascade)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Erkenne Gesichter im Bild
        faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)

        # Zeichne Rechtecke um die erkannten Gesichter
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Zeige das Bild mit den erkannten Gesichtern
        cv2.imshow('Gesichtserkennung von Niklas', frame)

        # Beende die Schleife, wenn die Taste 'q' gedrückt wird
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Die Gesichtserkennung wurde beendet!")
            break
            
finally:
    # Gib die Ressourcen frei
    cap.release()
    cv2.destroyAllWindows()