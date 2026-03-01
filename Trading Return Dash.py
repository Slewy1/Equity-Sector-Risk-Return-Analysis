import ReturnsFunc as rf
import numpy as np
import matplotlib.pyplot as plt
import os


# data = ["XLE.csv", "XLF.csv", "XLK.csv", "XLP.csv", "XLV.csv", "GLD.csv", "BTCUSD.csv"]
data = ["XLE.csv", "XLF.csv", "XLK.csv",
        "XLP.csv", "XLV.csv", "GLD.csv"]
sector_names = {
    'XLE': 'Energy',
    'XLF': 'Finance',
    'XLK': 'Tech',
    'XLP': 'Consumer Staples',
    'XLV': 'Healthcare',
    'GLD': 'Gold'
}
results = {}

for d in data:
    avg, vol = rf.dashboard(d)
    results[d.replace(".csv", "")] = (avg, vol)

ranking_avg = {}
ranking_vol = {}

for ret in data:
    avg = results[ret.replace(".csv", "")][0]
    ranking_avg[ret.replace(".csv", "")] = avg
    vol = results[ret.replace(".csv", "")][1]
    ranking_vol[ret.replace(".csv", "")] = vol

# ranks highest to lowest (best to worst)
avgRank = sorted(ranking_avg.items(), key=lambda x: x[1], reverse=True)
# ranks lowest to highest (best to worst)
riskRank = sorted(ranking_vol.items(), key=lambda x: x[1])

# ranking_avg.items(): turns dictionary → list of (name, return) pairs
# key=lambda x: x[1]: sort based on the 2nd thing, which is the return

for name, avg in avgRank:
    print(sector_names[name], f"{round(avg*100, 2)}%")
for name, vol in riskRank:
    print(sector_names[name], f"{round(vol*100, 2)}%")


x = np.array(list(ranking_avg.values()))
y = np.array(list(ranking_vol.values()))
label = list(sector_names.values())


fig, ax = plt.subplots(figsize=(16, 9))  # create both figure and axes together
ax.set_facecolor("#0E0E0E")
fig.patch.set_facecolor("#242424")
bbox = dict(boxstyle="round,pad=0.5", fc="#3E3E3E", ec="w", lw=2, alpha=0.8)
for i in range(len(label)):
    ax.scatter(x[i] * 100, y[i] * 100, s=200, edgecolor='w')

    ax.text(x[i] * 100 + 0.025, y[i] * 100 -
            0.05, label[i], fontweight="bold", fontsize=11, bbox=bbox, color='w')

ax.invert_yaxis()
limits_x = ax.get_xlim()
limits_y = ax.get_ylim()
mid_x = (limits_x[0] + limits_x[1]) / 2
mid_y = (limits_y[0] + limits_y[1]) / 2

# ax.axvline(x=mid_x, color='w', linewidth=3, linestyle="--")
# ax.axhline(y=mid_y, color='w', linewidth=3, linestyle="--")

ax.annotate("", (mid_x, limits_y[0]-0.35), xytext=(mid_x, limits_y[1]+0.35),
            arrowprops=dict(arrowstyle="<->", linewidth=3, color='w'))
ax.annotate("", (limits_x[0]+0.1, mid_y), xytext=(limits_x[1]-0.1, mid_y),
            arrowprops=dict(arrowstyle="<->", linewidth=3, color='w'))

ax.text(mid_x, 3.7, 'Low Volatility',
        fontweight="bold", fontsize=12, ha='center', color="#00a9dce4")
ax.text(mid_x, 8.6, 'High Volatility',
        fontweight="bold", fontsize=12, ha='center', color="#ff5454d3")
ax.text(0.35, mid_y+0.1, 'Low \nReturn',
        fontweight="bold", fontsize=12, ha='center', color="#ffcc00e6")
ax.text(1.67, mid_y+0.1, 'High \nReturn',
        fontweight="bold", fontsize=12, ha='center', color="#2bff06a0")

ax.grid(True, color='grey', linestyle='--', linewidth=0.5)
ax.tick_params(labelsize=15, colors='w')
ax.set_xlabel("Average Monthly Return %", fontsize=15,
              color='w', fontweight="bold")
ax.set_ylabel("Average Monthly Volatility %",
              fontsize=15, color='w', fontweight="bold")
ax.set_title("Trading Risk Return Scatterplot",
             fontsize=25, color='w', loc='left', style='italic', fontweight="bold")

save_path = os.path.join(os.path.dirname(__file__), 'RiskReturn Scatterplot.png')
fig.savefig(save_path, dpi=300, bbox_inches='tight')
plt.show()

