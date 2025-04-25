import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt, falls sie nicht existiert)
conn = sqlite3.connect("M:\\HTL\\4.Schuljahr\\FSST\\Abschlussprojekt\\schiffe_versenken.db")



# Cursor-Objekt erstellen, um SQL-Befehle auszuführen
cursor = conn.cursor()

# Tabelle erstellen, falls sie noch nicht existiert
cursor.execute("""
CREATE TABLE IF NOT EXISTS spiele (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    spielername TEXT NOT NULL,
    datum TEXT NOT NULL,
    ergebnis TEXT NOT NULL
)
""")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Datenbank und Tabelle wurden erfolgreich erstellt!")
