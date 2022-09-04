import csv
import os 
csvpath=os.path.join("Resources/budget_data.csv")
filetooutput=os.path.join("analysis", "budget_analysis.txt")


#Declare variables
monthcount=0
nettotal=0
date=[]
profits=[]
increase=["", 0]
decrease=["", 999999999999999]

#Open CSV as Reader
with open(csvpath) as csv_file:
    csv_reader=csv.reader(csv_file)
    csv_header=next(csv_reader)
   # print(f"Header:{csv_header}") 
    firstrow=next(csv_reader)
    monthcount +=1
    nettotal += int(firstrow[1])
    previous = int(firstrow[1])
 

    #The total number of months included in the dataset
    for row in csv_reader:
        monthcount +=1
        nettotal += int(row[1])
        netchange = int(row[1]) - previous
        previous = int(row[1]) 
        profits += [netchange]  
        date += [row[0]]

        if netchange >increase[1]: 
           increase[0] = row[0]
           increase[1] = netchange

        if netchange <decrease[1]: 
           decrease[0] = row[0]
           decrease[1] = netchange  

netmonthlyaverage = sum(profits)/len(profits)


output = ( 
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {monthcount}\n"
f"Total: ${nettotal}\n"
f"Average Change: ${netmonthlyaverage:.2f}\n"
f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n")

print(output)

with open(filetooutput, "w") as file:
    file.write (output)




