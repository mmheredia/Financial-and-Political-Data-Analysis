import os
import csv
import statistics

# Set path for excel file
csvpath=os.path.join("..", "resources", "budget_data.csv")

# Open the csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # establish variables with empty values to begin
    months = []
    total = []
    monthly_change = []

    # Skip the header row & begin pulling data from second row
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    # Append each row
    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        monthly_change.append(int(row[1]))

    print(f"Total Months: {len(months)}")

    # Calculate profit/loss
    total_revenue = 0
    for values in total:
        total_revenue += int(values)
    print(f"Total Profits/Losses: ${total_revenue}")

    # Calculate average change by creating a list and using zip  
    bottom_line = [j-i for i,j in zip(monthly_change[:-1], monthly_change[1:])]
    average_bottom_line = sum(bottom_line)/len(bottom_line)
    print(f"Average Change: ${round(average_bottom_line,2)}")

    # Sort the average change in decending order
    bottom_line.sort(reverse=True)
    # Takes the 0th index, which is the greatest value
    print(f"The greatest increase in profits: $ {bottom_line[0]}")
    # Takes the last index value in the list which is the smallest value
    print(f"The greatest decrease in profits: ${bottom_line[len(bottom_line)-1]}")

 # output
    export_text = "Analysis.txt"
with open(export_text, "w", newline ="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Analysis"])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f"Total Months: {len(months)}"])
    csvwriter.writerow([f"Total Profits/Losses: ${total_revenue}"])
    csvwriter.writerow([f"Average Change: ${round(average_bottom_line,2)}"])
    csvwriter.writerow([f"The greatest increase in profits: ${bottom_line[0]}"])
    csvwriter.writerow([f"The greatest decrease in profits: ${bottom_line[len(bottom_line)-1]}"])

