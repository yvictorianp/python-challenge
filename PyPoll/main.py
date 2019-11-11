#modules
import os
import csv

#collecting file
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

#lists to store data
all_candidates = []
each_candidate = [] 
each_candidate_votes = []
each_candidate_percent = []

#setting variable to zero
votes_total = 0
most_votes = 0

#reading csv file
with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #putting candidates in all candidates list
        all_candidates.append(row[2])
    
    #total votes casted
    votes_total = len(all_candidates)

    #getting candidate names
    #n = names
    for n in set(all_candidates):
        each_candidate.append(n)

        #getting votes for each candidate
        #v = votes
        v = all_candidates.count(n)
        each_candidate_votes.append(v)

        #getting percent for each candidate
        #p= percent
        p = (round((v/votes_total)*100))
        each_candidate_percent.append(p)
    
    #getting the candidate with most votes
    most_votes = max(each_candidate_votes)
    winner = all_candidates[each_candidate_votes.index(most_votes)]

    print ("                                     ")
    print ("Election Results")
    print ("-------------------------------------")
    print (f"Total Votes: {votes_total}")
    print ("-------------------------------------")
    #c = candidate
    for c in range (len(each_candidate)):
        print (f"{each_candidate[c]} : {str(each_candidate_percent[c])}% ({(str(each_candidate_votes[c]))})")
    print ("-------------------------------------")
    print (f"Winner: {winner}")
    print ("-------------------------------------")

#output file
results = open ("Election Results.txt", "w")
results.write ("---------------------------------------\n")
results.write ("Election Results\n")
results.write ("---------------------------------------\n")
results.write (f"Total Votes: {votes_total}\n")
results.write ("---------------------------------------\n")
for c in range (len(each_candidate)):
    results.write (f"{each_candidate[c]} : {str(each_candidate_percent[c])}% ({(str(each_candidate_votes[c]))})\n")
results.write ("---------------------------------------\n")
results.write (f"Winner: {winner}\n")
results.write ("---------------------------------------\n")
results.close()



