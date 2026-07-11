# 📂 Smart Downloads Organizer

A Python automation tool that organizes files inside your Downloads folder into categorized folders based on their file extensions.

This project was built as part of my Python Automation learning journey and focuses on writing clean, modular, and maintainable Python code while solving a real-world problem.

---

## Features

- 📄 Automatically categorizes files by extension
- 📁 Creates destination folders automatically
- 🖼️ Supports images, documents, videos, audio, archives, installers, programming files, and more
- 🔤 Handles uppercase and lowercase file extensions
- 🔁 Prevents duplicate filenames by automatically renaming files
- 🧩 Modular project structure for future expansion

---

## Supported Categories

- Images
- Documents
- Spreadsheets
- Presentations
- Videos
- Audio
- Archives
- Installers
- Programming
- Java
- Disk Images
- Fonts
- Other

---

## Example

Before:

```
Downloads/
│
├── Resume.pdf
├── Vacation.png
├── Music.mp3
├── ChromeSetup.exe
```

After:

```
Downloads/
│
├── Documents/
│   └── Resume.pdf
│
├── Images/
│   └── Vacation.png
│
├── Audio/
│   └── Music.mp3
│
└── Installers/
    └── ChromeSetup.exe
```

Duplicate files are automatically renamed.

Example:

```
Resume.pdf
Resume (1).pdf
Resume (2).pdf
```

---

## Technologies Used

- Python 3
- pathlib
- shutil

---

## Project Structure

```
smart-download-organizer/
│
├── main.py
├── organizer.py
├── config.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Future Improvements

- Logging system
- Dry-run mode
- Undo support
- Recursive folder organization
- Configuration file (JSON/YAML)
- PySide6 graphical interface
- Automatic folder watching
- Unit tests

---

## What I Learned

This project helped me practice:

- Functions
- Dictionaries
- Loops
- Conditionals
- Modular project organization
- pathlib
- shutil
- File system automation
- Duplicate file handling
- Writing maintainable Python code

---

## Version History

### v1.0.0
- Automatic file categorization
- Dynamic folder creation
- Duplicate filename handling
- Modular project structure
- Cross-platform path support with `pathlib`

---

## License

This project is licensed under the MIT License.