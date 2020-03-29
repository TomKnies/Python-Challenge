import os
import csv
import operator

election_csv = os.path.join("..", "Resources", "election_data.csv")

# Things I want to find
total_votes = 0

# list of candidates
# votes per candidate
candidate_votes = {}
# percent of total vote by candidate
# election winner

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# python read that data and tell it what each column is
    for row in csvreader:
        id = row[0]
        county = row[1]
        candidate = row[2]

# overall votes simple enough since python counts adds 1 to the starting 0 for each row
        total_votes += 1
        
# votes per candidate gettin stored up
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# I can see winners and calculate on my own, but we gotta teach python how to do it
winner = max(candidate_votes.items(), key = operator.itemgetter(1))[0]

# Might be too much user input but there are only 4 candidates and they're all easy to reference keys
# in my dictionary.  Might as well make use of that.
Khan_vote = candidate_votes["Khan"]
Correy_vote = candidate_votes["Correy"]
Li_vote = candidate_votes["Li"]
OT_vote = candidate_votes["O'Tooley"]

# write it up pretty and show it off
analysis = (
    f"Election Results\n"
    f"------------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------------------\n"
    f"Khan: %{round(Khan_vote/total_votes*100)} ({Khan_vote})\n"
    f"Correy: %{round(Correy_vote/total_votes*100)} ({Correy_vote})\n"
    f"Li: %{round(Li_vote/total_votes*100)} ({Li_vote})\n"
    f"O'Tooley: %{round(OT_vote/total_votes*100)} ({OT_vote})\n"
    f"------------------------------------\n"
    f"Winner: {winner}"
)
print(analysis)

# then set it to a new text document
output_file = os.path.join("Election_Analysis.csv")

with open("Election_Analysis.csv", "w") as text_file:
    print(f"{analysis}", file=text_file)
