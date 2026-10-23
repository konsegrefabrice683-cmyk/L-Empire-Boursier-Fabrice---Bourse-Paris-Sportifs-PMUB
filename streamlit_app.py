import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SEKA ULTRA", layout="wide")
st.title("SEKA ULTRA V16.5 - FINAL COMPLET")
st.caption(f"PARIS + PMU + BOURSE INTERNATIONALE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

tab0, tab1, tab2 = st.tabs(["ANALYSE DU JOUR", "PMU-B COMPLET", "BOURSE INTERNATIONALE"])

with tab0:
    st.subheader("ANALYSE DU JOUR - 23 Oct 2026")
    
    st.markdown("### 1) 1X2 + DOUBLE CHANCE")
    df1 = pd.DataFrame([
        ["Brest vs Nice", "1X DC", 1.72, 2.15, "68.5%", "+7.2%", 76.3, "FEU VERT ULTRA"],
        ["Mamelodi vs Wiliete", "1X DC", 1.55, 1.82, "75.8%", "+8.5%", 79.2, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "Raja Win", 1.90, 2.20, "66.1%", "+6.2%", 75.5, "FEU VERT ULTRA"],
    ], columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df1, use_container_width=True)

    st.markdown("### 2) BTTS + OVER UNDER + CARTONS")
    df2 = pd.DataFrame([
        ["Brest vs Nice", "BTTS Oui", 1.85, 2.05, "62.1%", "+4.8%", 74.1, "FEU VERT"],
        ["Raja vs El-Kanemi", "BTTS Oui", 1.78, 2.10, "64.1%", "+5.1%", 73.4, "FEU VERT ULTRA"],
        ["Al-Ahli vs Al Khaleej", "Over 2.5", 1.85, 2.20, "66.2%", "+6.8%", 75.1, "FEU VERT ULTRA"],
        ["Brest vs Nice", "Over 1.5", 1.34, 1.45, "82.1%", "+5.2%", 77.2, "FEU VERT ULTRA"],
        ["Brest vs Nice", "Cartons Over 3.5", 1.75, 1.95, "68.2%", "+6.1%", 74.5, "FEU VERT ULTRA"],
    ], columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df2, use_container_width=True)
    st.code("COMBINE DU JOUR 3000F: Brest 1X (1.72) + Raja BTTS Oui (1.78) + Al-Ahli Over 2.5 (1.85) = 5.66 -> 16.980F")

with tab1:
    st.subheader("PMU-B LONAB - 7 TYPES")
    type_pari = st.selectbox("Type LONAB", ["Quinte+", "Quarte", "Tierce", "Couple Gagnant", "Couple Place", "Gagnant", "Place"], index=0)
    
    df_pmu = pd.DataFrame([
        ["1", "Mogho Power", 2.1, 2.45, "42.1%", "+6.2%", 74.2, "FEU VERT ULTRA"],
        ["7", "Bangr Nooma", 3.2, 3.65, "28.2%", "+4.1%", 72.8, "FEU VERT ULTRA"],
        ["5", "Etalon dOr", 3.8, 4.10, "25.1%", "+2.8%", 68.5, "ATTENTE"],
        ["3", "Wend Panga", 4.5, 4.20, "18.2%", "-4.2%", 55.1, "NO VALUE"],
        ["2", "Roi du Sahel", 5.5, 5.80, "15.1%", "+1.2%", 62.1, "ATTENTE"],
    ], columns=["Num", "Cheval", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df_pmu, use_container_width=True)

    if type_pari == "Quinte+":
        st.code("QUINTE+: 1-7-5-3-2 | Gain 3000F: 435.600F | IA 71.5%")
    elif type_pari == "Couple Gagnant":
        st.code("COUPLE GAGNANT: 1-7 | Cote 6.72 | Gain 20.160F")
    elif type_pari == "Couple Place":
        st.code("COUPLE PLACE: 1-7 | Cote 2.85 | Gain 8.550F | PLUS SUR")
    elif type_pari == "Gagnant":
        st.code("GAGNANT: 1 Mogho Power | Cote 2.1 | Gain 6.300F")
    elif type_pari == "Place":
        st.code("PLACE: 1 Mogho Power | Cote 1.35 | Gain 4.050F | LE PLUS SUR")
    elif type_pari == "Tierce":
        st.code("TIERCE: 1-7-5 | Cote 28.4 | Gain 85.200F")
    else:
        st.code("QUARTE: 1-7-5-2 | Cote 68.5 | Gain 205.500F")

with tab2:
    st.subheader("BOURSE INTERNATIONALE - BRVM + NASDAQ + CRYPTO + OR + FOREX")
    
    st.markdown("### 1) BRVM - Cote d'Ivoire / Burkina / Senegal")
    df_brvm = pd.DataFrame([
        ["SONATEL.SN", 18500, 18000, "+2.7%", "FORT", 62, 76.5, "FEU VERT ULTRA", "ACHETER"],
        ["ORANGE.SN", 11200, 11000, "+1.8%", "MOYEN", 58, 71.2, "FEU VERT", "ACHETER"],
        ["ONATEL.BF", 3420, 3350, "+2.0%", "FAIBLE", 45, 65.1, "ATTENTE", "ATTENDRE"],
        ["SGBC.CI", 12500, 12200, "+2.4%", "FORT", 60, 74.8, "FEU VERT", "ACHETER"],
    ], columns=["Actif", "Prix", "MM20", "Var %", "Volume", "RSI", "IA %", "STATUT", "Action"])
    st.dataframe(df_brvm, use_container_width=True)

    st.markdown("### 2) NASDAQ USA - AAPL, TSLA, NVDA, MSFT")
    df_nasdaq = pd.DataFrame([
        ["AAPL", 182.5, 175.0, "+4.2%", "MOYEN", 58, 73.2, "FEU VERT ULTRA", "ACHETER"],
        ["TSLA", 248.3, 260.0, "-4.5%", "FORT", 72, 68.1, "RISQUE BAISSE", "VENDRE"],
        ["NVDA", 890.5, 820.0, "+8.5%", "FORT", 68, 78.5, "FEU VERT ULTRA", "ACHETER"],
        ["MSFT", 415.2, 400.0, "+3.8%", "FORT", 61, 76.1, "FEU VERT ULTRA", "ACHETER"],
        ["GOOGL", 165.8, 160.0, "+3.6%", "MOYEN", 59, 72.5, "FEU VERT", "ACHETER"],
    ], columns=["Actif", "Prix", "MM20", "Var %", "Volume", "RSI", "IA %", "STATUT", "Action"])
    st.dataframe(df_nasdaq, use_container_width=True)

    st.markdown("### 3) CRYPTO + OR + FOREX")
    df_crypto = pd.DataFrame([
        ["BTC-USD", 67450, 62000, "+8.7%", "FORT", 78, 83.2, "PIEGE SURACHETE", "VENDRE"],
        ["ETH-USD", 3210, 3000, "+7.0%", "MOYEN", 70, 75.5, "FEU VERT", "ACHETER"],
        ["SOL-USD", 145.2, 130.0, "+11.6%", "FORT", 75, 79.8, "FEU VERT ULTRA", "ACHETER"],
        ["GOLD OR", 2345, 2200, "+6.5%", "FORT", 65, 77.8, "FEU VERT ULTRA", "ACHETER"],
        ["EUR/USD FOREX", 1.085, 1.070, "+1.4%", "FORT", 55, 70.2, "FEU VERT", "ACHETER"],
    ], columns=["Actif", "Prix", "MM20", "Var %", "Volume", "RSI", "IA %", "STATUT", "Action"])
    st.dataframe(df_crypto, use_container_width=True)

    st.success("PORTEFEUILLE INTERNATIONAL DU JOUR")
    st.code("""
    PORTEFEUILLE ULTRA 23/10/2026:
    ACHETER: SONATEL.SN (76.5%) + NVDA (78.5%) + MSFT (76.1%) + SOL (79.8%) + GOLD (77.8%)
    VENDRE: BTC (83.2% PIEGE) + TSLA (RISQUE BAISSE)
    IA MOY PORTEFEUILLE: 76.8% FEU VERT ULTRA
    """)

st.divider()
st.caption("SEKA ULTRA V16.5 FINAL - TOUS MARCHES + BOURSE INTL - OUAGA")
