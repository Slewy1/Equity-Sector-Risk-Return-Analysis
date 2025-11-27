import ReturnsFunc as rf
import matplotlib.pyplot as plt

avgE, volE = rf.dashboard("XLE.csv")
avgF, volF = rf.dashboard("XLF.csv")
avgK, volK = rf.dashboard("XLK.csv")
avgP, volP = rf.dashboard("XLP.csv")
avgV, volV = rf.dashboard("XLV.csv")
# avgBTC, volBTC = rf.dashboard("BTCUSD.csv")
avgGd, volGd = rf.dashboard("GLD.csv")

results = {
    "XLE": (avgE, volE),
    "XLV": (avgV, volV),
    "XLF": (avgF, volF),
    # "BTC": (avgBTC, volBTC), 
    "GLD": (avgGd, volGd)
}

print(results)

print(avgE, volE)
print(avgV, volV)
print(avgF, volF)


plt.plot()
plt.show

