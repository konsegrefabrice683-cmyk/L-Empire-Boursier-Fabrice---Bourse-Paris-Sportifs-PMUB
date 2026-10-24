import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="FABRICE EMPIRE MONDIAL ULTRA", layout="wide")
st.title("FABRICE EMPIRE MONDIAL ULTRA V16.9 FINAL - INFINI")
st.caption(f"PARIS + PMU + BOURSE INTERNATIONALE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

# --- SELECTEUR DATES INFINI ---
if "date_selected" not in st.session_state:
    st.session_state.date_selected = "SAM 24"
if "nb_matchs" not in st.session_state:
    st.session_state.nb_matchs = 15

st.markdown("### 📅 Dates LONAB - INFINI")
c_cal, c1, c2, c3, c4, c5, c6 = st.columns(7)
with c_cal:
    st.markdown("📅")
with c1:
    if st.button("VEN\n23"): st.session_state.date_selected = "VEN 23"
with c2:
    if st.button("SAM\n24", type="primary"): st.session_state.date_selected = "SAM 24"
with c3:
    if st.button("DIM\n25"): st.session_state.date_selected = "DIM 25"
with c4:
    if st.button("LUN\n26"): st.session_state.date_selected = "LUN 26"
with c5:
    if st.button("MAR\n27"): st.session_state.date_selected = "MAR 27"
with c6:
    if st.button("MER\n28"): st.session_state.date_selected = "MER 28"

# --- GENERATEUR INFINI ---
EQUIPES = ["Brest", "Nice", "Mamelodi", "Raja", "Real Madrid", "Barca", "Man City", "Arsenal", "Bayern", "Dortmund", "PSG", "Lyon", "Inter", "Milan", "Al Hilal", "Al Nassr", "Juventus", "Roma", "Liverpool", "Chelsea", "EFO", "ASFA", "Burkina", "Mali", "ASEC", "Africa Sports", "Wydad", "Esperance", "Al Ahly", "Zamalek", "Simba", "Yanga", "Kaizer Chiefs", "Orlando Pirates", "TP Mazembe", "Vita Club", "Coton Sport", "Canon Yaounde", "Enyimba", "Kano Pillars", "Flamengo", "Palmeiras", "Boca", "River Plate", "Ajax", "PSV", "Feyenoord", "Benfica", "Porto", "Galatasaray", "Fenerbahce", "Al Ittihad", "Al Ahli", "SALITAS", "RCK", "AS Douanes", "RC Bobo", "Real Bamako", "Stade Malien"]

def generer_matchs_infinis(n, jour):
    matchs = []
    for i in range(n):
        eq1 = random.choice(EQUIPES)
        eq2 = random.choice([e for e in EQUIPES if e != eq1])
        matchs.append(f"{eq1} vs {eq2} - {jour}")
    return matchs

# --- CONTROLES INFINI ---
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric("Matchs chargés", f"{st.session_state.nb_matchs} / ∞")
with col_b:
    if st.button("➕ Charger +20 matchs", use_container_width=True):
        st.session_state.nb_matchs += 20
        st.rerun()
with col_c:
    if st.button("🔄 Reset à 15", use_container_width=True):
        st.session_state.nb_matchs = 15
        st.rerun()

st.success(f"📆 {st.session_state.date_selected} - {st.session_state.nb_matchs} matchs infinis - FABRICE EMPIRE MONDIAL")

tab_paris, tab_pmu, tab_bourse = st.tabs(["ANALYSE DU JOUR - INFINI ♾️", "PMU-B COMPLET", "BOURSE INTERNATIONALE"])

with tab_paris:
    jour = st.session_state.date_selected
    matchs_infinis = generer_matchs_infinis(st.session_state.nb_matchs, jour)
    
    st.subheader(f"PARIS LONAB - 7 TYPES - {jour} - {st.session_state.nb_matchs} MATCHS INFINIS")
    type_paris = st.selectbox("Type LONAB", ["1X2", "Double Chance", "BTTS Oui/Non", "Over/Under", "Cartons", "Corners", "Score Exact"], key="paris_menu")
    
    # Génération infinie selon type
    rows = []
    for match in matchs_infinis:
        cote = round(random.uniform(1.4, 3.5), 2)
        proba = random.randint(55, 85)
        value = f"+{round(random.uniform(2.0, 9.0),1)}%"
        ia = round(random.uniform(70, 82), 1)
        statut = random.choice(["FEU VERT", "FEU VERT ULTRA", "FEU VERT ULTRA", "FEU VERT"])
        
        if type_paris == "1X2":
            marche = f"{match.split(' vs ')[0]} Win"
        elif type_paris == "Double Chance":
            marche = random.choice(["1X", "X2", "12"])
        elif type_paris == "BTTS Oui/Non":
            marche = random.choice(["BTTS Oui", "BTTS Non"])
        elif type_paris == "Over/Under":
            marche = random.choice(["Over 1.5", "Over 2.5", "Over 3.5", "Under 2.5"])
        elif type_paris == "Cartons":
            marche = random.choice(["Cartons Over 3.5", "Cartons Over 4.5", "Cartons Over 5.5"])
        elif type_paris == "Corners":
            marche = random.choice(["Corners Over 8.5", "Corners Over 9.5", "Corners Over 10.5"])
        else:
            marche = random.choice(["1-0", "2-1", "2-0", "1-1", "3-1", "2-2"])
            cote = round(random.uniform(6.0, 15.0), 2)
        
        rows.append([match, marche, cote, f"{proba}%", value, ia, statut])
    
    df = pd.DataFrame(rows, columns=["Match","Marche","Cote LONAB","Proba","Value","IA %","STATUT"])
    st.dataframe(df, use_container_width=True, height=600)
    
    # Ticket infini
    total_cote = round(sum([r[2] for r in rows[:5]]), 2)
    st.code(f"TICKET {type_paris} {jour} INFINI: {st.session_state.nb_matchs} matchs dispos - Cote 5 matchs = {total_cote} -> Gain {total_cote*3000}F")
    
    if st.button("♾️ Charger 100 matchs d'un coup - INFINI"):
        st.session_state.nb_matchs = 100
        st.rerun()

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
        df_b = pd.DataFrame([["SONATEL.SN", 18500, "+2.7%", 76.5, "ULTRA", "ACHETER"], ["ORANGE.SN", 11200, "+1.8%", 71.2, "VERT", "ACHETER"], ["ECOBANK.CI", 4500, "+3.1%", 74.8, "ULTRA", "ACHETER"], ["SGB.CI", 12500, "+0.9%", 68.5, "ATTENTE", "GARDER"]], columns=["Actif","Prix","Var","IA %","STATUT","Action"])
    elif type_bourse == "USA":
        df_b = pd.DataFrame([["NVDA", 890.5, "+8.5%", 78.
