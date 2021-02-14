# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")


# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    Movie_Found= False
    i=0
     # Read each row of data after the header
    for row in csvreader:
       if(row[i] == video):
        print(row[i] + row[i+1] + row[i+2])
        Movie_Found= True
        break

    if(Movie_Found is  False):
        print("Movie not found")
