import os 
import csv

budget_data_path = os.path.join ('C:/Users/marce/OneDrive/Desktop/Git/Python--Challenge-/Resources/budget_data.csv')

#Create Variables for calculations 


profit = []
average_monthly_change = []
net_loss = []
previous_loss = 0
current_month = 0
profit_change = 0 
count_months = 0
total_revenue = 0
greatest_profit_loss = 0
highest_profit_gain = 0 
highest_gain_date = ""
greatest_loss_date = ""

#open path and read header
with open(budget_data_path, newline='') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=",")
  
    # Read the header row first
    csv_header = next(csvfile)
    
    
    for row in csv_reader: 
        
        total_revenue = total_revenue + int(row[1])
        count_months = count_months + 1
        current_month = int(row[1])
        net_loss = current_month
     
     #Find Greatest Prfit gain and loss and add the dates 
        if (current_month >= 0):
           if(current_month > highest_profit_gain):
               highest_profit_gain = current_month
               highest_gain_date = (str(row[0]))
        elif(current_month < 0):
           if(current_month < greatest_profit_loss):
               greatest_profit_loss = current_month
               greatest_loss_date =  (str(row[0]))
           
average_monthly_change = total_revenue / count_months
print(total_revenue)


# Print to the terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${total_revenue}")
print(f"Average Change:  ${average_monthly_change}")
print(f"Greatest Increase in Profits:  {highest_gain_date} (${highest_profit_gain})")
print(f"Greatest Decrease in Losses:  {greatest_loss_date} (${greatest_profit_loss})")

Finacial_Analysis = os.path.join("C:/Users/marce/OneDrive/Desktop/Git/Python--Challenge-/Pybank Financial Analysis.txtt")
with open(Finacial_Analysis, "w") as outfile:
    outfile.write("Financial Analysis")
    outfile.write("----------------------------")
    outfile.write(f"Total Months:  {count_months}")
    outfile.write(f"Total:  ${total_revenue}")\7
    outfile.write(f"Average Change:  ${average_monthly_change}")
    outfile.write(f"Greatest Increase in Profits:  {highest_gain_date} (${highest_profit_gain})")
    outfile.write(f"Greatest Decrease in Losses:  {greatest_loss_date} (${greatest_profit_loss})")
    
    
    
