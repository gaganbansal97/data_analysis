# Data of Organisation
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#Profit for Each Month
profit = []
for i in range(0,len(revenue)):
    profit.append(revenue[i]-expenses[i])


#Calculation of Profit after tax
#First calculating tax and then profit after tax
tax = [round(i*.3,2) for i in profit]
profit_after_tax = []
for i in range(0,len(profit)):
    profit_after_tax.append(profit[i]-tax[i])


#Profit Margin = ProfitAfterTax/Revenue
profit_margin = []
for i in range(0,len(profit)):
    profit_margin.append(profit_after_tax[i]/revenue[i])
profit_margin = [round(i*100,2) for i in profit_margin]


#Mean of ProfitAfterTax of the year
mean_year = sum(profit_after_tax)/len(profit_after_tax)


#Good Months
good_months = []
for i in range(0,len(profit)):
    good_months.append(profit_after_tax[i] > mean_year)


#Bad Months
bad_months = []
for i in range(0,len(profit)):
    bad_months.append(profit_after_tax[i] < mean_year)


#Best Months
best_month = []
for i in range(0,len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))


#Worst Months
worst_month = []
for i in range(0,len(profit)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))

