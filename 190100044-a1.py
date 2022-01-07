import os
import csv


# ### Initialize ### #
def find_files():
    # Get the current working directory
    cwd = os.path.dirname(os.path.realpath(__file__))

    # Get the files in the directory
    files = os.listdir(os.path.join(cwd, 'csv-files'))

    return files


def setup():
    files = find_files()

    tables = {}
    for file in files:
        table = {}

        # Open the file
        with open(os.path.join('csv-files', file), 'r') as f:
            reader = csv.reader(f)

            # Get the header row
            table['header'] = next(reader)

            # Store the data
            table['data'] = list(reader)

        tables[file[:-4]] = table

    return tables
