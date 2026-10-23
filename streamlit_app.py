import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SEKA ULTRA", layout="wide")
st.title("SEKA ULTRA V16.3 - COMPLET")
st.caption(f"TOUS MARCHES: 1X2, DC, BTTS, OVER/UNDER, CARTONS + QUINTE, COUPLE | {datetime.now().strftime('%d/%m/%Y')} | OUAGA")

tab_jour, tab_pmu, tab_bourse = st.tabs(["ANALYSE DU JOUR COMPLETE", "PMU-B COMPLET", "BOURSE"])

with tab_jour:
    st.subheader("🔥 ANALYSE DU JOUR - 23 Oct 2026 - TOUS MARCHES")
    
    # 1. MARCHES 1X2 + DOUBLE CHANCE
    st.markdown("### 1) 1X2 + DOUBLE CHANCE")
    data_1x2 = [
        ["Brest vs Nice", "Brest", 2.45, 2.80, "62.1%", "+5.5%", 76.2, "FEU VERT ULTRA"],
        ["Brest vs Nice", "1X Double Chance", 1.72, 2.15, "68.5%", "+7.2%", 76.3, "FEU VERT ULTRA"],
        ["Brest vs Nice", "X2 Double Chance", 1.68, 1.95, "65.2%", "+3.1%", 70.1, "ATTENTE"],
        ["Mamelodi vs Wiliete", "Mamelodi", 1.85, 2.10, "75.8%", "+8.5%", 79.2, "FEU VERT ULTRA"],
        ["Mamelodi vs Wiliete", "1X Double Chance", 1.55, 1.82, "75.8%", "+8.5%", 79.2, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "Raja", 1.90, 2.20, "66.1%", "+6.2%", 75.5, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "1X Double Chance", 1.35, 1.55, "78.2%", "+5.8%", 77.1, "FEU VERT ULTRA"],
    ]
    df_1x2 = pd.DataFrame(data_1x2, columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df_1x2, use_container_width=True)

    # 2. BTTS
    st.markdown("### 2) BTTS - Les Deux Equipes Marquent")
    data_btts = [
        ["Brest vs Nice", "BTTS Oui", 1.85, 2.05, "62.1%", "+4.8%", 74.1, "FEU VERT"],
        ["Brest vs Nice", "BTTS Non", 1.95, 2.15, "58.2%", "+2.1%", 68.2, "ATTENTE"],
        ["Raja vs El-Kanemi", "BTTS Oui", 1.78, 2.10, "64.1%", "+5.1%", 73.4, "FEU VERT ULTRA"],
        ["Raja vs El-Kanemi", "BTTS Non", 2.05, 1.85, "45.2%", "-8.2%", 55.1, "NO VALUE"],
        ["Al-Ahli vs Al Khaleej", "BTTS Oui", 1.72, 1.95, "68.2%", "+6.1%", 75.8, "FEU VERT ULTRA"],
        ["Al-Ahli vs Al Khaleej", "BTTS Non", 2.15, 2.05, "42.1%", "-3.2%", 58.1, "RISQUE"],
    ]
    df_btts = pd.DataFrame(data_btts, columns=["Match", "Marche", "Cote LONAB", "Cote Juste", "Proba", "Value %", "IA %", "STATUT"])
    st.dataframe(df_btts, use_container_width=True)

    # 3. OVER UNDER
    st.markdown("### 3) OVER / UNDER BUTS")
    data_ou = [
       
