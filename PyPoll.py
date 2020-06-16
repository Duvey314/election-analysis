
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

with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   headers = next(file_reader)
   print(headers)
   # for row in next(file_reader):
   #    print(row)

# with open(file_to_save,"w") as election_data:
#    election_data.write("Hello World")

