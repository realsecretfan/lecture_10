import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode = "r") as csv_file:
        data = {}
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key, value in row.items():
                if not key in data:
                    data[key] = []
                data[key].append(value)
    return data

def selection_sort():


def main():
    read_data("numbers.csv")


if __name__ == '__main__':
    main()
