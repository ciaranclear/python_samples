import csv


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # generator steps over first line ie the headers

    for line in csv_reader:
        print(line)
        print(line[2])


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # writing to a csv file
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-') # delimeter defaults t>

        for line in csv_reader:
            csv_writer.writerow(line)


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['email'])


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('other_new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
           del line['email']
           csv_writer.writerow(line)

