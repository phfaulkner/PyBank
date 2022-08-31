# PyBank Challange
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Defining the stored values list
date = []
revenue = []
profit_history = []

# Open csv file
with open(csvpath) as csvfile:
# Declares how to read the csv file.
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
# Define sum_revenue to add up values of revenue list
    def sum_revenue(csvreader):
        total = 0
        for row in csvreader:
            total = int(total) + int(row)
        return total
# For loop to enter the values for date and revenue
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1]) 
# Populate profit_history, track change by month over time
for i in range(len(revenue) - 1):
    change = int(revenue[i+1]) + (0 - int(revenue[i]))
    profit_history.append(change)

endtime = (len(revenue)) - 1
months = len(date)

# Calculate total change
change = int(revenue[int(endtime)]) - int(revenue[0])
total_change = change / endtime
#format response to 2 decimal
total_change_f = "{:.2f}".format(total_change)

# Greatest increase & decrease adding total sum
min = min(profit_history)
max = max(profit_history)
total_sum = sum_revenue(revenue)

# Finding the dates corresponding to the greatest increase / decrease
for i in range(len(profit_history)-1):
    if profit_history[i] == min:
        min_date = date[i+1]
    elif profit_history[i] == max:
        max_date = date[i+1]
       
# Print results to terminal
print_statement = str(
    "------------------------------ \n"
    "Financial Anaylsis \n"
    "------------------------------ \n"
    f'Total Months: {months} \n'
    f'Total: ${total_sum} \n'
    f'Average Change: ${total_change_f} \n'
    f'Greatest Increase in Profits: {max_date} (${max}) \n'
    f'Greatest Decrease in Profits: {min_date} (${min}) \n'
    "------------------------------ \n"
    )
print(print_statement)

# Print results to txt file
# Declare output file
output = os.path.join('Analysis', 'budget_summarized.txt')
# Open file with correct permissions
file = open(output, "w")
# Write file
file.write(
    print_statement
)