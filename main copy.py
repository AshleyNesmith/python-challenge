import os
import csv

#path to csv files
election_data = os.path.join("Resources", "election_data.csv")

#list of names of candidates

candidates = []

#list of number of votes each candidate receives 

num_votes = []

#list of perecentage of total votes each candidate garners

percent_votes = []

#counter for the toal number of votes

total_votes = 0

with open(election_data, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        #add to vote-counter

        total_votes += 1

if row[2] not in candidates:
    candidates.append(row[2])
    index = candidates.index(row[2])
    num_votes.append(1)

else:
    index = candidates.index(row[2])
    num_votes.append(1)

    #add percent_votes
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage) 

    #find the winning candidate
    winner = max(num_votes) 
    index = num_votes.index(winner) 
    winning_candidate = candidates[index]

    #results
    print("Election Results")
    print(f"Total Votes: {str(total_votes)}")

    for i in range(len(candidates)):
        print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
        print(f"Winner: {winning_candidate}")


