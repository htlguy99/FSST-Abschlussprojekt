import tkinter as tk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk

# Konfigurationen
raster = 10  # Größe des Spielfelds (10x10)
zelle = 50  # Größe jeder Zelle in Pixeln

# Schiffsgrößen
schiff_typen = {
    "Schlachtschiff": 5,
    "Kreuzer": 4,
    "Zerstörer": 3,
    "U-Boot": 2
}

# Schiffsanzahl
schiff_anzahl = {
    "Schlachtschiff": 1,
    "Kreuzer": 2,
    "Zerstörer": 3,
    "U-Boot": 4
}

# Laden und Skalieren von Bildern
def bild_skallierung(dateipfad, breite, höhe):
    if not os.path.exists(dateipfad):
        print("Datei nicht gefunden:", dateipfad)
        print("Ordnerinhalt:", os.listdir(os.path.dirname(dateipfad)))
        raise FileNotFoundError(f"Bild nicht gefunden: {dateipfad}")
    bild = Image.open(dateipfad)
    bild = bild.resize((breite, höhe), Image.LANCZOS)
    return ImageTk.PhotoImage(bild)

# Spielfeld erstellen
def raster(canvas):
    for i in range(raster + 1):
        canvas.create_line(i * zelle, 0, i * zelle, raster * zelle, fill="black")
        canvas.create_line(0, i * zelle, raster * zelle, i * zelle, fill="black")

# Hauptfenster erstellen
def hauptfenster():
    root = tk.Tk()
    root.title("Schiffe Versenken")
    canvas = tk.Canvas(root, width=raster * zelle, height=raster * zelle)
    canvas.pack()
    root.bilder = []
    pfad = r"c:\Users\nikla\Documents\Schule\4cHEL\FSST\Abschlussprojekt"

    # Hintergrundbild (Meer)
    meer_bild_pfad = os.path.join(pfad, "sea.png")
    meer_bild = bild_skallierung(meer_bild_pfad, zelle, zelle)
    root.bilder.append(meer_bild)

    for x in range(0, raster * zelle, zelle):
        for y in range(0, raster * zelle, zelle):
            canvas.create_image(x, y, image=meer_bild, anchor="nw")

    # Schiff-Bild laden
    schiff_bild_pfad = os.path.join(pfad, "schiff.png")
    schiff_bild = bild_skallierung(schiff_bild_pfad, zelle, zelle)
    root.bilder.append(schiff_bild)
    raster(canvas)
    aktueller_schiffs_typ = {"typ": "Schlachtschiff"}
    gesetzte_schiffe_anzahl = {key: 0 for key in schiff_anzahl}
    schiff_koordinaten = []

    # Mausklick-Callback auf das Spielfeld
    def mausklick(event):
        schiffs_typ = aktueller_schiffs_typ["typ"]
        länge = schiff_typen[schiffs_typ]

        # Prüfen, ob noch Schiffe dieses Typs gesetzt werden dürfen
        if gesetzte_schiffe_anzahl[schiffs_typ] >= schiff_anzahl[schiffs_typ]:
            print(f"{schiff_anzahl[schiffs_typ]} {schiffs_typ}(e) gesetzt!")
            return

        # Rasterposition berechnen
        raster_x = event.x // zelle
        raster_y = event.y // zelle

        # Prüfen, ob Schiff innerhalb des Rasters passt (waagrecht)
        if raster_x + länge > raster:
            print("Schiff passt nicht mehr ins Raster (zu lang)!")
            return

        # Prüfen, ob schon Schiff an der Stelle liegt
        for i in range(länge):
            if (raster_x + i, raster_y) in schiff_koordinaten:
                print("Da liegt schon ein anderes Schiff!")
                return

        # Schiff platzieren (waagrecht)
        for i in range(länge):
            x_pixel = (raster_x + i) * zelle
            y_pixel = raster_y * zelle
            canvas.create_image(x_pixel, y_pixel, image=schiff_bild, anchor="nw")
            schiff_koordinaten.append((raster_x + i, raster_y))

        gesetzte_schiffe_anzahl[schiffs_typ] += 1
        print(f"{schiffs_typ} platziert bei Start-Zelle: ({raster_x}, {raster_y})")
        raster(canvas)

    # Schifftyp auswählen
    def schiffstypen(event):
        taste = event.char
        if taste == "1":
            aktueller_schiffs_typ["typ"] = "Schlachtschiff"
        elif taste == "2":
            aktueller_schiffs_typ["typ"] = "Kreuzer"
        elif taste == "3":
            aktueller_schiffs_typ["typ"] = "Zerstörer"
        elif taste == "4":
            aktueller_schiffs_typ["typ"] = "U-Boot"
        print(f"Aktueller Schiffstyp: {aktueller_schiffs_typ['typ']}")

    canvas.bind("<Button-1>", mausklick)
    root.bind("<Key>", schiffstypen)
    print("Nutze Tasten 1 (Schlachtschiff), 2 (Kreuzer), 3 (Zerstörer), 4 (U-Boot) zum Auswählen!")
    root.mainloop()

hauptfenster()
