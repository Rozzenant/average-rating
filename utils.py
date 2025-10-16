import csv


def read_csv_files(file_paths):
    data = []
    for path in file_paths:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data.extend(list(reader))
    return data
