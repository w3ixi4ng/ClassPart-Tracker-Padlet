# 📝 Padlet Class Participation Tracker

This Python script automates the process of recording and calculating class participation (CP) scores from Padlet post exports. Designed for educators and teaching assistants, it streamlines class participation tracking and ensures fair scoring by counting each student's contributions only once per session/question.

## 💡 Features

- Automatically scans the `add_post_here` directory for `.csv` exports from Padlet.
- Extracts student names from the `Author` column.
- Adds or updates each student's CP score in `cp.csv`.
- Prevents duplicate counting using a tracking mechanism.
- Displays a clean table of participation scores.

## 📁 Folder Structure

project-folder/ 
├── add_post_here/       # Place all Padlet .csv exports here 
├── cp.csv               # Automatically generated/updated CP record 
└── padlet_reader.py     # Script with core functionality


## 🚀 Getting Started

1. **Install Dependencies**  
   Requires `pandas`, which can be installed via pip:
   `pip install pandas`

2. **Add CSV Files**
    Export Padlet posts as .csv 
    Unzip the folder, rename (if necessary) and move only the Posts `.csv` inside the `add_post_here` folder.

3. **Run the Script**
    `python padlet_reader.py`

4. **View Results**
    The CP scores will be printed in table format and stored in `cp.csv`.


## 📌 Notes
- Manual unzipping and moving of `.csv` files is required.
- Students are uniquely identified by the name in the Author field.
- Duplicate entries within a file are ignored to avoid inflation.
- Initial participation grants 1 CP; subsequent entries increase their score cumulatively.


## 🛠️ Potential Enhancements
- Automatically unzip files and process only post `.csv`.
- Log errors or failed reads to a debug file.
- Add support for unique student IDs to avoid name collisions.
- Introduce a GUI for ease of use.


## Created by Lau to simplify classroom engagement tracking. 📚✨

## Let me know if you want to tweak this for a more technical audience, include screenshots, or add contribution guidelines—it’s your masterpiece, I’m just polishing it. 😄


