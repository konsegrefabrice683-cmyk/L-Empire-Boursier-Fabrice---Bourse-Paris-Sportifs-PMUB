import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="FABRICE EMPIRE MONDIAL ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.9 FINAL")
st.caption(f"PARIS + PMU + BOURSE INTERNATIONALE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

tab_paris, tab_pmu, tab_bourse = st.tabs(["ANALYSE DU JOUR", "PMU-B COMPLET", "BOURSE INTERNATIONALE"])

with tab_paris:
    st.subheader("PARIS LONAB - 7 TYPES")
    type_paris = st.selectbox("Type LONAB", ["1X2", "Double Chance", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"], key="paris_menu")
    
    if type_paris == "1X2":
        df = pd.DataFrame([
            ["Brest vs Nice", "Brest Win", 2.45, "62%", "+5.5%", 76.2, "FEU VERT"],
            ["Mamelodi vs Wiliete", "Mamelodi Win", 1.85, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "Raja Win", 1.90, "66%", "+6.2%", 75.5, "FEU VERT ULTRA"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET 1X2: Brest (2.45) + Mamelodi (1.85) = 4.53 -> 13.590F")
    elif type_paris == "Double Chance":
        df = pd.DataFrame([
            ["Brest vs Nice", "1X", 1.72, "68%", "+7.2%", 76.3, "FEU VERT ULTRA"],
            ["Mamelodi vs Wiliete", "1X", 1.55, "75%", "+8.5%", 79.2, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "1X", 1.68, "65%", "+3.1%", 70.1, "ATTENTE"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET DC: Brest 1X (1.72) + Mamelodi 1X (1.55) = 2.66 -> 7.980F PLUS SUR")
    elif type_paris == "BTTS Oui/Non":
        df = pd.DataFrame([
            ["Brest vs Nice", "BTTS Oui", 1.85, "62%", "+4.8%", 74.1, "FEU VERT"],
            ["Raja vs El-Kanemi", "BTTS Oui", 1.78, "64%", "+5.1%", 73.4, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "BTTS Oui", 1.72, "68%", "+6.1%", 75.8, "FEU VERT ULTRA"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET BTTS: 1.85 + 1.78 + 1.72 = 5.66 -> 16.980F")
    elif type_paris == "Over/Under":
        df = pd.DataFrame([
            ["Brest vs Nice", "Over 1.5", 1.34, "82%", "+5.2%", 77.2, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "Over 2.5", 1.85, "66%", "+6.8%", 75.1, "FEU VERT ULTRA"],
            ["Al-Ahli vs Khaleej", "Over 3.5", 2.85, "38%", "+4.2%", 70.1, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET OVER: Over 1.5 (1.34) + Over 2.5 (1.85) = 2.47 -> 7.410F")
    elif type_paris == "Cartons":
        df = pd.DataFrame([
            ["Brest vs Nice", "Cartons Over 3.5", 1.75, "68%", "+6.1%", 74.5, "FEU VERT ULTRA"],
            ["Raja vs El-Kanemi", "Cartons Over 4.5", 1.85, "65%", "+5.8%", 74.2, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET CARTONS: Over 3.5 (1.75) + Over 4.5 (1.85) = 3.23 -> 9.690F")
    elif type_paris == "Corners":
        df = pd.DataFrame([
            ["Mamelodi vs Wiliete", "Corners Over 9.5", 1.90, "62%", "+6.2%", 73.8, "FEU VERT"],
            ["Brest vs Nice", "Corners Over 8.5", 1.75, "68%", "+4.1%", 71.2, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET CORNERS: Over 9.5 (1.90) + Over 8.5 (1.75) = 3.32 -> 9.960F")
    else:
        df = pd.DataFrame([
            ["Brest vs Nice", "2-1", 8.50, "12%", "+8.5%", 68.2, "FEU VERT"],
            ["Al-Ahli vs Khaleej", "3-1", 12.00, "9%", "+7.2%", 70.5, "FEU VERT"],
        ], columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
        st.code("TICKET SCORE: 2-1 (8.50) mise 1000F -> 8.500F")
    st.dataframe(df, use_container_width=True)

with tab_pmu:
    st.subheader("PMU-B LONAB - 7 TYPES")
    type_pmu = st.selectbox("Type LONAB", ["Quinte+", "Quarte", "Tierce", "Couple Gagnant", "Couple Place", "Gagnant", "Place"], key="pmu_menu")
    df_pmu = pd.DataFrame([
        ["1", "Mogho Power", 2.1, "42%", "+6.2%", 74.2, "FEU VERT ULTRA"],
        ["7", "Bangr Nooma", 3.2, "28%", "+4.1%", 72.8, "FEU VERT ULTRA"],
        ["5", "Etalon dOr", 3.8, "25%", "+2.8%", 68.5, "ATTENTE"],
        ["3", "Wend Panga", 4.5, "18%", "-4.2%", 55.1, "NO VALUE"],
    ], columns=["Num","Cheval","Cote LONAB","Proba","Value","IA %","STATUT"])
    st.dataframe(df_pmu, use_container_width=True)
    if type_pmu == "Quinte+": st.code("QUINTE+: 1-7-5-3-2 | Gain 435.600F")
    elif type_pmu == "Couple Place": st.code("COUPLE PLACE: 1-7 | Cote 2.85 | Gain 8.550F PLUS SUR")
    elif type_pmu == "Gagnant": st.code("GAGNANT: 1 | Cote 2.1 | Gain 6.300F")
    elif type_pmu == "Place": st.code("PLACE: 1 | Cote 1.35 | Gain 4.050F LE PLUS SUR")
    else: st.code(f"{type_pmu}: 1-7-5 | Gain estimé 85.200F")

with tab_bourse:
    st.subheader("BOURSE INTERNATIONALE - FABRICE EMPIRE MONDIAL")
    type_bourse = st.selectbox("Marché", ["BRVM", "USA", "CRYPTO", "OR & MATIERES"], key="bourse_menu")
    
    if type_bourse == "BRVM":
        df_b = pd.DataFrame([
            ["SONATEL.SN", 18500, "+2.7%", 76.5, "ULTRA", "ACHETER"],
            ["ORANGE.SN", 11200, "+1.8%", 71.2, "VERT", "ACHETER"],
            ["ECOBANK.CI", 4500, "+3.1%", 74.8, "ULTRA", "ACHETER"],
            ["SGB.CI", 12500, "+0.9%", 68.5, "ATTENTE", "GARDER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    elif type_bourse == "USA":
        df_b = pd.DataFrame([
            ["NVDA", 890.5, "+8.5%", 78.5, "ULTRA", "ACHETER"],
            ["AAPL", 182.5, "+4.2%", 73.2, "VERT", "ACHETER"],
            ["TSLA", 245.2, "+6.8%", 75.5, "ULTRA", "ACHETER"],
            ["MSFT", 415.2, "+2.1%", 70.1, "VERT", "ACHETER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    elif type_bourse == "CRYPTO":
        df_b = pd.DataFrame([
            ["BTC", 67450, "+8.7%", 83.2, "PIEGE", "VENDRE"],
            ["ETH", 3450, "+5.2%", 76.8, "VERT", "ACHETER"],
            ["SOL", 145.2, "+11%", 79.5, "ULTRA", "ACHETER"],
            ["BNB", 580, "+3.2%", 72.1, "VERT", "ACHETER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    else:
        df_b = pd.DataFrame([
            ["GOLD", 2345, "+6.5%", 77.8, "ULTRA", "ACHETER"],
            ["SILVER", 28.5, "+4.2%", 71.5, "VERT", "ACHETER"],
            ["PETROLE", 85.2, "+2.8%", 69.8, "ATTENTE", "GARDER"],
        ], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    
    st.dataframe(df_b, use_container_width=True)
    st.success(f"MARCHE {type_bourse} - Analyse FABRICE EMPIRE MONDIAL")

st.caption("FABRICE EMPIRE MONDIAL ULTRA V16.9 - OUAGA - BOURSE INTERNATIONALE COMPLETE")
