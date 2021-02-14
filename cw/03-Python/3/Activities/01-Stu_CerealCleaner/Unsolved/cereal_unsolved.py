import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

# Open and read csv
with open(cereal_csv) as csv_file:
    csv_reader =  csv.reader(csv_file)
    header = next(csv_reader)
    i=0
    for row in csv_reader:
        if(float(row[7])>=5):
            print(row)

