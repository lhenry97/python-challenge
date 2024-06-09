# import os module to create file path across operating systems
import os

#import module for reading CSV files
import csv

#create variable to hold location of csv
csvpath = os.path.join('Resources', 'election_data.csv')

#create list to hold each column
ballot_id = []
county = []
candidate = []

#create list to hold a single instance of each candidate
candidatelist = []

#Print header
print("")
print(f"Election Results")
print("")
print("-------------------------------")
print("")

#read the csv file
with open(csvpath) as csvfile:
    
     #specifys comma as delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first
    csv_header = next(csvreader)
    
    #read each row of data after header
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    #get number of votes
    totalvotes = len(ballot_id)
    print(f"Total Votes: {totalvotes}")
    print("")
    print("-------------------------------")
    print("")

    #identify the candidates
    for row in candidate:
        if (row not in candidatelist):
            #add new candidate to list
            candidatelist.append(row)
    
    #assign candidates to their own variable
    candidate_one = candidatelist[0]
    candidate_two = candidatelist[1]
    candidate_three = candidatelist[2]
    
    #initalise candidate tallys for each to zero
    can_one_total = 0
    can_two_total = 0
    can_three_total = 0

    #count the total votes for each candidate
    for row in candidate:
        if (candidate_one == row):

            can_one_total += 1

        elif (candidate_two == row):

            can_two_total += 1

        elif (candidate_three == row):

            can_three_total += 1
    
    #calculate percentage of votes and round to three decimal places
    can_one_percent = round((can_one_total / totalvotes) * 100,3)
    can_two_percent = round((can_two_total / totalvotes) * 100,3)
    can_three_percent = round((can_three_total / totalvotes) * 100,3)


    #print percentage and total votes
    print(f"{candidate_one}: {can_one_percent}% ({can_one_total})")
    print("")
    print(f"{candidate_two}: {can_two_percent}% ({can_two_total})")
    print("")
    print(f"{candidate_three}: {can_three_percent}% ({can_three_total})")
    print("")
    print("-------------------------------")
    print("")

    #if statement to identify the winner
    if (can_one_percent > can_two_percent and can_one_percent > can_three_percent):
        winner = candidate_one
    elif (can_two_percent > can_one_percent and can_two_percent > can_three_percent):
        winner = candidate_two
    elif (can_three_percent > can_one_percent and can_three_percent > can_two_percent):
        winner = candidate_three

    #print the winner
    print(f"Winner: {winner}")
    print("")
    print("-------------------------------")
    print("")

    #create text file containg polling results
    text_path = "PyPoll_Polling_Results.txt"
    with open(text_path, 'w') as file:
        #write content to file
        file.write("\n")
        file.write(f"Election Results\n")
        file.write("\n")
        file.write("--------------------------------\n")
        file.write("\n")
        file.write(f"Total Votes: {totalvotes}\n")
        file.write("\n")
        file.write("--------------------------------\n")
        file.write("\n")
        file.write(f"{candidate_one}: {can_one_percent}% ({can_one_total})\n")
        file.write("\n")
        file.write(f"{candidate_two}: {can_two_percent}% ({can_two_total})\n")
        file.write("\n")
        file.write(f"{candidate_three}: {can_three_percent}% ({can_three_total})\n")
        file.write("\n")
        file.write("--------------------------------\n")
        file.write("\n")
        file.write(f"Winner: {winner}\n")
        file.write("\n")
        file.write("--------------------------------\n")
        file.write("\n")
