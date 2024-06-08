# import os module to create file path across operating systems
import os

#import module for reading CSV files
import csv

#create variable to hold location of csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#create lists to hold the data
dates=[]
profitlosslist=[]
change_profitlosslist=[]

#create variable to hold profit/loss value
profitloss = 0

#create variables to hold change values
previous_pl = 0
current_pl = 0
change_pl = 0
averagechange = 0
total_change = 0
#print intro
print("")
print("Financial Analysis")
print("")
print("--------------------------------")
print("")

#read the csv file
with open(csvpath) as csvfile:

    #specifys comma as delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first
    csv_header = next(csvreader)

    #read each row of data after the header
    for row in csvreader:
        dates.append(row[0])
        profitlosslist.append(row[1])

    #print total amount of months as by printing length of list as each row is a different month
    print(f"Total Months: {len(dates)}")
    print("")
    
    #get length of list of profitloss list
    list_length=len(profitlosslist)

    #for loop to calculate total profit/loss
    for row in range(list_length):
        profitloss=profitloss + int(profitlosslist[row])

    print(f"Total: ${profitloss}")
    print("")

    #remove the first data point from list
  

    #for loop to create new list containing change
    for row in range(list_length):
        previous_pl = int(profitlosslist[row-1])
        current_pl = int(profitlosslist[row])
        change_pl = current_pl - previous_pl
        change_profitlosslist.append(change_pl)
    
    #remove first value as cannot get change from data that is not there
    change_profitlosslist.remove(change_profitlosslist[0])

    #find average of change in profit/loss
    change_list_length=len(change_profitlosslist)

    for row in range(change_list_length):
        total_change = total_change + int(change_profitlosslist[row])
    
    averagechange = total_change / change_list_length

    print(f"Average Change: ${averagechange}")
