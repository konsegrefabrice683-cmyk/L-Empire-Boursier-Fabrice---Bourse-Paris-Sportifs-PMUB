import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf

st.set_page_config(page_title="Fabrice AI Empire V2", page_icon="👑", layout="wide")

st.markdown("<h1 style='text-align:center;color:#FFD700;'>👑 FABRICE AI EMPIRE V2</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>Filtre STRICT 72-80% | Ouaga | {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>", unsafe_allow_html=True)

SEUIL_MIN, SEUIL_MAX = 72, 80

with st.sidebar:
    st.success(f"✅ Filtre: {SEUIL_MIN}-{SEUIL_MAX}%")
    st.metric("Bankroll LONAB", "150 000 FCFA", "3% = 4500F")
    st.metric("Bankroll PMU", "150 000 FCFA", "2% = 3000F")
    st.info("📲 Alerte WhatsApp: Active 8h/jour")
    st.warning("⚠️ VALUE mini: +12%")

tab1, tab2, tab3, tab4 = st.tabs(["⚽ PARIS 72-80%", "🐎 PMU-B LONAB", "📈 BOURSE", "📸 PHOTO IA"])

with tab1:
    st.subheader("⚽ Paris Sportifs - Zone 72-80%")
    col1, col2 = st.columns(2)
    with col1:
        match = st.text_input("Match", "Man City vs Arsenal")
        marche = st.selectbox("Marché", ["Over 2.5 Buts", "BTTS Oui", "
