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
    table1 = query.split('from')[1].split('where')[0].split(',')[0].strip()
    table2 = query.split('from')[1].split('where')[0].split(',')[1].strip()
    column1 = query.split('where')[1].split('=')[0].split('.')[1].strip()
    column2 = query.split('where')[1].split('=')[1].split('.')[1].strip()

    col1_no = tables[table1]['header'].index(column1)
    col2_no = tables[table2]['header'].index(column2)

    res = []
    for row1 in tables[table1]['data']:
        for row2 in tables[table2]['data']:
            if row1[col1_no] == row2[col2_no]:
                res.append(row1 + row2)

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
    column_list = query.split('select')[1].split('from')[0].split(',')
    table = query.split('from')[1].split('group by')[0].strip()
    column = query.split('group by')[1].strip()

    if column_list[0].strip() == column:
        subtype = 0
        colX = column_list[1].split('sum')[1].strip().strip('()').strip()
    else:
        subtype = 1
        colX = column_list[0].split('sum')[1].strip().strip('()').strip()

    col_no = tables[table]['header'].index(column)
    colX_no = tables[table]['header'].index(colX)

    groups = {}
    for row in tables[table]['data']:
        if row[col_no] in groups.keys():
            groups[row[col_no]] += int(row[colX_no])
        else:
            groups[row[col_no]] = int(row[colX_no])

    res = []
    for key in sorted(groups.keys()):
        if subtype == 0:
            res.append([key, groups[key]])
        else:
            res.append([groups[key], key])

    return res


def q5(query, tables):
    column_list = query.split('select')[1].split('from')[0].split(',')
    table = query.split('from')[2].split('where')[0].strip()
    column1 = query.split('where')[1].split('=')[0].strip()
    value1 = query.split('where')[1].split('=')[1].strip().strip(')').strip().strip('\'')
    column2 = query.split('where')[2].split('=')[0].strip()
    value2 = query.split('where')[2].split('=')[1].strip().strip('\'')

    col_no_list = []
    for column in column_list:
        col_no_list.append(tables[table]['header'].index(column.strip()))
    col1_no = tables[table]['header'].index(column1)
    col2_no = tables[table]['header'].index(column2)

    residue = []
    for row in tables[table]['data']:
        if row[col1_no] == value1:
            residue.append(row)

    res = []
    for row in residue:
        if row[col2_no] == value2:
            sel = []
            for col_no in col_no_list:
                sel.append(row[col_no])
            res.append(sel)

    return res


# ### Helper functionalities ### #
def clean(query):
    query = query.strip()
    if query[-1] == ';':
        return query[:-1].strip()
    return query


def output(res):
    for row in res:
        for iter in range(len(row) - 1):
            print(row[iter], end=',')
        print(row[-1])


if __name__ == '__main__':
    tables = setup()

    while(True):
        qtype = input('Query Type? ').strip()

        if qtype == '0':
            print('exiting...')
            break

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
            print(q3(query, tables))
        elif qtype == '4':
            query = clean(input('Enter your query: '))
            output(q4(query, tables))
        elif qtype == '5':
            query = clean(input('Enter your query: '))
            output(q5(query, tables))
