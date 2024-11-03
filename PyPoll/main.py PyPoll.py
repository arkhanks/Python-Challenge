# -*- coding: UTF-8 -*-
"""PyPoll Homework."""

# Import necessary modules
import csv
from pathlib import Path

# Files to load and output 
file_to_load = Path(r"C:\Users\arkha\OneDrive\Desktop\Analysis Projects\Module 3 Challenge - Python\Python-Challenge\PyPoll\Resource\election_data.csv")  
file_to_output = Path(r"C:\Users\arkha\OneDrive\Desktop\Analysis Projects\Module 3 Challenge - Python\Python-Challenge\PyPoll\Analysis\.gitkeep") 

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}
candidate_options = []

# Winning Candidate and Winning Count Tracker
winner = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load, mode='r') as election_data:
    reader = csv.DictReader(election_data)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Get the candidate's name from the row
        candidate_name = row["Candidate"]

        # Increment the total vote count for each row
        total_votes += 1

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    output = (
        f'Election Results\n'
        f'-----------------------\n'
        f'Total Votes: {total_votes}\n'
        f'-----------------------\n'
    )
    print(output, end="")
    txt_file.write(output)  # Write output to external file

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100

        # Check for the winner
        if votes > winning_count:
            winning_count = votes
            winner = candidate

        # Print and save each candidate's vote count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)   #Write to external file

    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)  #Write to external file
    

