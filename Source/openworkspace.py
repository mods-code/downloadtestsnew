
from tkinter import filedialog
import os
import shutil

# Funktion, die aufgerufen wird, wenn der Button geklickt wird
def choose_folder_and_copy():
    # Öffnet ein File Picker, um den Ordner auszuwählen
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        # Erstellt einen neuen Ordner unter mods/ mit dem Namen des ausgewählten Ordners
        new_folder = os.path.join("mods", os.path.basename(selected_folder))
        os.makedirs(new_folder, exist_ok=True)

        # Kopiert den Inhalt des ausgewählten Ordners und aller Unterordner in den neuen Ordner
        for dirpath, dirnames, filenames in os.walk(selected_folder):
            # Erstellt das entsprechende Zielverzeichnis
            relative_path = os.path.relpath(dirpath, selected_folder)
            new_dir = os.path.join(new_folder, relative_path)
            os.makedirs(new_dir, exist_ok=True)

            # Kopiert alle Dateien im Verzeichnis
            for filename in filenames:
                src_file = os.path.join(dirpath, filename)
                dst_file = os.path.join(new_dir, filename)
                shutil.copy(src_file, dst_file)

