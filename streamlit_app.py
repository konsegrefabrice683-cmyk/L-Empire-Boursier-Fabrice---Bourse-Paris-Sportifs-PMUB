import streamlit as st
from datetime import datetime
import random
import pandas as pd

st.set_page_config(page_title="Fabrice V10.3", layout="wide")
st.title("FABRICE EMPIRE V10.3 - 20 MATCHS + PMU + BOURSE")
st.write(datetime.now().strftime("%d/%m/%Y %H:%M"))
st.write("---")

def statut(c):
    if 72 <= c <= 80:
        return "FEU VERT"
    if c > 80:
        return "PIEGE"
    return "RISQUE"

def calc(cote):
    b = 75.0
    if 1.7 <= cote <= 2.15:
        b += 3
    if cote > 2.6:
        b -= 8
    b += random.uniform(-1,1)
    c = round(b,2)
    if c < 65:
        c = 66 + random.uniform(0,2)
    if c > 90:
        c = 87 + random.uniform(0,2)
    return round(c,2)

tab1, tab2, tab3 = st.tabs(["PARIS 20", "PMU", "BOURSE"])

with tab1:
    st.write("20 MATCHS")
    matchs = [
        ["Man City vs Arsenal", 1.85],
        ["Liverpool vs Chelsea", 1.88],
        ["Man Utd vs Tottenham", 1.72],
        ["Real vs Barca", 1.95],
        ["Atletico vs Sevilla", 1.75],
        ["PSG vs Marseille", 1.78],
        ["Lyon vs Monaco", 1.92],
        ["Bayern vs Dortmund", 1.65],
        ["Leverkusen vs Leipzig", 1.8],
        ["Inter vs Milan", 1.7],
        ["Juve vs Napoli", 1.82],
        ["Burkina vs Senegal", 2.05],
        ["Al Ahly vs Wydad", 1.65],
        ["ES Tunis vs Mamelodi", 1.85],
        ["Raja vs Simba", 1.9],
        ["Etalons U23 vs Ghana", 2.15],
        ["AS Douanes vs Salitas", 1.55],
        ["Rahimo vs Majestic", 1.7],
        ["Man City vs Real", 1.6],
        ["Miami vs Galaxy", 1.6]
    ]
    if st.button("ANALYSER 20 MATCHS"):
        res = []
        for m in matchs:
            c = calc(m[1])
            res.append({"Match": m[0], "Cote": m[1], "IA": c, "Statut": statut(c)})
        df = pd.DataFrame(res).sort_values(by="IA", ascending=False)
        st.dataframe(df, use_container_width=True)
        verts = df[df["Statut"] == "FEU VERT"]
        st.success(f"{len(verts)} FEU VERT")
        for _, r in verts.iterrows():
            st.code(f"{r['Match']} Cote {r['Cote']} IA {r['IA']}% FEU VERT Code {random.randint(10000,99999)}")
        st.balloons()
