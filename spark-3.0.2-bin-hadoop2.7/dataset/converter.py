import csv

with open('movies.dat') as dat_file, open('movies.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    for line in dat_file:
        row = [field.strip() for field in line.split('\t')]
        csv_writer.writerow(row)