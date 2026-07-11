from pathlib import Path
import shutil
from config import FILE_CATEGORIES


downloads_folder = Path.home() / "Downloads"

def organize_downloads():
    for file in downloads_folder.iterdir(): 
        if file.is_file():
            category = FILE_CATEGORIES.get(file.suffix.lower(), "Other")
            destination_folder = downloads_folder / category
            destination_folder.mkdir(exist_ok=True)
            destination = destination_folder / file.name
            counter = 1
            while destination.exists():
                new_filename = f"{file.stem} ({counter}){file.suffix}"
                destination = destination_folder / new_filename
                counter += 1
            shutil.move(file, destination)
        elif file.is_dir(): 
            print(f"📁 {file.name}")