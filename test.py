from unittest.mock import patch

# Die Eingaben, die das Spiel erwartet (als Strings)
eingaben = [
    "0", "0", "0", "1",
    "1", "0", "1", "1",
    "2", "0", "2", "1",
    "3", "0", "3", "1",
    "2", "0",
    "0", "0",
    "2", "1",
    "0", "1"
]

with patch("builtins.input", side_effect=eingaben):
    # Hier kommt dein Spielcode (oder importiere ihn)
    # Beispiel:
    from Spiel_1 import spiel_starten
    spiel_starten()
