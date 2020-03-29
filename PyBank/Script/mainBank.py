import os
import csv

bank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Things I neeeeeds:
# Start with 0 and then count up or replace as we find a new record increase / decrease
total_months = 0
total_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

# [] to store all my changes
last_change = 0
changes = []

# python reads csv
with open(bank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# python reads each row.  all two columns in each one
# and keeps a running tally of total profits and months as it goes    
    for row in csvreader:
        date = row[0]
        profits = int(row[1])
        total_profit += profits
        total_months += 1
        
# python storing each change for me while keeping track of the biggest winners and losers
        change = profits - last_change
        if total_months != 1:
            changes.append(change)
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = date
        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = date

        last_change = profits

# with our new collection of changes python recorded, we average it by how many total changes there are 
average_change = (round(sum(changes)/len(changes), 2))

monthly_average_profit = int(round(total_profit/total_months, 0))

# \n so it's line by line
analysis = (
f"Financial Analysis\n"
f"--------------------------------------------------------\n"
f"Total Profit: ${total_profit}\n"
f"Total Months: {total_months}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: ${greatest_inc} during {greatest_inc_month}\n"
f"Greatest Decrease in Profits: ${greatest_dec} during {greatest_dec_month}\n"
)

print(analysis)

# create a text file of the analysis
output_file = os.path.join("PyBank_Analysis.csv")

with open("PyBank_Analysis.csv", "w") as text_file:
    print(f"{analysis}", file=text_file)