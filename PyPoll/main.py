# Python script for analysing the financial records of a company

import os
import csv

# Define path of source file

election_csv = os.path.join("PyPoll","Resources","election_data.csv")


def election_stats(row):
    vid = row[0]
    county = row [1]
    candidate = row[2]

# read in the file

with open(election_csv,"r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# define some variables and find the total number of months in the data set

    count = 0
    total = 0
    candidate = ""
    candidate_list = []

# Need to skip first row as it is the header

    csv_header = next(csvreader)

    for row in csvreader:

            count += 1

            candidate = row[2]

            # only want unique candidates - this is adding everything but will filter that later

            candidate_list.append(candidate)

    
    unique_candidates = list(set(candidate_list))
      
   

    # The above returned the hoped for result. Next is to use this list to run a count of 
    # how many votes each received and create another list to zip together


# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


    vote_tally = []

    for name in unique_candidates:
        
        vote_count = 0

        with open(election_csv,"r") as csvfile:

            csvreader = csv.reader(csvfile, delimiter=',')
   

            for row in csvreader:
                if row[2] == name:
                    vote_count += 1
       
        vote_tally.append(vote_count)

        


print("Election Results")
print("-------------------------")
print(f"Total Votes: {count}")
print("-------------------------")
print(unique_candidates)
print(vote_tally)
print("-------------------------")
print(f"Winner: ")
print("-------------------------")
