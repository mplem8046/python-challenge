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
