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
fig, ax = plt.subplots(figsize=(16, 9))  # create both figure and axes together
for i in range(len(label)):
    ax.scatter(x[i] * 100, y[i] * 100, s=80, edgecolor='w')
    ax.text(x[i] * 100 + 0.015, y[i] * 100 -
            0.01, label[i], fontweight="bold", fontsize=11)
ax.invert_yaxis()

limits_x = ax.get_xlim()
limits_y = ax.get_ylim()
mid_x = (limits_x[0] + limits_x[1]) / 2
mid_y = (limits_y[0] + limits_y[1]) / 2

ax.axvline(x=mid_x, color='w', linewidth=3, linestyle="--")
ax.axhline(y=mid_y, color='w', linewidth=3, linestyle="--")
ax.text(1.02, 3.55, 'Low Volatility', fontweight="bold", fontsize=12)
ax.text(1.02, 8.65, 'High Volatility', fontweight="bold", fontsize=12)
ax.text(0.31, 6, 'Low Return', fontweight="bold", fontsize=12)
ax.text(1.58, 6, 'High Return', fontweight="bold", fontsize=12)
# ax.annotate("LOL", (1.5, 4), xytext=(1.2, 5), arrowprops=dict())

ax.tick_params(labelsize=15)
ax.set_xlabel("Average Monthly Return %", fontsize=15)
ax.set_ylabel("Average Monthly Volatility %", fontsize=15)
ax.set_title("Trading Risk Return Scatterplot",
             fontsize=20, color='w', loc='left', style='italic')
plt.show()
