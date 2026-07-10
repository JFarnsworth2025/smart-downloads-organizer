from pathlib import Path


downloads_folder = Path.home() / "Downloads"

def organize_downloads():
    for file in downloads_folder.iterdir(): 
        if file.is_file(): 
            print(f"📄 {file.name}") 
        elif file.is_dir(): 
            print(f"📁 {file.name}")