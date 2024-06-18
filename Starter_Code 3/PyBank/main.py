# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "budget_data.csv")

#Set Lists
date = []
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999999]
net_total = 0
average_change_list = []

# # Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    
    
       # Loop to add all months
    for row in csvreader:
        total_months =+ 1
        net_total += int(row[1])


        net_change = int(row[1])- prev_net
        prev_net = int(row[1])
        net_change_list  += [net_change]
        date += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
       
        if net_change > greatest_decrease[1]:
            greatest_decrease [0] = row[0]
            greatest_decrease[1] = net_change


print("net change"+ str(net_change) )
print
        

