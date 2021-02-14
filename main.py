import os
import csv

file = os.path.join('..', 'Resources', 'budget_data.csv')
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)  
    months = []
    profitlosses = []
    profit = []
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profitlosses.append(profit[i+1]-profit[i])
        
    increase = max(profitlosses)
    decrease = min(profitlosses)
    increasemonth = profitlosses.index(max(profitlosses))
    decreasemonth = profitlosses.index(min(profitlosses))

#print the table
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(profit)}")
#average change
print(f"Average Change: {round(sum(profitlosses)/len(profitlosses),2)}")
print(f"Greatest Increase in Profits: {months[increasemonth]} (${(str(increase))}")
print(f"Greatest Decrease in Profits: {months[decreasemonth]} (${(str(decrease))}")      

#exporting the file = USE WRITE
output = output.txt
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("------------------------")
    new.write(f"Total Months:{len(months)}")
    new.write(f"Total: ${sum(profit)}")
    new.write(f"Average Change: {round(sum(profitlosses)/len(profitlosses),2)}")
    new.write(f"Greatest Increase in Profits: {months[increasemonth]} (${(str(increase))}")
    new.write(f"Greatest Decrease in Profits: {months[decreasemonth]} (${(str(decrease))}")