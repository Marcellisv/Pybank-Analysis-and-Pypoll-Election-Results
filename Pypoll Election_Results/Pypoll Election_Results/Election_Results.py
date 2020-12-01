import os
import csv 

election_data_csv = os.path.join("C:/Users/marce/OneDrive/Desktop/Git/Python--Challenge-/Pypoll Election_Results/election_data.csv")


#Create varibles 

total_votes = 0
candidates_votes = []
candidates = []
winning_candidate = ""
winners_votes = 0
percent_of_vote = 0.0
v = 0
with open(election_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    
    for row in csvreader:
        #Add total vote count
        total_votes = total_votes + 1
        
    # Account for canidates not in the list
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidates_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidates_votes[index] += 1
            
   #caculate the winner      
   #using the lambada funtion we can cycle through the candidates total votes and return the candidate with the most votes
    winning_votes = max(range(len(candidates_votes)), key = lambda x: candidates_votes[x])
    winning_candidate = candidates[int(winning_votes)]              
      

     
       
#Print Results in the Terminal 
 
print("Election Results") 
print("-----------------------------------")
print(f"Total Votes:  {str(total_votes)}")
print("-----------------------------------")
while v <= (len(candidates) - 1):
	print(str(candidates[v]) + ": " + str(round((candidates_votes[v]/total_votes * 100),2)) + "% (" + str(candidates_votes[v]) + ")")
	v = v + 1
winning_cannidate = max(candidates_votes)

print("-----------------------------------")
print("Winner:" + str(winning_candidate))
print("------------------------------------")


#Output to a text file 
Election_Results = os.path.join("C:/Users/marce/OneDrive/Desktop/Git/Python--Challenge-/Pypoll Election_Results/Election_Results.txt")
with open(Election_Results, "w+", newline = "\n") as outfile:

    outfile.write("Election Results\n") 
    
    outfile.write("-----------------------------------\n")
    
    outfile.write("Total Votes:  {str(total_votes)}" + "\n")
    
    outfile.write("-----------------------------------\n")
    
    while v <= (len(candidates) - 1):
        outfile = str(f"(candidates[v]):", "str(round((candidates_votes[v]/total_votes * 100),2))" + "%"  + "(str(candidates_votes[v]) + ")
        v = v + 1
    outfile.write("-----------------------------------\n")
    
    outfile.write("Winner:" + str(winning_candidate) + "\n")
    
    outfile.write("------------------------------------\n")
        
            

            
     
    