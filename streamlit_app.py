import streamlit as st
from datetime import datetime
import random, pandas as pd

st.set_page_config(page_title="Fabrice Empire V10.2", layout="wide")
st.markdown("### FABRICE EMPIRE V10.2 | 20 MATCHS + PMU PRO + BOURSE | " + datetime.now().strftime("%d/%m %H:%M"))
st.write("---")

def statut(c):
    if 72 <= c <= 80:
        return "FEU VERT"
    elif c > 80:
        return "PIEGE"
    else:
        return "RISQUE"

def calc_paris(cote, marche, xg):
    b = 75.0
    if 1.7 <= cote <= 2.15:
        b += 3
    elif cote > 2.6:
        b -= 8
    elif cote < 1.5:
        b -= 10
    if "Over" in marche and xg >= 2.5:
        b += 2
    b += random.uniform(-0.8, 0.8)
    c = round(b, 2)
    if c < 65:
        c = round(65 + random.uniform(0, 3), 2)
    if c > 90:
        c = round(86 + random.uniform(0, 4), 2)
    return c

def calc_pmu(cotes, formes, typ):
    b = 74.0
    avg_c = sum(cotes)/len(cotes) if cotes else 3.0
    avg_f = sum(formes)/len(formes) if formes else 4.0
    if typ == "Gagnant" and 1.8 <= avg_c <= 3.5:
        b += 5
    if typ == "Place":
        b += 5
    if "Couple" in typ:
        b += 3
    if avg_f >= 4.2:
        b += 2
    b += random.uniform(-1, 1)
    c = round(b, 2)
    if c < 65:
        c = round(65 + random.uniform(0, 3), 2)
    if c > 90:
        c = round(86 + random.uniform(0, 4), 2)
    return c

def calc_bourse(t, v):
    b = 75.0
    if t == "Hausse Forte":
        b += 4
    elif t == "Hausse":
        b += 2.5
    elif "Baisse" in t:
        b -= 3
    b += random.uniform(-1, 1)
    return round(b, 2)

tab1, tab2, tab3 = st.tabs(["PARIS 20 MATCHS", "PMU-B PRO", "BOURSE WORLD"])

with tab1:
    st.subheader("20 MATCHS - Analyse Auto")
    matchs = [
        ["Man City vs Arsenal", "Double Chance", 1.85, 2.9, "19:00", "PL"],
        ["Liverpool vs Chelsea", "Over 2.5", 1.88, 3.1, "18:30", "PL"],
        ["Man Utd vs Tottenham", "BTTS Oui", 1.72, 2.7, "16:00", "PL"],
        ["Real vs Barca", "Over 2.5", 1.95, 3.2, "20:45", "Liga"],
        ["Atletico vs Sevilla", "Double Chance", 1.75, 2.4, "19:00", "Liga"],
        ["PSG vs Marseille", "BTTS Oui", 1.78, 2.8, "21:00", "L1"],
        ["Lyon vs Monaco", "Over 2.5", 1.92, 2.9, "19:00", "L1"],
        ["Bayern vs Dortmund", "Over 2.5", 1.65, 3.4, "18:30", "Bun"],
        ["Leverkusen vs Leipzig", "Double Chance", 1.8, 2.6, "17:30", "Bun"],
        ["Inter vs Milan", "Double Chance", 1.7, 2.5, "20:45", "SerieA"],
        ["Juve vs Napoli", "Under 2.5", 1.82, 1.9, "18:00", "SerieA"],
        ["Burkina vs Senegal", "Double Chance", 2.05, 2.1, "18:00", "CAN"],
        ["Al Ahly vs Wydad", "Under 2.5", 1.65, 1.6, "16:00", "CAF"],
        ["ES Tunis vs Mamelodi", "Double Chance", 1.85, 2.0, "15:00", "CAF"],
        ["Raja vs Simba", "BTTS Non", 1.9, 1.8, "20:00", "CAF"],
        ["Etalons U23 vs Ghana", "Double Chance", 2.15, 2.3, "16:30", "U23"],
        ["AS Douanes vs Salitas", "1X", 1.55, 1.7, "16:00", "BF"],
        ["Rahimo vs Majestic", "Over 1.5", 1.7, 2.2, "15:30", "BF"],
        ["Man City vs Real Madrid", "Over 2.5", 1.6, 3.5, "21:00", "UCL"],
        ["Miami vs Galaxy", "BTTS Oui", 1.6, 3.0, "02:00", "MLS"],
    ]
    if st.button("ANALYSER LES 20 MATCHS"):
        data = []
        for m in matchs:
            c = calc_paris(m[2], m[1], m[3])
            data.append({"Match": m[0], "Marche": m[1], "Cote": m[2], "xG": m[3], "Heure": m[4], "League": m[5], "IA %": c, "Statut": statut(c)})
        df = pd.DataFrame(data).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True)
        verts = df[df["Statut"] == "FEU VERT"]
        st.success(f"{len(verts)} FEU VERT SUR 20 MATCHS !")
        for _, r in verts.iterrows():
            code = random.randint(10000,99999)
            st.code(f"TICKET: {r['Match']} | {r['Marche']} Cote {r['Cote']} IA {r['IA %']}% Code LONAB-{code} Gain {int(3000*r['Cote'])}F FEU VERT")
        st.balloons()

with tab2:
    st.subheader("PMU-B L
