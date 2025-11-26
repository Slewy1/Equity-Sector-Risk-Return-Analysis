import csv
from datetime import datetime
import numpy as np


def dashboard(Tradfile):
    dates = []
    prices = []

    with open(f"E:\\Python stuff\\Project1\\{Tradfile}", newline="", encoding="utf-8-sig") as file:

        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            date = datetime.strptime(row['Date'], "%m/%d/%Y")
            dates.append(date)
            prices.append(float(row['Price']))

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

    returns = np.array(monthly_returns)

    avg_monthly_returns = np.mean(returns)
    avg_monthly_volatility = np.std(returns)

    return avg_monthly_returns, avg_monthly_volatility


if __name__ == "__main__":  # Only runs when executed directly for testing
    print(dashboard("XLE.csv"))

