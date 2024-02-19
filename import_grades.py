import csv
from collections import defaultdict

grades = defaultdict(int)
def scan_csv(file_path):
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip header if present
            next(csv_reader, None)
            for row in csv_reader:
                email = row[1]
                username = email.split('@')[0].lower()
                grade = float(row[2]) if row[2] != 'null' else 0
                grades[username] += grade
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)

def write_csv(write_path):
    try:
        with open(write_path, 'r', newline='') as file:
            rows = list(csv.reader(file))

        for row in rows:
            if row[2] in grades:
                row[-1] = grades[row[2]]
        print(rows)

        with open(write_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    # Example usage
    file_path = "Test1.csv"  # Change this to your CSV file path
    write_path = "Write.csv" # Change this to your desired output file path
    scan_csv(file_path)
    write_csv(write_path)