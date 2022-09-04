import csv
import os
csvpath = os.path.join("Resources/election_data.csv")
filetooutput = os.path.join("analysis", "election_analyis.txt")

totalvotes = 0

candidateoptions = []
candidatevotes = {}
winningcandidate = ""
winningcount = 0


with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
   # print(f"Header:{csv_header}")


    for row in csv_reader: 
        totalvotes += 1
        candidatename = row[2]

        if candidatename not in candidateoptions: 
            candidateoptions.append(candidatename)
            candidatevotes[candidatename] = 0

        candidatevotes[candidatename] +=1

with open(filetooutput, "w") as file:
    output = (f"""Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------\n""")
    print(output)    
    file.write (output)

    for candidate in candidatevotes:
        votes = candidatevotes.get(candidate)
        votepercent = votes/totalvotes*100

        if votes > winningcount:
            winningcount = votes
            winningcandidate = candidate

        votecount = f"{candidate}: {votepercent:.3f}% ({votes})\n"
        print(votecount)
        file.write(votecount)

    winningcandidateannouncement=(f""" 
-------------------------
Winner: {winningcandidate}
-------------------------
    """)
    print(winningcandidateannouncement)
    file.write(winningcandidateannouncement)
