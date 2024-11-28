import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

indice = 'BNP.PA'

data = yf.download(indice, start='2023-11-01', end='2024-12-31')

# SMA 20 j
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# ecart type 20 j
data['STD_20'] = data['Close'].rolling(window=20).std()

# calcul des bandes de Bollinger
data['Upper_Band'] = data['SMA_20'] + (data['STD_20'] * 2)
data['Lower_Band'] = data['SMA_20'] - (data['STD_20'] * 2)

plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Prix de l\'action', color='blue', alpha=0.6)
plt.plot(data['SMA_20'], label='SMA 20 jours', color='orange')
plt.plot(data['Upper_Band'], label='Bande Supérieure', color='red', linestyle='--')
plt.plot(data['Lower_Band'], label='Bande Inférieure', color='green', linestyle='--')

plt.title(f'{indice} Bollinger', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Prix (€)')
plt.legend(loc='best')
plt.grid(True)
plt.show()
