# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..","Resources", "election_data.csv")

#total number of votes cast
#a complete list of candidates who received votes
#count each row of row[0]

#a complete list of candidates who received votes
#a unique list of candidates

unique_candidates = []
count_votes = []
count_candidates = 0
candidates = []

# # Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
       # Loop to add all months
    for row in csvreader:
        

for row in csvreader 
    if row[2] == row[2]
        count_candidates = count_candidates + 1
        

percent = candidates / count_votes




x = "Yes"
while x == "Yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")