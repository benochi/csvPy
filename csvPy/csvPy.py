import csv

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tAge:{row[1]} \nexperience:{row[2]} \nindustry:{row[3]} \njob title:{row[4]} \ncompany:{row[5]} \neducation:{row[6]} \nState:{row[7]} \nAnnual Base Salary:{row[9]} \nAnnual Bonus:{row[10]} Annual Average of RSUs: {row[11]}')
            val1 = {row[9]}
            val2 = {row[10]}
            val3 = {row[11]}
            print(val1)
            line_count += 1
    print(f'Processed {line_count} lines.')
