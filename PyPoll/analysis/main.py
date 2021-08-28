import os
import csv
import statistics

# Set path for excel file
csvpath=os.path.join("..", "resources", "election_data.csv")

candidates = []

# Open the csv
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Skip the header row & begin pulling data from second row
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    # Loop through dandidate data
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
        print(f"List of Candidates: {candidates}")

# Loop through votes of list of candiates: ["Khan", "Correy", "Li", "O'Tooley"]
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    # establish variables with empty values to begin
    Khan = 0
    Correy = 0
    Li = 0
    O_Tooley = 0

    for row in csvreader:
        if row[2] == candidates[0]:
            Khan += 1
        elif row[2] == candidates[1]:
            Correy += 1
        elif row[2] == candidates[2]:
            Li += 1
        elif row[2] == candidates[3]:
            O_Tooley += 1
        
    # Calculate total votes and set the value to total
    total = Khan + Correy + Li + O_Tooley

    # Print the results & round to 2 decimals
    print("Elections Results")
    print("----------------------------------------------------")
    print(f"Total Votes: {total}")
    print(f"Khan: {round((Khan/total)*100, 2)}% ({Khan})")
    print(f"Correy: {round((Correy/total)*100, 2)}% ({Correy})")
    print(f"Li: {round((Li/total)*100, 2)}% ({Li})")
    print(f"O_Tooley: {round((O_Tooley/total)*100, 2)}% ({O_Tooley})")

    # Determine the winner!
    print("----------------------------------------------------")
    if Khan > Correy and Khan > Li and Khan > O_Tooley:
        winner = "Khan"
    if Correy > Khan and Correy > Li and Correy >  O_Tooley:
        winner = "Correy"
    if Li > Khan and Li > Correy and Li > O_Tooley:
        winner = "Li"
    if O_Tooley > Khan and O_Tooley > Correy and O_Tooley > Li:
        winner = "O_Tooley"
    
    print(f"The winner is {winner}!")
    print("----------------------------------------------------")

# output
    export_text = "Election Results.txt"
with open(export_text, "w", newline ="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------------------------"])
    csvwriter.writerow([f"Total Votes: {total}"])
    csvwriter.writerow(["----------------------------------------------------"])
    csvwriter.writerow([f"Total of Khan Votes: {round((Khan/total)*100,2)}% ({Khan})"])
    csvwriter.writerow([f"Total of Correy Votes: {round((Correy/total)*100,2)}% ({Correy})"])
    csvwriter.writerow([f"Total of Li Votes: {round((Li/total)*100,2)}% ({Li})"])
    csvwriter.writerow([f"Total of O_Tooley Votes: {round((O_Tooley/total)*100,2)}% ({O_Tooley})"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"The winner is {winner}!"])
    csvwriter.writerow(["------------------------------------"])