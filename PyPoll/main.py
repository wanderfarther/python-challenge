'Import OS and CSV'
import os
import csv

'Import the files to be analysed'
path = "C:\\Users\\morga\\Documents\\Analysis Projects\\Week 3\\python-challenge\\PyPoll\\Resources"
file_name = "election_data.csv"

file_path = os.path.join(path, file_name)

'Variables'
vote_count = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0
#perc_stockham = 0

'Opens and iterates through the csv file'
with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader: # Counts total votes and keeps track of each candidates votes
        vote_count = vote_count + 1
        if row[2] == "Charles Casper Stockham":
            stockham_votes = stockham_votes +1
        elif row[2] == "Diana DeGette":
            degette_votes = degette_votes + 1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes = doane_votes + 1

'Creates percentage values of votes for each candidate '
perc_stockham = "{:.3%}".format(stockham_votes / vote_count)
perc_degette = "{:.3%}".format(degette_votes / vote_count)
perc_doane = "{:.3%}".format(doane_votes / vote_count)

'Finds the winner of the election'
candidate_dict={'Charles Capser Stockham':stockham_votes, 'Dianna Degette':degette_votes, 'Raymon Anthony Doane':doane_votes}
winner = max(candidate_dict, key=candidate_dict.get)

'What to write into my new csv file'
line_1 = ("Election Results", )
line_2 = ("-------------------------", )
line_3 = ("Total Votes: ", vote_count)
line_4 = ("-------------------------", )
line_5 = ("Charles Casper Stockham: ", perc_stockham, "(",stockham_votes,")")
line_6 = ("Diana DeGette: ", perc_degette, "(", degette_votes, ")")
line_7 = ("Raymon Anthony Doane: ", perc_doane, "(", doane_votes, ")")
line_8 = ("-------------------------", )
line_9 = ("Winner: ", winner)
line_10 = ("-------------------------", )



'Writing and exporting the new csv file'
with open("Analysis\\winner_file.txt", 'w') as file:
    writer = csv.writer(file, delimiter = ' ')
    writer.writerow(line_1)
    writer.writerow(line_2)
    writer.writerow(line_3)
    writer.writerow(line_4)
    writer.writerow(line_5)
    writer.writerow(line_6)
    writer.writerow(line_7)
    writer.writerow(line_8)
    writer.writerow(line_9)
    writer.writerow(line_10)
    file.close()