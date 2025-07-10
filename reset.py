import shutil
import os

# resets folder for new lesson
def main():
    folder_name = 'add_zipfiles_here'
    results_file = 'cp.csv'

    # remove the content of the folder
    for filename in os.listdir(folder_name):
        try:
            file_path = os.path.join(folder_name, filename)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
        except Exception as error:
            print(f"Failed to delete file: {file_path} due to {error}")

    # remove results file
    if os.path.exists(results_file):
        os.remove(results_file)

if __name__ == '__main__':
    main()