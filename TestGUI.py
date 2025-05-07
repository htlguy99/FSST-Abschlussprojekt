import tkinter as tk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk  # Pillow-Bibliothek für Bildskalierung

# Konfigurationen
GRID_SIZE = 10  # Größe des Spielfelds (10x10)
CELL_SIZE = 50  # Größe jeder Zelle in Pixeln

def load_and_resize_image(file_path, width, height):
    """Hilfsfunktion zum Laden und Skalieren von Bildern."""
    if not os.path.exists(file_path):
        print("⚠️ Datei nicht gefunden:", file_path)
        print("📂 Ordnerinhalt:", os.listdir(os.path.dirname(file_path)))
        raise FileNotFoundError(f"Bild nicht gefunden: {file_path}")
    image = Image.open(file_path)  # Bild mit Pillow öffnen
    image = image.resize((width, height), Image.LANCZOS)  # Bild skalieren
    return ImageTk.PhotoImage(image)  # In tkinter-kompatibles Bild umwandeln

def draw_grid(canvas):
    """Zeichnet das Spielfeldraster."""
    for i in range(GRID_SIZE + 1):
        canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE, fill="black")
        canvas.create_line(0, i * CELL_SIZE, GRID_SIZE * CELL_SIZE, i * CELL_SIZE, fill="black")

def create_game_window():
    """Erstellt das Hauptfenster und das Spielfeld."""
    root = tk.Tk()
    root.title("Schiffe Versenken")

    # Canvas für das Spielfeld
    canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
    canvas.pack()

    # Bildreferenzen speichern, sonst werden sie vom Garbage Collector entfernt
    root.images = []

    # Ordnerpfad
    image_folder = r"c:\Users\nikla\Documents\Schule\4cHEL\FSST\Abschlussprojekt"

    # Hintergrundbild (Meer)
    sea_image_path = os.path.join(image_folder, "sea.png")
    sea_image = load_and_resize_image(sea_image_path, CELL_SIZE, CELL_SIZE)
    root.images.append(sea_image)

    for x in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
        for y in range(0, GRID_SIZE * CELL_SIZE, CELL_SIZE):
            canvas.create_image(x, y, image=sea_image, anchor="nw")

    # Schiff platzieren
    ship_image_path = os.path.join(image_folder, "schiff.png")
    ship_image = load_and_resize_image(ship_image_path, CELL_SIZE, CELL_SIZE)
    root.images.append(ship_image)

    canvas.create_image(2 * CELL_SIZE, 3 * CELL_SIZE, image=ship_image, anchor="nw")

    # Spielfeldraster zeichnen
    draw_grid(canvas)

    root.mainloop()


create_game_window()