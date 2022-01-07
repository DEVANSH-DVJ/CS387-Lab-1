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


# ### Queries ### #
def q1a(query, tables):
    table = query.split('from')[1].strip()
    res = tables[table]['data']

    return res


def q1b(query, tables):
    table = query.split('from')[1].split('where')[0].strip()
    column = query.split('where')[1].split('=')[0].strip()
    value = query.split('where')[1].split('=')[1].strip().strip('\'')

    col_no = tables[table]['header'].index(column)

    res = []
    for row in tables[table]['data']:
        if row[col_no] == value:
            res.append(row)

    return res


def q1c(query, tables):
    column_list = query.split('select')[1].split('from')[0].split(',')
    table = query.split('from')[1].split('where')[0].strip()
    main_column = query.split('where')[1].split('=')[0].strip()
    value = query.split('where')[1].split('=')[1].strip().strip('\'')

    col_no_list = []
    for column in column_list:
        col_no_list.append(tables[table]['header'].index(column.strip()))
    main_col_no = tables[table]['header'].index(main_column)

    res = []
    for row in tables[table]['data']:
        if row[main_col_no] == value:
            sel = []
            for col_no in col_no_list:
                sel.append(row[col_no])
            res.append(sel)

    return res


def q2(query, tables):
    res = query

    return res


def q3(query, tables):
    table = query.split('from')[1].split('where')[0].strip()
    column = query.split('where')[1].split('=')[0].strip()
    value = query.split('where')[1].split('=')[1].strip().strip('\'')

    col_no = tables[table]['header'].index(column)

    res = 0
    for row in tables[table]['data']:
        if row[col_no] == value:
            res += 1

    return res


def q4(query, tables):
    res = query

    return res


def q5(query, tables):
    res = query

    return res


# ### Helper functionalities ### #
def clean(query):
    query = query.strip()
    if query[-1] == ';':
        return query[:-1].strip()
    return query


def output(res):
    print(res)


if __name__ == '__main__':
    tables = setup()

    while(True):
        qtype = input('Query Type? ').strip()

        if qtype == '0':
            print('exiting...')
            exit(0)

        if qtype == '1a':
            query = clean(input('Enter your query: '))
            output(q1a(query, tables))
        elif qtype == '1b':
            query = clean(input('Enter your query: '))
            output(q1b(query, tables))
        elif qtype == '1c':
            query = clean(input('Enter your query: '))
            output(q1c(query, tables))
        elif qtype == '2':
            query = clean(input('Enter your query: '))
            output(q2(query, tables))
        elif qtype == '3':
            query = clean(input('Enter your query: '))
            output(q3(query, tables))
        elif qtype == '4':
            query = clean(input('Enter your query: '))
            output(q4(query, tables))
        elif qtype == '5':
            query = clean(input('Enter your query: '))
            output(q5(query, tables))
