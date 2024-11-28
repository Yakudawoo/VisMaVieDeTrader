import streamlit as st
import matplotlib.pyplot as plt

# params
capital_initial = 10_000_000  # En euros
rendement_default_1 = 3 / 100  # 3% en décimal pour le premier graphique
rendement_default_2 = 8 / 100  # 8% en décimal pour le second graphique
rendement_default_3 = 15 / 100

# Title
st.title("Simulation de placements financiers")
st.sidebar.header("Paramètres")

# Graphique 1 : Fonds Euro et Obligations
st.header("1. Simulation : Fonds Euro et Obligations")
annees_1 = st.sidebar.slider("Durée (années) - Graphique 1", 1, 10, 3)
rendement_annuel_1 = st.sidebar.slider("Rendement annuel (%) - Graphique 1", 1, 10, 3) / 100

# Graphique 1 : calcul
repartition_1 = {"Fonds Euro": 60, "Obligations": 40}
capital_fonds_euro = capital_initial * (repartition_1["Fonds Euro"] / 100)
capital_obligations = capital_initial * (repartition_1["Obligations"] / 100)
capital_total_1 = (
    capital_fonds_euro * (1 + rendement_annuel_1) ** annees_1
    + capital_obligations * (1 + rendement_annuel_1) ** annees_1
)
interets_1 = capital_total_1 - capital_initial

# Print Graphique 1
st.write(f"**Capital final après {annees_1} ans :** {capital_total_1:,.2f} €")

if interets_1 >= capital_initial * rendement_default_1 * annees_1 :
    st.markdown(f"Intérêts cumulés : \
                <span style='font-size:20px; color:green;'>{interets_1:,.2f} €</span>", unsafe_allow_html=True)
                # <li style='font-size:20px; color:green;'>{interets_1:,.2f}", unsafe_allow_html=True)
else :
    st.markdown(f"Intérêts cumulés : \
                <span style='font-size:20px; color:orange;'>{interets_1:,.2f} €</span>", unsafe_allow_html=True)
st.write(f"- Fonds Euro : {capital_fonds_euro:,.2f} € initial")
st.write(f"- Obligations : {capital_obligations:,.2f} € initial")

fig1, ax1 = plt.subplots()
labels_1 = repartition_1.keys()
sizes_1 = repartition_1.values()
explode_1 = (0.1, 0) 
ax1.pie(
    sizes_1,
    explode=explode_1,
    labels=labels_1,
    autopct="%1.1f%%",
    startangle=90,
)
ax1.axis("equal") 
st.pyplot(fig1)


# Graphique 2 : ETF et Actions
st.html("</ br></br></br>")
st.subheader("2. Résultats pour profil 2 : Modéré (5 ans minimum)")
annees_2 = st.sidebar.slider("Durée (années) - Graphique 2", 1, 10, 5)
rendement_annuel_2 = st.sidebar.slider("Rendement annuel (%) - Graphique 2", 1, 20, 8) / 100

# Graphique 2 : calcul
repartition_2 = {"ETF": 30, "Actions": 70}
capital_etf = capital_initial * (repartition_2["ETF"] / 100)
capital_actions = capital_initial * (repartition_2["Actions"] / 100)
capital_total_2 = (
    capital_etf * (1 + rendement_annuel_2) ** annees_2
    + capital_actions * (1 + rendement_annuel_2) ** annees_2
)
interets_2 = capital_total_2 - capital_initial

# Print Graphique 2
st.write(f"**Capital final après {annees_2} ans :** {capital_total_2:,.2f} €")
if interets_2 >= capital_initial * rendement_default_2 * annees_2 :
    st.markdown(f"Intérêts cumulés : \
                <span style='font-size:20px; color:green;'>{interets_2:,.2f} €</span>", unsafe_allow_html=True)
                # <li style='font-size:20px; color:green;'>{interets_2:,.2f}", unsafe_allow_html=True)
else :
    st.markdown(f"Intérêts cumulés : \
                <span style='font-size:20px; color:orange;'>{interets_2:,.2f} €</span>", unsafe_allow_html=True)
st.write(f"- ETF : {capital_etf:,.2f} € initial")
st.write(f"- Actions : {capital_actions:,.2f} € initial")

fig2, ax2 = plt.subplots()
labels_2 = repartition_2.keys()
sizes_2 = repartition_2.values()
explode_2 = (0.1, 0) 
ax2.pie(
    sizes_2,
    explode=explode_2,
    labels=labels_2,
    autopct="%1.1f%%",
    startangle=90,
)
ax2.axis("equal") 
st.pyplot(fig2)


# Graphique 3 : Fonds Euro et Obligations
st.html("</ br></br></br>")
st.header("3. Simulation : Cryptomonnaire, Actions Small Caps et Devises")
annees_3 = st.sidebar.slider("Durée (années) - Graphique 3", 1, 10, 8)
rendement_annuel_3 = st.sidebar.slider("Rendement annuel (%) - Graphique 3", 1, 30, 15) / 100

# Graphique 3 : calcul
repartition_3 = {"Cryptomonnaie": 30, "Actions Small Cap": 40, "Devises": 30} 
capital_crypto = capital_initial * (repartition_3["Cryptomonnaie"] / 100)
captial_small_cap = capital_initial * (repartition_3["Actions Small Cap"] / 100)
captial_devises = capital_initial * (repartition_3["Devises"] / 100)

capital_total_3 = (
    capital_crypto * (1 + rendement_annuel_3) ** annees_3
    + captial_small_cap * (1 + rendement_annuel_3) ** annees_3
    + captial_devises * (1 + rendement_annuel_3) ** annees_3
)
interets_3 = capital_total_3 - capital_initial

# Print Graphique 3
st.subheader("Résultats pour profil 3 : Risqué (8 ans minimum)")
st.write(f"**Capital final après {annees_3} ans :** {capital_total_3:,.2f} €")
st.write(capital_initial * rendement_default_3 * annees_3)
if interets_3 >= capital_initial * rendement_annuel_3 * annees_3 :
    st.markdown(f"Intérêts cumulés : \
                <span style='font-size:20px; color:green;'>{interets_3:,.2f} €</span>", unsafe_allow_html=True)
                # <li style='font-size:20px; color:green;'>{interets_3:,.2f}", unsafe_allow_html=True)
else :
    st.markdown(f"Intérêts cumulés : \
                <span style='font-size:20px; color:orange;'>{interets_3:,.2f} €</span>", unsafe_allow_html=True)
st.write(f"- Cryptomonnaie : {capital_crypto:,.2f} € initial")
st.write(f"- Small Caps : {captial_small_cap:,.2f} € initial")
st.write(f"- Devises : {captial_devises:,.2f} € initial")

fig1, ax1 = plt.subplots()
labels_3 = repartition_3.keys()
sizes_3 = repartition_3.values()
explode_3 = (0.05, 0.05, 0.05) 
ax1.pie(
    sizes_3,
    explode=explode_3,
    labels=labels_3,
    autopct="%1.1f%%",
    startangle=90,
)
ax1.axis("equal")
st.pyplot(fig1)