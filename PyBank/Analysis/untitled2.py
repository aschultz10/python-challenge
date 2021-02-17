import os
import csv

csvpath = os.path.join()
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    month_count = []
    profit = []
    change_profit = []