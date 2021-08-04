# Python script for analysing the financial records of a company

import os
import csv

# Define path of source file

budget_csv = os.path.join("PyBank","Resources","budget_data.csv")


def budget_stats(row):
    month = row[0]
    prof_loss = int(row [1])

# read in the file

with open(budget_csv,"r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# define some variables and find the total number of months in the data set

    count = 0
    total = 0
    delta = 0
    sum_delta = 0
    old_val = 0
    old_loss_month = ""
    old_prof_month = ""
    old_loss = 0
    old_prof = 0
    delta_list = []

# Need to skip first row as it is the header

    csv_header = next(csvreader)

# Need also to count only the rows where the month is not null.

    for row in csvreader:
        if row[0] != "":

            count += 1
# set the first found date value to initialize the value of the held max profit & loss months.
# This is subsequently updated based upon the following two if statements.

            if count == 1:
                old_loss_month = row[0]
                old_prof_month = row[0]
                delta_list = [0]

                    
            total = total + int(row[1])

            if count >= 2:
                delta = int(row[1]) - int(old_val) 
                delta_list.append(int(delta))

            # print(delta)

            # Initialize or append to a list for the deltas??
                             
            # sum_delta = sum_delta + delta

            # print(f"Sum delta {sum_delta} Delta  {delta}")

# The greatest decrease in profits (date and amount) over the entire period. Compare monthly deltas
# If lesser update variables - month and current delta

            if delta < old_loss:
                old_loss = delta
                old_loss_month = row[0]
            
# Find the greatest increase in profits date and amount over the entire period. Compare monthly deltas
# If greater update variables - month and current delta


            if delta > old_prof:
                old_prof = delta
                old_prof_month = row[0]

            old_val = int(row[1])


    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")

# Net amount of total profit and losses in the entire period

    print(f"Total: ${total}")

    
# Calculate the changes month to month of profit and losses over 
# the entire period and then calculate the average of those. Possibly create a list and append
# the monthly delta then divide by the length of the list??

# This was not working properly, something wrong with the calc of sum_delta. 
# Fixed on line 55 - was including line one invalid calc

    avg_delta = round(sum(delta_list)/(len(delta_list)-1),2)

    # avg_delta =- round(sum_delta / count,2)

    print(f"Average Change :${avg_delta}")
    # print(f"Sum delta : ${sum_delta}")
    # print(f"Final delta {delta}")


    print(f"Greatest Increase in Profits: {old_prof_month} (${old_prof})")
    print(f"Greatest Decrease in Profits: {old_loss_month} (${old_loss})")


# final script should both print the analysis to the terminal and export 
# a text file with the results

# Define the path of the output file

PyBankAnalysis = os.path.join("PyBank","analysis","PyBank_Out.txt")

with open (PyBankAnalysis,'w') as f:

    f.write("Financial Analysis" + "\n")
    f.write("----------------------------" + "\n")
    f.write("Total Months: " + str(count) + "\n")
    f.write("Total: $" + str(total) + "\n")
    f.write("Average Change: $" + str(avg_delta) + "\n")
    f.write("Greatest Increase in Profits: " + old_prof_month + "($" + str(old_prof) +")" + "\n")
    f.write("Greatest Decrease in Profits: " + old_loss_month + "($" + str(old_loss) +")" + "\n")


