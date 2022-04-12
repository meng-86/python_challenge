# Create the folder with name 'PyBank' and 'PyPoll' using bash 

# cd mentong 
# mkdir PythonHomework 
# cd PythonHomework 
# mkdir PyBank
# mkdir PyPoll
# cd PyBank
# mkdir Resources
# move download csv resource files (budget_data.csv) into Resources folder 
# cd ..
# cd PyPoll
# mkdir Resources
# move download csv resource files (election_data.csv) into Resources folder 
# cd ..
# cd PyBank
# explorer main.py

# Solving PyBank challenge
# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results

# Import dependencies
import os
import csv

# Load the data 
# files I need to load

csvpath = os.path.join('PyBank','Resources')
pathout = os.path.join('PyBank','Resources')

# Define variables for PyBank date and Profit/Losses counting 

Total_month = 0 
Total_revenue = 0
Revenue_1 = 0
Revenue_changes= 0
Revenue_changes_list = []
monthly_change= []
greatest_increase=["", 0]
greatest_decrease = ["", 99999999999]

# Read file budget_data csv 

with open(csvpath) as revenueData:
    reader= csv.reader(revenueData, delimiter=",")

# Using loop to calculate the number of month in total 

for row in reader:

   Total_month= Total_month + 1
   Total_revenue=Total_revenue+ int(row["Profit/Losses"])

# Revenue changes in dynamics
   Revenue_changes= int(row["Profit"])-Revenue_1
   Revenue_1= int(row["Revenue_1"])
   monthly_change= monthly_change+[row["Date"]]

# Gratest increase 
   if (Revenue_changes> greatest_increase[1]):
       greatest_increase[1]= Revenue_changes
       greatest_increase[0]= row["Date"]
# Gratest decrease     
   if (Revenue_changes> greatest_decrease[1]):
       greatest_decrease[0]= row["Date"]
       greatest_decrease[1]= Revenue_changes

# Calculating the average revenue of full sample 

Revenue_mean=sum(Revenue_changes_list)/len(Revenue_changes_list)

# Printing analysis output 

#print the outcomes


print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {Total_month}")
print(f"Total:  ${Total_revenue}")
print(f"Average Change:  ${Revenue_mean}")
print(f"Greatest increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]}\n")
print(f"Greatest decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n")













