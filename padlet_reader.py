import pandas as pd
import os

def auto_cp(results_file, filepath):
    # read post csv file, getting only students' name
    try: 
        df = pd.read_csv(filepath)
        students  = df['Author']
    except:
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

    # first post.csv load - students only gain 1 CP and only recorded once
    else:
        recorded = set()
        with open(results_file, 'w') as records:
            for student in students:
                if student not in recorded:
                    records.write(student  + ",1" + "\n")
                recorded.add(student)

def table(results_file):
    results = pd.read_csv(results_file, header=None, names=['Name', 'CP'])
    print(results)


def main():
    results_file = 'cp.csv'

    # dynamically read all csv files in folder
    for filename in os.listdir("add_post_here"):
        if filename.endswith('.csv'):
            filepath = os.path.join("add_post_here", filename)
            auto_cp(results_file, filepath)

    table(results_file)

if __name__ == "__main__":
    main()





