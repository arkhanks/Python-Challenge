# -*- coding: UTF-8 -*-


# Dependencies
import csv
from pathlib import Path

# Files to load and output 
file_to_load = Path(r"C:\Users\arkha\OneDrive\Desktop\Analysis Projects\Module 3 Challenge - Python\Python-Challenge\PyBank\Resources\budget_data.csv")   
file_to_output = Path(r"C:\Users\arkha\OneDrive\Desktop\Analysis Projects\Module 3 Challenge - Python\Python-Challenge\PyBank\Analysis\.gitkeep")    

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit = None
greatest_increase = ("", float('-inf'))  # Initialize greatest increase
greatest_decrease = ("", float('inf'))   # Initialize greatest decrease
changes=[]

# Open and read the csv
with open(file_to_load, mode='r') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        month = row[0]
        profit =int(row[1])
        total_months += 1
        total_net += profit # add current to net total
        # Track the net change
        if previous_profit is not None:
            change = profit-previous_profit 
            changes.append(change) #append the changes to the changes list

             # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase[1]: 
                greatest_increase = (month, change)
            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease[1]:
                greatest_decrease = (month, change)

        previous_profit = profit # update to current month's profit/losses       


    if changes:
        # Calculate the average net change across the months
        average_change=sum(changes)/len(changes) 
    else:
        average_change=0 
# Generate the output summary
output = (
    f'Financial Analysis\n'
    f'-----------------------\n'
    f'Total Months:{total_months}\n'
    f'Net Total:${total_net}\n'
    f'Average Change: ${average_change:.2f}\n'
    f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
    f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
)
# Print the output
print(f'Financial Analysis')
print(f'-----------------------')
print(f'Total Months:{total_months}') # Print total nubmer of months
print(f'Net Total: ${total_net}') # Print net total profit/loss
print(f'Average Change: ${average_change:.2f}') 
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
