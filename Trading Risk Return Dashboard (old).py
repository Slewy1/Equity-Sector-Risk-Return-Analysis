import csv
from datetime import datetime

dates = []
prices = []

# encoding="utf-8-sig" remoes BOM and quotes in header
with open(r"E:\Python stuff\Project1\XLE.csv", newline="", encoding="utf-8-sig") as file:

    csv_reader = csv.DictReader(file)

#    for row in csv_reader: # Check true name for headers
#        print(row.keys())
#        break

    for row in csv_reader:

        date = datetime.strptime(row['Date'], "%m/%d/%Y")
        dates.append(date)
        prices.append(float(row['Price']))


# print(dates[:5])
# print(prices[:5])

# excelDate = "11/21/2025"
# correctedDate = datetime.strptime(excelDate, "%m/%d/%Y")
# print(correctedDate)

dates.reverse()
prices.reverse()

monthly_returns = []
monthly_dates = []

current_month = (dates[0].year, dates[0].month)
first_price_of_month = prices[0]


for i in range(1, len(dates)):
    this_month = (dates[i].year, dates[i].month)

    if this_month == current_month:
        continue
    else:
        monthly_return = (
            prices[i-1] - first_price_of_month)/first_price_of_month
        monthly_returns.append(monthly_return)
        monthly_dates.append(dates[i-1])
        current_month = this_month
        first_price_of_month = prices[i]


print(monthly_returns)
print(monthly_dates)
