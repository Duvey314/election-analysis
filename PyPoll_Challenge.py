
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

#make a list fo the county names
county_names = []

#make a dictionary to store the votes cast in each county
county_votes = {}

#store the county they are voting in
county_name = ""

county_vote = 0
county_percentage = 0

county_results = ""

#variable to hold largest county
largest_county = ""
largest_county_vote = 0

#make a list for the cadidates names
candidate_options = [ ]

#create a dictionary to hold the candidates votes
candidate_votes = {}

#open the elections results and read the file
with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   
   #increment past the headers
   headers = next(file_reader)

   #for each vote cast
   for row in file_reader:
      #add the vote to the total number of votes
      total_votes += 1
      
      #who are they voting for?
      candidate_name = row[2]

      #create a list of candidates
      if candidate_name not in candidate_options:
         #add the candidate to the candidate list
         candidate_options.append(candidate_name)
         #start tracking their totals
         candidate_votes[candidate_name] = 0
      
      #add the vote to the candidates vote total
      candidate_votes[candidate_name] += 1

      #county they are voting in
      county_name = row[1]

      #check if the county is in the list
      if county_name not in county_names:
         county_names.append(county_name)
         county_votes[county_name] = 0

      #add the vote to the county vote total
      county_votes[county_name] += 1


#write the results to the file
with open(file_to_save,"w") as election_data:
   #header for the file
   election_results = (
   f"Election Results\n"
   f"-------------------------\n"
   f"Total Votes: {total_votes:,}\n"
   f"-------------------------\n"
   f"County Results:\n")
   election_data.write(election_results)
   print(election_results)

   #tabulate county results
   for county in county_names:
      #get county vote count
      county_vote = county_votes[county]
      
      #calcultate vote percentage
      county_percentage = round(county_vote/total_votes*100,1)
      
      #find the county with the largest vote
      if county_vote > largest_county_vote:
         largest_county_vote = county_vote
         largest_county = county
      
      #save results to file
      county_results = (f"{county}: {county_percentage}% ({county_vote:,})\n")
      election_data.write(county_results)
      print(county_results)

   #save county results
   county_results =(
    f"-------------------------\n"
    f"Largest County Turnout: {largest_county} ({largest_county_vote:,})\n"
    f"-------------------------\n")
   election_data.write(county_results)
   print(county_results)

   election_data.write("Candidate Results:\n")
   print("Candidate Results:\n")
   #tabulate the totals and find the winner
   for candidate in candidate_votes:
      #number of votes the candidate received
      votes = candidate_votes[candidate]

      #vote percentage of the candidate
      vote_percentage = round(votes/total_votes*100,1)
      
      #calculate the winner
      if (votes > winning_total) and (vote_percentage > winning_percentage):
         winning_total = votes
         winning_percentage = vote_percentage 
         winning_candidate = candidate
      
      #print each candidates results
      candidate_results = (f"{candidate}: {vote_percentage}% ({votes:,})\n")
      election_data.write(candidate_results)
      print(candidate_results) 
   
   #print winning candidate
   winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_total:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
   election_data.write(winning_candidate_summary)
   print(winning_candidate_summary)