import os
import csv


def dataReader(filename):
    list = []
    base_path = os.path.dirname(__file__)
    path = base_path.replace('func', 'testdata/' + filename)
    with open(path, encoding='gbk') as file:
        table = csv.reader(file)
        i = 0
        for row in table:
            if i == 0:
                pass
            else:
                list.append(row)
            i = i + 1

    return list
