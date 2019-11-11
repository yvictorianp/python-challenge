#importing modules
import os
import csv

# collecting csv file
bank_csv = os.path.join('..','Resources', 'budget_data.csv')

#lists to store data
dates = []
profit_loss = []
changes=[]

#setting variables to zero
total_months = 0
net_amount = 0
avg_change = 0
avg_monthly_chg = 0
max_change = 0
min_change = 0

#reading csv file
with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #reading through each row
    for row in csvreader:
        dates.append(row[0])
        profit_loss.append(int(row[1]))

    total_months = len(dates)
    net_amount = sum(profit_loss)

    #loop variables
    x = 1
    y = 0

    #average change
    avg_change = (profit_loss[1]- profit_loss[0])

    #loop calculating month to month change
    for date in range (total_months-1):
        avg_change = (profit_loss[x] - profit_loss[y])
        changes.append(avg_change)
        x+=1
        y+=1

    #rounded average month to month change
    avg_monthly_chg = round(sum(changes)/(total_months -1),2)

    #find max/min
    max_change = max(changes)
    min_change = min(changes)

    #getting date associated with max/min change
    max_chg_date = dates[changes.index(max_change)]
    min_chg_date = dates[changes.index(min_change)]
   

    print ("                                ")
    print ("Financial Analysis")
    print ("-------------------------------")
    print (f"Total Months: {total_months}")
    print (f"Total Net Amount: ${net_amount}")
    print (f"Average Change: ${avg_monthly_chg}")
    print (f"Greatest Increase in Profits: {max_chg_date} (${max_change})")
    print (f"Greatest Decrease in Profits: {min_chg_date} (${min_change})")
    print ("                                   ")

#output file
analysis = open ("Financial Analysis.txt", "w")
analysis.write("---------------------------------------------\n")
analysis.write(" Financial Analysis"+ "\n")
analysis.write("-------------------------------------------\n\n")
analysis.write(f" Total Months: {total_months}\n")
analysis.write(f" Total Net Amount: ${net_amount}\n")
analysis.write(f" Average Change: ${avg_monthly_chg}\n")
analysis.write(f" Greatest Increase in Profits: {max_chg_date} (${max_change})\n")
analysis.write(f" Greatest Decrease in Profits: {min_chg_date} (${min_change})\n")
analysis.write("-----------------------------------------------\n")
analysis.close()



