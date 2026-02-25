import ReturnsFunc as rf
import numpy as np
import matplotlib.pyplot as plt


# data = ["XLE.csv", "XLF.csv", "XLK.csv", "XLP.csv", "XLV.csv", "GLD.csv", "BTCUSD.csv"]
data = ["XLE.csv", "XLF.csv", "XLK.csv",
        "XLP.csv", "XLV.csv", "GLD.csv"]
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

plt.style.use('dark_background')
plt.figure(figsize=(16, 9))
for i in range(len(label)):
    plt.scatter(x[i] * 100, y[i] * 100, s=80, edgecolor='w')
    plt.text(x[i] * 100 + 0.015, y[i] * 100 -
             0.01, label[i], fontweight="bold", fontsize=11)
plt.gca().invert_yaxis()
plt.xlim(0, 2)
plt.ylim(3, 9)

limits_x = plt.xlim(0, 2)
limits_y = plt.ylim(3, 9)

mid_x = (limits_x[1] - limits_x[0])/2
mid_y = (limits_y[1] - limits_y[0])/2

plt.axvline(x=1, color='r', label='axvline - full height',
            linewidth=4)
plt.axhline(y=6, color='r', label='axvline - full height',
            linewidth=4)

plt.grid(True)
plt.xlabel("Average Monthly Return %")
plt.ylabel("Average Monthly Volatility %")
plt.title("Trading Risk Return Scatterplot")
plt.show()
