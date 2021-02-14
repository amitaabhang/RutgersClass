import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

wrestler_data = {
    "Name":[],"Won":[],"Lost":[],"Draw":[]
}

# Define the function and have it accept the 'wrestlerData' as its sole parameter

# Find the total number of matches wrestled

# Find the percentage of matches won

# Find the percentage of matches lost

# Find the percentage of matches drawn

# Print out the wrestler's name and their percentage stats

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        wrestler_data["Name"].append(row[0])
        wrestler_data["Won"].append(row[1])
        wrestler_data["Lost"].append(row[2])
        wrestler_data["Draw"].append(row[3])

    #print(wrestler_data["Draw"])
    

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for v in wrestler_data["Name"]:
        #print(k[0])
        print(v)
        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        for name in v:
            if(name_to_check == name):
                print("Found the name")
            #print_percentages(row)

