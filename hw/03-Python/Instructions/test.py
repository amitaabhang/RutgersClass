import os
import csv


election_csv = os.path.join("Resources", "election_data.csv")

candidates =[]
vote_dict ={}

print(candidates)
total_votes = 0

with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
    csv_header = next(csv_reader)
    print(csv_header)
    
    #data = list(csv_reader) 
    
    #Make lists
    for row in csv_reader:
        total_votes = total_votes +1
        
        if(row[2] not in candidates):
            candidates.append(str(row[2]))
            vote_dict[row[2]] =0

        vote_dict[row[2]] += 1

    print(vote_dict)
    
    Khan_votes = vote_dict["Khan"]
    Correy_votes = vote_dict["Correy"]
    Li_votes = vote_dict["Li"]
    OTooley_votes = vote_dict["O'Tooley"]

    maxVotes=0
    for candidate, votes in vote_dict.items():
        if votes > maxVotes:
            maxVotes = votes
            winner = candidate
    
    print(total_votes)
    print(winner)
   
    output = f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    Khan: {(Khan_votes/total_votes)*100:.3f}%  ({Khan_votes})
    Correy: {(Correy_votes/total_votes)*100:.3f}% ({Correy_votes})
    Li: {(Li_votes/total_votes)*100:.3f}%  ({Li_votes})
    O'Tooley: {(OTooley_votes/total_votes)*100:.3f}% ({OTooley_votes})
    -------------------------
    Winner: {winner}
    -------------------------
    """
    print(output)
  

    