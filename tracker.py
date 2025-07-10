import pandas as pd
import os
import zipfile


def process_csv(results_file, filepath):
    # read post csv file, getting only students' name
    try: 
        df = pd.read_csv(filepath)
        students  = df['Author']
    except Exception as error:
        print(f"Skipping file: {filepath} due to {error}")
        return

    # second post.csv load onwards
    if os.path.exists(results_file):
        cp_dict = {}

        # get all students' name and cp in a dict
        with open(results_file, 'r') as records:
            for record in records:
                record = record.rstrip()
                name, cp = record.split(',')
                cp_dict[name] = cp

        # ensure all current and new students participating are recorded and only recorded once
        recorded = set()
        for student in students:
            if student not in recorded:
                if student in cp_dict:
                    # participated students
                    cp_dict[student] = int(cp_dict[student]) + 1
                else:
                    # new participation
                    cp_dict[student] = 1
            recorded.add(student)
        
        # write back into csv file
        with open(results_file, 'w') as records:
            for name, cp in cp_dict.items():
                records.write(f"{name},{cp}\n")

    # first Posts .csv load - students only gain 1 CP and only recorded once
    else:
        recorded = set()
        with open(results_file, 'w') as records:
            for student in students:
                if student not in recorded:
                    records.write(student  + ",1" + "\n")
                recorded.add(student)


def process_files(zip_files_folder, results_file):
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
                    process_csv(results_file, filepath)


def table(results_file):
    results = pd.read_csv(results_file, header=None, names=['Name', 'CP'])
    print(results)



def main():
    results_file = 'cp.csv'
    zip_files_folder = 'add_zipfiles_here'

    # process zipfiles and its corresponding Posts .csv file
    process_files(zip_files_folder, results_file)

    # final call to show results
    table(results_file)


if __name__ == "__main__":
    main()