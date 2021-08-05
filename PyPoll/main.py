# Python script for analysing the financial records of a company
# Requirements
# The total number of votes cast. Done
# A complete list of candidates who received votes. Identified
# The percentage of votes each candidate won
# The total number of votes each candidate won. Identified
# The winner of the election based on popular vote. Done

import os
import csv

# Define path of source file

election_csv = os.path.join("PyPoll","Resources","election_data.csv")

# Not sure if I'm going to need this but will create it now anyway

def election_stats(row):
    vid = row[0]
    county = row [1]
    candidate = row[2]

# read the file

with open(election_csv,"r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# define some variables and a list

    count = 0
    total = 0
    candidate = ""
    candidate_list = []

# Need to skip first row as it is the header
# The next section performs an initial scan of the file looking for votes cast & candidates

    csv_header = next(csvreader)

    for row in csvreader:

            count += 1

            candidate = row[2]

            # only want unique candidates - the next line is adding every record because I don't 
            # know how many candidates there are but will filter that shortly

            candidate_list.append(candidate)

    # This next line creates a set of unique values and then creates a list
    
    unique_candidates = list(set(candidate_list))

    print("")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")

    # Next is to use this list to run a count of how many votes each received and create another list to zip together
    # The file will be scanned multiple times, once for each candidate

    vote_tally = []
    winner = ""
    vote_count_old = 0

    for name in unique_candidates:
        
        vote_count = 0

        with open(election_csv,"r") as csvfile:

            csvreader = csv.reader(csvfile, delimiter=',')

            for row in csvreader:
                if row[2] == name:
                    vote_count += 1
       
        vote_tally.append(vote_count)
        percentage = round(vote_count/count*100,3)

        print(f"{name}: {percentage}% ({vote_count})")

        if vote_count > vote_count_old:
            vote_count_old = vote_count
            winner = name

    # Next step is to zip the two lists together, calculate percentages & report results 
    # Preferably ordered highest to lowest
 
# print(unique_candidates)
# print(vote_tally)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
