import pandas as pd
import os
import zipfile


def process_csv(cp_dict, filepath):
    # read post csv file, getting only students' name
    try: 
        df = pd.read_csv(filepath)
        students  = df['Author']
    except Exception as error:
        print(f"Skipping file: {filepath} due to {error}")
        return

    # ensure all current and new students participating are recorded and only recorded once
    recorded = set()
    for student in students:
        if student not in recorded:
            if student in cp_dict:
                # participated before students
                cp_dict[student] = int(cp_dict[student]) + 1
            else:
                # new participation
                cp_dict[student] = 1
        recorded.add(student)


def process_files(zip_files_folder, cp_dict):
    # dynamically unzip the zipfiles and process only the Post csv
    for zip_filename in os.listdir(zip_files_folder):
        if zip_filename.endswith('.zip'):
            zip_path = os.path.join(zip_files_folder, zip_filename)
            extract_path = os.path.join(zip_files_folder, zip_filename.replace(".zip", ""))
            # extract zipfile
            with zipfile.ZipFile(zip_path, 'r') as zip_file:
                zip_file.extractall(extract_path)

            # once extracted, find the Posts csv and process it
            for filename in os.listdir(extract_path):
                if filename.startswith("Posts") and filename.endswith(".csv"):
                    # call process_csv to process every Posts .csv file
                    filepath = os.path.join(extract_path, filename)
                    process_csv(cp_dict, filepath)


def table(results_file):
    results = pd.read_csv(results_file, header=None, names=['Name', 'CP'])
    print(results)



def main():
    results_file = 'cp.csv'
    zip_files_folder = 'add_zipfiles_here'
    cp_dict = {}

    # process zipfiles and its corresponding Posts .csv file
    process_files(zip_files_folder, cp_dict)

    with open(results_file, 'w') as f:
        for name, cp in cp_dict.items():
            f.write(f"{name},{cp}\n")


    # final call to show results
    if os.path.exists(results_file) and cp_dict:
        table(results_file)
    else:
        print(f"No data. Add Padlet csv zipfiles in {zip_files_folder} to proceed.")


if __name__ == "__main__":
    main()