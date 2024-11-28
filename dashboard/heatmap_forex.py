import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Liste des paires de devises (Forex)
tickers_forex = tickers_forex = ['EURUSD=X', 'GBPUSD=X', 'USDJPY=X',
                                 'AUDUSD=X', 'USDCAD=X', 'NZDUSD=X', 
                                 'EURGBP=X', 'EURJPY=X', 'USDCHF=X', 
                                 'EURCHF=X', 'GBPJPY=X', 'GBPCHF=X', 
                                 'AUDJPY=X', 'AUDCHF=X', 'NZDJPY=X', 
                                 'NZDCHF=X', 'NZDCAD=X']


# Fonction pour télécharger les données historiques
def get_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Période de simulation
start_date = '2020-01-01'
end_date = '2024-10-31'

# Télécharger les données pour les paires de devises
forex_data = get_data(tickers_forex, start_date, end_date)

# Calcul des rendements quotidiens (pourcentage de variation)
forex_returns = forex_data.pct_change().dropna()

# Calcul de la matrice de corrélation des rendements
correlation_matrix = forex_returns.corr()

# Affichage de la heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Matrice de Corrélation des Rendements des Paires de Devises")
plt.show()
