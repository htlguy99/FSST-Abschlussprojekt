# ⚓ Netzwerk-Schiffe-Versenken

Ein Schiffe-Versenken-Spiel, das über zwei Computer im lokalen Netzwerk funktioniert. Die Spieler sind über Python-Sockets verbunden, und der Spielfortschritt wird in einer Datenbank gespeichert.

## 🎯 Ziel des Projekts

- Zwei Spieler treten über das Netzwerk gegeneinander an.
- Die Spieler platzieren ihre Schiffe und geben abwechselnd Koordinaten ein.
- Treffer und Versenken werden automatisch erkannt.
- Das Spiel wird mit SQLite gespeichert: Spielername, Datum, Ergebnis.
- Optional: Eine grafische Oberfläche mit Tkinter.

## 🧩 Technologien

| Bereich             | Tool / Technologie   |
|---------------------|----------------------|
| Programmiersprache  | Python 3             |
| Netzwerk            | socket, threading    |
| Datenbank           | SQLite               |
| Oberfläche (optional) | Tkinter           |
| Source Control      | Git + GitHub         |

## 📌 Wichtige User Stories

- Als Spieler möchte ich Schiffe setzen, um zu spielen.
- Als Spieler möchte ich koordinatenbasierte Angriffe machen.
- Als Spieler möchte ich wissen, ob ich getroffen habe oder nicht.
- Als Spieler möchte ich sehen, wenn ich das Spiel gewonnen habe.
- Als Spieler möchte ich meine Ergebnisse später ansehen können.

## 🔁 Geplante Iterationen

| Datum      | Ziel                                            |
|------------|--------------------------------------------------|
| 4. April   | Themenfindung & Präsentation                    |
| 11. April  | Socket-Verbindung & einfache Kommunikation      |
| 25. April  | Spiellogik (Setzen, Schießen, Treffer prüfen)   |
| 9. Mai     | Sieg-Erkennung und Spielende                    |
| 16. Mai    | Datenbank-Anbindung                             |
| 6. Juni    | Optionale GUI / Polishing                       |
| 13. Juni   | Abschlusspräsentation mit Live-Demo             |

## ✅ Erste Aufgaben (GitHub Issues)

- [ ] Socket-Verbindung aufbauen (Server/Client)
- [ ] Threads für parallele Kommunikation einbauen
- [ ] Spielfeld (10x10) anlegen
- [ ] Schiffe setzen (manuell oder zufällig)
- [ ] Trefferlogik + Kommunikation
- [ ] Datenbank vorbereiten und schreiben

## 👥 Team

- Alexander Jäger
- Patrick Korber
