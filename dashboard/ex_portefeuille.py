import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# params
capital_initial = 10_000_000 
tickers_btc = ['BTC-USD', 'ETH-USD']
tickers_stoxx = ['MC.PA', 'OR.PA', 'AIR.PA', 'SAN.PA', 'BNP.PA',
    'GLE.PA', 'ENGI.PA', 'VIV.PA', 'SGO.PA', 'CA.PA']  
tickers_forex = ['EURUSD=X', 'GBPUSD=X'] 

start_date = '2019-01-01'
end_date = '2024-01-01'

btc_data = get_data(tickers_btc, start_date, end_date)
stoxx_data = get_data(tickers_stoxx, start_date, end_date)
forex_data = get_data(tickers_forex, start_date, end_date)

# rendements quotidiens
btc_returns = btc_data.pct_change().dropna()
stoxx_returns = stoxx_data.pct_change().dropna()
forex_returns = forex_data.pct_change().dropna()

weights = {'BTC': 0.30, 'stoxx': 0.40, 'Forex': 0.30}

# rendements pondérés
portfolio_returns = (
    btc_returns.mean(axis=1) * weights['BTC'] + 
    stoxx_returns.mean(axis=1) * weights['stoxx'] + 
    forex_returns.mean(axis=1) * weights['Forex']
)

# Calcul du capital final sur 5 ans avec un réinvestissement des rendements
portfolio_value = capital_initial * (1 + portfolio_returns).cumprod()

st.title("Simulation de Portefeuille")

st.subheader("Portefeuille total en 5 ans")
st.write(f"**Capital final estimé : {portfolio_value[-1]:,.2f} €**")

# Graphique de la performance du portefeuille
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(portfolio_value, label="Portefeuille", color="blue")
ax.set_title("Évolution du Portefeuille sur 5 ans")
ax.set_xlabel("Date")
ax.set_ylabel("Valeur du portefeuille (€)")
ax.legend()
st.pyplot(fig)

# Graphique des rendements annuels sous forme d'histogramme
st.subheader("Rendement annuel du portefeuille")

# Calcul des rendements annuels moyens
annual_returns = portfolio_returns.resample('Y').apply(lambda x: (1 + x).prod() - 1)

# Créer le graphique en barres
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.bar(annual_returns.index.year, annual_returns * 100, color=['red' if ret < 0 else 'green' for ret in annual_returns])  # Multiplie par 100 pour afficher en pourcentage
ax3.set_title("Rendement Annuel du Portefeuille")
ax3.set_xlabel("Année")
ax3.set_ylabel("Rendement (%)")
ax3.axhline(0, color='black', linestyle='--', linewidth=1.5)  
ax3.set_xticks(annual_returns.index.year) 
st.pyplot(fig3)


# Affichage des rendements moyens et volatilité
st.subheader("Rendements et volatilité")
mean_annual_return = portfolio_returns.mean() * 252  
volatility = portfolio_returns.std() * np.sqrt(252)  
st.write(f"**Rendement annuel moyen : {mean_annual_return:.2f}%**")
st.write(f"**Volatilité annuelle : {volatility:.2f}%**")


