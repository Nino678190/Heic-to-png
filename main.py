import os
from PIL import Image

def convert_to_png(directory):
    # Durchlaufe alle Dateien im angegebenen Verzeichnis
    for filename in os.listdir(directory):
        # Erstelle den vollständigen Pfad zur Datei
        file_path = os.path.join(directory, filename)
        
        # Überprüfe, ob es sich um eine Datei handelt
        if os.path.isfile(file_path):
            # Öffne die Bilddatei
            try:
                with Image.open(file_path) as img:
                    # Setze den Namen der Ausgabedatei
                    base, _ = os.path.splitext(filename)
                    new_filename = base + '.png'
                    new_file_path = os.path.join(directory, new_filename)
                    
                    # Konvertiere das Bild in PNG und speichere es
                    img.save(new_file_path, 'PNG')
                    print(f'{filename} wurde erfolgreich in {new_filename} umgewandelt.')
            except Exception as e:
                print(f'Fehler beim Verarbeiten von {filename}: {e}')

# Beispielaufruf der Funktion
convert_to_png('/pfad/zu/deinem/ordner')
