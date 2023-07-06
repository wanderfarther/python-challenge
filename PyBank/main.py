'Import OS and CSV'
import os
import csv

'Import the files to be analysed'
path = "C:\\Users\\morga\\Documents\\Analysis Projects\\Week 3\\python-challenge\\PyBank\\Resources\\"
file_name = "budget_data.csv"

file_path = os.path.join(path, file_name)

with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    csv_header = next(csvreader)
 
    'variables and lists'    
    profit = []
    change_pl_lst = []
    months =[]
    month_count = 0
    money = 0

    'look through each columkn in the row'
    for row in csvreader:
        month = str(row[0])

        profit.append(float(row[1])) # this hopefully adds the number in the profit loss column to this list
        months.append(row[0])
        
        'Find the net total amount of Profit to the total amount of Losses'
        money = money + int(row[1])
        
        'Counting the total number of months'
        month_count = month_count + 1
 
'Find the change in profit vs loss over entire period' 
begin_list = profit[:len(profit)-1]
end_list = profit[1:]

for idx, a in enumerate(begin_list):
    change_pl_lst.append(-(a-end_list[idx]))
        
max_increase = max(change_pl_lst)
min_increase = min(change_pl_lst)
pl_average = sum(change_pl_lst)/ len(change_pl_lst)

months.remove('Jan-10')

'Display total months'
# print(month_count)

'Display net total amount of profit and losses'
# print(money)

'Display the average of each day of changes of profit/loss'
# print(max_increase)
# print(min_increase)
# print(pl_average) 

'Greatest increase in profits (include date & amount) over entire period'
index_max_change = change_pl_lst.index(max_increase)
max_month_index = months[index_max_change]
# print(max_increase)
# print(max_month_index)

'Greatest decrease in profits (include date & amount) over entire period' 
index_min_change = change_pl_lst.index(min_increase)
min_month_index = months[index_min_change]
# print(min_increase)
# print(min_month_index)

'Bring it all together'
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", month_count)
print("Total: $", money)
print("Average Change: $", pl_average)
print("Greatest Increase in Profits: ", max_month_index, "($",max_increase,")")
print("Greatest Decrease in Profits: ", min_month_index, "($",min_increase,")")

total_months = "Total Months: ", month_count
total_money = "Total: $", money
ave_change = "Average Change: $", pl_average
increase = "Greatest Increase in Profits: ", max_month_index, "($",max_increase,")"
decrease = "Greatest Decrease in Profits: ", min_month_index, "($",min_increase,")"

with open("Analysis\\fin_analysis.txt", 'w') as file:
    writer = csv.writer(file, delimiter = ' ')
    writer.writerow("Financial Analysis")
    writer.writerow("----------------------------")
    writer.writerow(total_months)
    writer.writerow(total_money)
    writer.writerow(ave_change)
    writer.writerow(increase)
    writer.writerow(decrease)
    file.close()