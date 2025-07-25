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
   Requires `pandas`, which can be installed via pip: `pip install pandas`

3. **Add CSV Files**  
   Export Padlet posts as csv and download it into the `add_zipfiles_here` folder.    
   Note: Padlet zipfiles might have the same filename. To avoid overwriting, rename each zipfile before downloading them into the folder (e.g., q1.zip, q2.zip, etc.).
   
5. **Run the Script**  
   Execute the main script using `python tracker.py`

7. **View Results**  
   The Class Participation (CP) scores will be printed in a table format and saved in `cp.csv`.

4. **New Day**  
   When starting a new session/lesson, reset the folder and data using `python reset.py`.


## 📌 Notes
- Manually track participation when students are unable to post on Padlet.
- Duplicate entries within a file are ignored to avoid inflation (e.g., when posting on behalf of classmates).
- To avoid PermissionError: [WinError 5], run this project from a local drive (e.g., C:\) instead of a OneDrive folder.
- Download ALL zipfiles into `add_zipfiles_here` directory before running script.
- Students are uniquely identified by the name in the Author field.
- Initial participation grants 1 CP; subsequent entries increase their score cumulatively.


## 🛠️ Potential Enhancements
- Auto save each lesson's Class Participation record in a new folder.
- Implement automated detection of student names in post content to track participation when posts are made using a friend's account.
- Log errors or failed reads to a debug file.
- Add support for unique student IDs to avoid name collisions.
- Introduce a GUI for ease of use.


## Created by Lau to simplify classroom participation tracking. 📚✨

## Let me know if you want to tweak this for a more technical audience, include screenshots, or add contribution guidelines—it’s your masterpiece, I’m just polishing it. 😄


