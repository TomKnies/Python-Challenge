import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

# Things I want to find
total_votes = 0

# list of candidates
# votes per candidate
# percent of total vote by candidate
# election winner





with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)