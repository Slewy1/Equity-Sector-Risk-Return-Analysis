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


print(dates[:5])
print(prices[:5])

excelDate = "11/21/2025"
correctedDate = datetime.strptime(excelDate, "%m/%d/%Y")
print(correctedDate)
