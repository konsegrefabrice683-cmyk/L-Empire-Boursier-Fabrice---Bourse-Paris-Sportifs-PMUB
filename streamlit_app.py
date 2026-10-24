import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="FABRICE V17", layout="wide")
st.title("FABRICE EMPIRE V17 - JOURS INFINIS")
st.caption("MOTEUR NEUF - PARIS + PMU + BOURSE")

if "nb_jours" not in st.session_state:
    st.session_state.nb_jours = 5

EQUIPES = ["Real","Barca","Man City","Arsenal","Bayern","PSG","Inter","Brest","Nice","EFO","ASFA","Burkina"]
CHEVAUX = ["Mogho Power","Bangr Nooma","Etalon dOr","Wend Panga","Faso Eclair","Sahel Vent","Ouaga Flash","Bobo Speed"]

def get_label(j, d, suf):
    ds = d.strftime("%d/%m/%Y")
    if j==0:
        return f"AUJOURD HUI - {ds} - {suf}"
    if j==1:
        return f"DEMAIN - {ds} - {suf}"
    return f"JOUR +{j} - {ds} - {suf}"

col1, col2 = st.columns(2)
with col1:
    st.metric("Jours", st.session_state.nb_jours)
with col2:
    if st.button("➕ +3 JOURS INFINIS"):
        st.session_state.nb_jours += 3
        st.rerun()

tab1, tab2, tab3 = st.tabs(["PARIS INFINI","PMU INFINI","BOURSE INFINI"])
today = datetime.now()

with tab1:
    tp = st.selectbox("Type LONAB", ["1X2","Double Chance","BTTS","Over/Under","Cartons","Corners","Score Exact"], key="p1")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        label = get_label(j, dj, "15 MATCHS")
        with st.expander(label, expanded=(j<2)):
            rows = []
            for k in range(15):
                a = random.choice(EQUIPES)
                b = random.choice(EQUIPES)
                while b==a:
                    b = random.choice(EQUIPES)
                rows.append([a+" vs "+b, tp, 1.85, "65%", "+5%", 75.0, "FEU VERT"])
            df = pd.DataFrame(rows, columns=["Match","Marche","Cote","Proba","Value","IA","STATUT"])
            st.dataframe(df, use_container_width=True, hide_index=True)

with tab2:
    tp2 = st.selectbox("Type PMU", ["Quinte+","Quarte","Tierce","Couple Place"], key="p2")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        label = get_label(j, dj, "PMU")
        with st.expander(label, expanded=(j<1)):
            rows = []
            for i, ch in enumerate(CHEVAUX):
                rows.append([str(i+1), ch, round(random.uniform(2,9),1), "25%", 72.0])
            df = pd.DataFrame(rows, columns=["Num","Cheval","Cote","Proba","IA"])
            st.dataframe(df, use_container_width=True, hide_index=True)

with tab3:
    tp3 = st.selectbox("Marche", ["BRVM","USA","CRYPTO","OR"], key="p3")
    for j in range(st.session_state.nb_jours):
        dj = today + timedelta(days=j)
        label = get_label(j, dj, f"BOURSE {tp3}")
        with st.expander(label, expanded=(j<1)):
            rows = []
            for nom in random.sample(["SONATEL","ORANGE","NVDA","BTC","ETH","GOLD"], 4):
                rows.append([nom, random.randint(1000,50000), "+2.5%", 75.0])
            df = pd.DataFrame(rows, columns=["Actif","Prix","Var","IA"])
            st.dataframe(df, use_container_width=True, hide_index=True)

if st.button("♾️ +5 JOURS INFINIS POUR TOUT"):
    st.session_state.nb_jours += 5
    st.rerun()
