import os
import csv

file_path = os.path.join("Resources","cereal_bonus.csv")

with open(file_path) as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    #header = next(reader)
    for row in reader:
        if(float(row[7]) >= 5):
            print(row)

