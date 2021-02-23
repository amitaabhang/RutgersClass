import os
import csv


election_csv = os.path.join("Resources", "election_data.csv")

candidates =[]


with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
    csv_header = next(csv_reader)
    data = list(csv_reader) 
    
    #Make lists
    for row in data:
        if(row[0] != " " and row[1] != " " and row[2] != " "):
            if(row[2] not in candidates):
                candidates.append(str(row[2]))
    
    candidates = candidates.lower()
    print(candidates)
    vote_count = []
    for candidate in candidates:
        vote_count.append(0)

    print(vote_count)
    print(candidates)
    #print(candidates.index('khan'))
    
    #x=0
    #for x in range(0,10):
        #vote_count[0] +=1

    #for row in data:
        #indexofcandidate = candidates.index(row[2])
        #vote_count[indexofcandidate] +=1
    
    #print(vote_count)
    #print(len(vote_count))