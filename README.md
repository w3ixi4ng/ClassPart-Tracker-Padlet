# 📝 Padlet Class Participation Tracker

This Python script automates the process of recording and calculating class participation (CP) scores from Padlet post exports. Designed for educators and teaching assistants, it streamlines class participation tracking and ensures fair scoring by counting each student's contributions only once per session/question.

## 💡 Features

- Download Padlet csv zipfiles into `add_zipfiles_here`.
- Automatically process and scans the `add_zipfiles_here` directory for Posts `.csv` exports from Padlet.
- Extracts student names from the `Author` column.
- Adds or updates each student's CP score in `cp.csv`.
- Prevents duplicate counting using a tracking mechanism.
- Displays a clean table of participation scores.
- Resets `add_zipfiles_here` directory and `cp.csv` using `reset.py`.

## 📁 Folder Structure

<pre>project-folder/ 
├── add_zipfiles_here/   # Place all Padlet .csv zipfiles exports here 
├── cp.csv               # Automatically generated/updated CP record 
├── reset.py             # Script to reset application for new session/lesson
└── tracker.py           # Script with core functionality </pre>


## 🚀 Getting Started

1. **Install Dependencies**  
   Requires `pandas`, which can be installed via pip:
   `pip install pandas`

2. **Add CSV Files**
    Export Padlet posts as csv into the `add_zipfiles_here` folder.

3. **Run the Script**
    `python tracker.py`

4. **View Results**
    The CP scores will be printed in table format and stored in `cp.csv`.

4. **New Day**
    Run `python reset.py` when you are ready to begin a new session/lesson.


## 📌 Notes
- To avoid PermissionError: [WinError 5], run this project from a local drive (e.g., C:\) instead of a OneDrive folder.
- Students are uniquely identified by the name in the Author field.
- Duplicate entries within a file are ignored to avoid inflation.
- Initial participation grants 1 CP; subsequent entries increase their score cumulatively.


## 🛠️ Potential Enhancements
- Auto save each lesson's Class Participation record in a new file.
- Log errors or failed reads to a debug file.
- Add support for unique student IDs to avoid name collisions.
- Introduce a GUI for ease of use.


## Created by Lau to simplify classroom participation tracking. 📚✨

## Let me know if you want to tweak this for a more technical audience, include screenshots, or add contribution guidelines—it’s your masterpiece, I’m just polishing it. 😄


