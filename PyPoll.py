
   # PyPoll
   # Tabulating vote counts for candidates and declaring winner based on popular vote 
   #
   # Need to track:
   # Total number of votes cast
   # A complete list of candidates who received votes
   # Total number of votes each candidate received
   # Percentage of votes each candidate won
   # The winner of the election based on popular vote
#import the needed libraries
import datetime as dt
import csv
import os

#where to load the data from 
file_to_load = os.path.join("Resources", "election_results.csv")

#where to save the output to
file_to_save = os.path.join("analysis","election_analysis.txt")

#set a variable to hold vote counts
total_votes = 0

#winners circle
winning_total = 0
winning_percentage = 0
winning_candidate = ""

#make a list for the cadidates names
candidate_options = [ ]

#create a dictionary to hold the candidates votes
candidate_votes = {}

#open the elections results and read the file
with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   
   #print the header row
   headers = next(file_reader)
   print(headers)

   #for each vote cast
   for row in file_reader:
      #add the vote to the total number of votes
      total_votes += 1
      
      #who are they voting for?
      candidate_name = row[2]
      
      #create a list of candidates
      if candidate_name not in candidate_options:
         candidate_options.append(row[2])
         candidate_votes[row[2]] = 0
      
      #add the vote to the candidates vote total
      candidate_votes[row[2]] += 1
      
#write the results to the file
with open(file_to_save,"w") as election_data:
   for candidate in candidate_votes:
      #number of votes the candidate received
      votes = candidate_votes[candidate]

      #vote percentage of the candidate
      vote_percentage = round(votes/total_votes*100,1)
      
      if (votes > winning_total) and (vote_percentage > winning_percentage):
         winning_total = votes
         winning_percentage = vote_percentage 
         winning_candidate = candidate

      #print all data totals
      election_data.write(f"{candidate}: recevied {vote_percentage}% of the vote\n") 
   
   #print winning candidate
   election_data.write(f"The winning candidate is:{winning_candidate} who recevied {winning_percentage}% of the vote")