# Python script for analysing the financial records of a company
# Requirements
# The total number of votes cast. Done
# A complete list of candidates who received votes. Done
# The percentage of votes each candidate won. Done
# The total number of votes each candidate won. Done
# The winner of the election based on popular vote. Done

import os
import csv

# Define path of source file

election_csv = os.path.join("PyPoll","Resources","election_data.csv")

# Define location and name for output file

PyPollAnalysis = os.path.join("PyPoll","analysis","PyPoll_Out.txt")

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

    # print the results summary thus far and start writing the output file

    print("")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")

    with open (PyPollAnalysis,'w') as f:
        f.write("Election Results" + "\n")
        f.write("----------------------------" + "\n")
        f.write("Total Votes: " + str(count) + "\n")
        f.write("----------------------------" + "\n")


    # Next is to use the unique_candidates list to run a count of how many votes each received and create another list to zip 
    # together if needed
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
        percentage = (vote_count/count*100)

        # print the result with percentage reported to 3 decimal places

        print(f"{name}: {percentage:.3f}% ({vote_count})")

        # write the same record to the output file.

        with open (PyPollAnalysis,'a') as f:
            f.write((name) + ": " + str("{0:.3f}".format(percentage)) +"% (" + str((vote_count)) +")" + "\n")

        if vote_count > vote_count_old:
            vote_count_old = vote_count
            winner = name

# Next two lines were used initially to check code logic
# print(unique_candidates)
# print(vote_tally)

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open (PyPollAnalysis,'a') as f:
    f.write("-------------------------" + "\n")
    f.write("Winner: " + (winner) + "\n")
    f.write("-------------------------" + "\n")