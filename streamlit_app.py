import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SEKA ULTRA", layout="wide")
st.title("SEKA ULTRA V16.4 FIX")
st.caption(f"FIX BRACKET + TOUS MARCHES | {datetime.now().strftime('%d/%m/%Y')} | OUAGA")

tab0, tab1, tab2 = st.tabs(["ANALYSE DU JOUR COMPLETE", "PMU-B COMPLET", "BOURSE"])

with tab0:
    st.subheader("ANALYSE DU JOUR - 23 Oct 2026 - TOUS MARCHES")

    st.markdown("### 1) 1X2 + DOUBLE CHANCE")
    df1 = pd.DataFrame([
        ["Brest vs Nice", "1X DC", 1.72, 2.15, "68.5%", "+7.2%", 76.3, "FEU VERT ULTRA"],
        ["Mamelodi vs Wiliete", "1X DC", 1.55, 1.82, "75.8%", "+8.5%", 79.2, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "Raja Win", 1.90, 2.20, "66.1%", "+6.2%", 75.5, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "1X DC", 1.35, 1.55, "78.2%", "+5.8%", 77.1, "FEU VERT ULTRA"],
    ], columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df1, use_container_width=True)

    st.markdown("### 2) BTTS")
    df2 = pd.DataFrame([
        ["Brest vs Nice", "BTTS Oui", 1.85, 2.05, "62.1%", "+4.8%", 74.1, "FEU VERT"],
        ["Raja vs El-Kanemi", "BTTS Oui", 1.78, 2.10, "64.1%", "+5.1%", 73.4, "FEU VERT ULTRA"],
        ["Al-Ahli vs Al Khaleej", "BTTS Oui", 1.72, 1.95, "68.2%", "+6.1%", 75.8, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "BTTS Non", 2.05, 1.85, "45.2%", "-8.2%", 55.1, "NO VALUE"],
    ], columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df2, use_container_width=True)

    st.markdown("### 3) OVER UNDER")
    df3 = pd.DataFrame([
        ["Brest vs Nice", "Over 1.5", 1.34, 1.45, "82.1%", "+5.2%", 77.2, "FEU VERT ULTRA"],
        ["Al-Ahli vs Al Khaleej", "Over 2.5", 1.85, 2.20, "66.2%", "+6.8%", 75.1, "FEU VERT ULTRA"],
        ["Brest vs Nice", "Over 2.5", 2.05, 2.35, "58.2%", "+4.1%", 71.2, "FEU VERT"],
        ["Al-Ahli vs Al Khaleej", "Over 3.5", 2.85, 3.20, "38.2%", "+4.2%", 70.1, "FEU VERT"],
    ], columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df3, use_container_width=True)

    st.markdown("### 4) CARTONS")
    df4 = pd.DataFrame([
        ["Brest vs Nice", "Cartons Over 3.5", 1.75, 1.95, "68.2%", "+6.1%", 74.5, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "Cartons Over 4.5", 1.85, 2.10, "65.2%", "+5.8%", 74.2, "FEU VERT ULTRA"],
        ["Mamelodi vs Wiliete", "Corners Over 9.5", 1.90, 2.20, "62.1%", "+6.2%", 73.8, "FEU VERT ULTRA"],
    ], columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %
