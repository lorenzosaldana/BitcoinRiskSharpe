import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt
import yfinance as yf


data = yf.Ticker('BTC-USD')

bitcoin = data.history('1y')['Close'] 

btc_price = 1000 / bitcoin[0]


btc_expected = np.multiply(bitcoin, btc_price)

risk = np.std(bitcoin)

Sharpe = np.mean(bitcoin) / risk * np.sqrt(252)

print ('Risk: ', risk)
print ('Sharpe: ', Sharpe)

plt.plot(btc_expected)

plt.savefig('plot.png')