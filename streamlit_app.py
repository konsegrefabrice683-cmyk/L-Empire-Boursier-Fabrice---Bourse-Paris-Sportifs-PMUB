import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="EMPIRE FABRICE", page_icon="👑", layout="wide")
st.title("👑 EMPIRE FABRICE - BOURSE + PARIONS + PMU'B")
st.write(f"Ouagadougou | {datetime.now().strftime('%d/%m/%Y')}")

tab1, tab2, tab3 = st.tabs(["📈 BOURSE", "⚽ PARIS", "🐴 PMU'B"])

with tab1:
    st.header("BOURSE")
    tickers = st.text_input("Actions", "AAPL, TSLA, NVDA, BTC-USD")
    seuil = st.slider("Alerte %", 1, 10, 3)
    if st.button("ANALYSER BOURSE"):
        for t in [x.strip().upper() for x in tickers.split(",")]:
            try:
                data = yf.download(t, period="1mo", progress=False)
                if data.empty: continue
                last = float(data['Close'].iloc[-1])
                prev = float(data['Close'].iloc[-2])
                var = (last-prev)/prev*100
                st.metric(t, f"${last:.2f}", f"{var:.2f}%")
                st.line_chart(data['Close'])
            except: pass

with tab2:
    st.header("PARIS SPORTIFS")
    cote1 = st.number_input("Cote 1", 1.0, 20.0, 2.10)
    proba = st.slider("Proba %", 10, 90, 55)
    value = (proba/100 * cote1) - 1
    if value > 0.05:
        st.success(f"VALUE BET {value*100:.1f}% -> PARIER")
    else:
        st.error(f"PAS VALUE {value*100:.1f}%")

with tab3:
    st.header("PRONO PMU'B")
    chevaux = []
    for i in range(6):
        chevaux.append(st.text_input(f"Cheval {i+1}", f"{i+1}", key=f"c{i}"))
    if st.button("GENERER PRONO"):
        st.success(f"TIERCE: {chevaux[1]} - {chevaux[0]} - {chevaux[3]}")
