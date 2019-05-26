import csv


with open("movies.csv", "r") as fp:
    # ak pouzijeme DictReader dostaneme dictionary, s ktorym sa da pracovat
    # ak pouzijeme reader, dostaneme array s ktorym vieme pracovat ako v pripade file_reader.py
    # vsetko ostatne zostava ako pri priklade file_reader
    csv_file = csv.DictReader(fp)
    for line in csv_file:
        print(line)

# zapisanie file,  je presne to iste ako v pripade file_reader.py
