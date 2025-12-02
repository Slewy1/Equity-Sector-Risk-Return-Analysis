import ReturnsFunc as rf
import numpy as np
import matplotlib.pyplot as plt


data = ["XLE.csv", "XLF.csv", "XLK.csv",
        "XLP.csv", "XLV.csv", "GLD.csv", "BTCUSD.csv"]
results = {}

for d in data:
    avg, vol = rf.dashboard(d)
    results[d.replace(".csv", "")] = (avg, vol)

print(results)

ranking_avg = {}
ranking_vol = {}

for ret in data:
    avg = results[ret.replace(".csv", "")][0]
    ranking_avg[ret.replace(".csv", "")] = avg
    vol = results[ret.replace(".csv", "")][1]
    ranking_vol[ret.replace(".csv", "")] = vol

print(ranking_avg)

# ranks highest to lowest (best to worst)
avgRank = sorted(ranking_avg.items(), key=lambda x: x[1], reverse=True)
# ranks lowest to highest (best to worst)
riskRank = sorted(ranking_vol.items(), key=lambda x: x[1])

# ranking_avg.items(): turns dictionary → list of (name, return) pairs
# key=lambda x: x[1]: sort based on the 2nd thing, which is the return

for name, avg in avgRank:
    print(name, f"{avg*100}%")
for name, vol in riskRank:
    print(name, f"{vol*100}%")


x = np.array(list(ranking_avg.values()))
y = np.array(list(ranking_vol.values()))
label = list(results.keys())

for i in range(len(label)):
    plt.scatter(x[i] * 100, y[i] * 100)
    plt.text(x[i] * 100 + 0.05, y[i] * 100 - 0.15, label[i], fontweight="bold")


plt.grid(True)
plt.xlabel("Average Monthly Return %")
plt.ylabel("Average Monthly Volatility %")
plt.title("Trading Risk Return Scatterplot")
plt.show()


