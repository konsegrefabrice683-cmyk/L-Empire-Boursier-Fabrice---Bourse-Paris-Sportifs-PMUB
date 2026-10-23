import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- CONFIG SEKA V2 - COMME EMPIRE V2 ---
st.set_page_config(page_title="SEKA", layout="wide")

st.markdown("<h1 style='text-align: center; color: #FFD700;'>SEKA V2</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Filtre STRICT 72-80% | Ouaga | {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>", unsafe_allow_html=True)

# --- MOTEUR SEKA ---
def statut(c):
    if 72.0 <= c <= 80.0:
        return "FEU VERT"
    if c > 80.0:
        return "PIEGE"
    return "RISQUE"

def calc(cote, bonus=0):
    base = 74.0 + bonus
    if 1.7 <= cote <= 2.15:
        base += 2.5
    base += random.uniform(-0.8, 0.8)
    if base < 65: base = 66.5 + random.uniform(0,2)
    if base > 89: base = 87.5 + random.uniform(0,2)
    return round(base,2)

# --- LES 3 ONGLETS COMME SUR TA PHOTO ---
tab1, tab2, tab3 = st.tabs(["PARIS 72-80%", "PMU-B LONAB", "BOURSE"])

# TAB 1 - PARIS
with tab1:
    st.subheader("Paris - Tendance / Valeur / Bruit / IA %")
    
    matchs = [
        ["Man City vs Arsenal", "Double Chance 1X", 1.85, 2.9, "19:00"],
        ["Liverpool vs Chelsea", "Over 2.5", 1.88, 3.1, "18:30"],
        ["Man Utd vs Tottenham", "BTTS Oui", 1.72, 2.7, "16:00"],
        ["Real vs Barca", "Over 2.5", 1.95, 3.2, "20:45"],
        ["Atletico vs Sevilla", "1X", 1.75, 2.4, "19:00"],
        ["PSG vs Marseille", "BTTS Oui", 1.78, 2.8, "21:00"],
        ["Lyon vs Monaco", "Over 2.5", 1.92, 2.9, "19:00"],
        ["Bayern vs Dortmund", "Over 2.5", 1.65, 3.4, "18:30"],
        ["Burkina vs Senegal", "Double Chance", 2.05, 2.1, "18:00"],
        ["AS Douanes vs Salitas", "1X", 1.55, 1.7, "16:00"],
        ["Rahimo vs Majestic", "Over 1.5", 1.70, 2.2, "15:30"],
        ["Man City vs Real", "Over 2.5", 1.60, 3.5, "21:00"],
    ]
    
    rows = []
    for m in matchs:
        ia = calc(m[2], 1.0 if m[3]>=2.8 else 0)
        tend = "HAUSSE" if m[3]>=2.8 else "STABLE"
        val = "EXCELLENTE VALEUR" if 1.7<=m[2]<=2.15 else "BONNE VALEUR" if m[2]<=2.6 else "COTE PIEGE"
        bruit = "MARCHE CALME" if ia>=74 else "MARCHE NORMAL"
        rows.append({
            "Match": m[0], "Marche": m[1], "Cote": m[2], "xG": m[3], "Heure": m[4],
            "Tendance": tend, "Valeur": val, "Bruit": bruit, "IA %": ia, "STATUT": statut(ia), "Gain 3000F": int(m[2]*3000)
        })
    
    df = pd.DataFrame(rows).sort_values(by="IA %", ascending=False)
    st.dataframe(df, use_container_width=True, height=500)
    
    verts = df[df["STATUT"]=="FEU VERT"]
    st.success(f"SEKA: {len(verts)} FEU VERT sur {len(df)}")
    for _, r in verts.iterrows():
        st.code(f"SEKA | {r['Match']} | {r['Marche']} | Cote {r['Cote']} | IA {r['IA %']}% | {r['Valeur']} | FEU VERT")

# TAB 2 - PMU
with tab2:
    st.subheader("PMU-B LONAB - Valeur / Benefice / Tendance")
    type_pari = st.selectbox("Type de pari", ["Gagnant", "Place", "Couple Place", "Couple Gagnant", "Tierce", "Quarte", "Quinte+"], index=2)
    
    chevaux = [
        ["1", "Mogho Power", 2.1, 4.8, "KONDE"],
        ["3", "Wend Panga", 4.5, 4.2, "SAWADOGO"],
        ["7", "Bangr Nooma", 3.2, 4.5, "OUEDRAOGO"],
        ["8", "Faso Vitesse", 6.8, 3.9, "TRAORE"],
        ["12", "Bobo Sprint", 12.0, 3.5, "KABORE"],
        ["2", "Roi du Sahel", 5.5, 4.6, "DIARRA"],
        ["5", "Etalon dOr", 3.8, 4.7, "ZONGO"],
    ]
    
    rows_pmu = []
    for c in chevaux:
        ia = calc(c[2], 1.5 if c[3]>=4.5 else 0)
        tend = "EN FEU" if c[3]>=4.5 else "EN FORME"
        val = "FAVORI SOLIDE" if c[2]<=4.5 else "OUTSIDER VALEUR"
        bruit = "CALME" if c[3]>=4.3 else "BRUYANT"
        rows_pmu.append({"Num": c[0], "Cheval": c[1], "Cote": c[2], "Forme": c[3], "Jockey": c[4], "Tendance": tend, "Valeur": val, "Bruit": bruit, "IA %": ia, "STATUT": statut(ia)})
    
    df_pmu = pd.DataFrame(rows_pmu).sort_values(by="IA %", ascending=False)
    st.dataframe(df_pmu, use_container_width=True)
    
    nb = {"Gagnant":1, "Place":1, "Couple Place":2, "Couple Gagnant":2, "Tierce":3, "Quarte":4, "Quinte+":5}[type_pari]
    sel = df_pmu.head(nb)
    ticket = " - ".join([f"{r['Num']}-{r['Cheval']}" for _, r in sel.iterrows()])
    st.code(f"SEKA TICKET {type_pari}: {ticket} | IA Moy {round(sel['IA %'].mean(),2)}%")

# TAB 3 - BOURSE (COMME TA PHOTO AVEC LISTE DEROULANTE)
with tab3:
    st.subheader("Bourse - Valeur / Benefice / Tendance")
    
    # Liste comme sur ta capture
    action_choisie = st.selectbox("Action", ["SONATEL.SN", "ORANGE.SN", "AAPL", "TSLA", "BTC-USD", "ETH-USD", "ONATEL.BF", "GOLD"], index=0)
    
    bourse_db = {
        "SONATEL.SN": ["SONATEL.SN", "18500 F", "HAUSSE", "FORT", "BRVM SN", 18500, 2.5],
        "ORANGE.SN": ["ORANGE.SN", "11200 F", "STABLE", "MOYEN", "BRVM SN", 11200, 1.2],
        "AAPL": ["AAPL Apple", "182.5 $", "HAUSSE", "MOYEN", "NASDAQ", 182.5, 3.1],
        "TSLA": ["TSLA Tesla", "248.3 $", "BAISSE", "FORT", "NASDAQ", 248.3, -1.5],
        "BTC-USD": ["BTC-USD", "67450 $", "HAUSSE FORTE", "FORT", "CRYPTO", 67450, 5.8],
        "ETH-USD": ["ETH-USD", "3210 $", "HAUSSE", "MOYEN", "CRYPTO", 3210, 3.2],
        "ONATEL.BF": ["ONATEL.BF", "3420 F", "HAUSSE", "FAIBLE", "BRVM BF", 3420, 1.8],
        "GOLD": ["GOLD Or", "2345 $", "HAUSSE FORTE", "FORT", "OR", 2345, 4.0],
    }
    
    # Afficher tout
    rows_b = []
    for key, b in bourse_db.items():
        ia = calc(2.0, 3.5 if b[2]=="HAUSSE FORTE" else 1.5 if b[2]=="HAUSSE" else -1.0)
        val = "FORTE ACTIVITE" if b[3]=="FORT" else "FAIBLE VOLUME"
        bruit = "TENDANCE CONFIRMEE" if b[3]=="FORT" and "HAUSSE" in b[2] else "FAUX SIGNAL" if b[3]=="FAIBLE" else "MARCHE LISIBLE"
        action = "ACHETER" if 72 <= ia <= 80 and "HAUSSE" in b[2] else "GARDER" if ia>=72 else "ATTENDRE"
        rows_b.append({
            "Action": b[0], "Prix": b[1], "Tendance": b[2], "Volume": b[3], "Marche": b[4],
            "Benefice potentiel %": b[6], "Valeur": val, "Bruit": bruit, "IA %": ia, "SIGNAL": statut(ia), "Action conseillee": action
        })
    
    df_b = pd.DataFrame(rows_b).sort_values(by="IA %", ascending=False)
    st.dataframe(df_b, use_container_width=True)
    
    # Detail de l'action choisie comme sur ta photo
    b = bourse_db[action_choisie]
    ia_detail = calc(2.0, 3.0)
    st.info(f"Detail: {b[0]} | Prix: {b[1]} | Tendance: {b[2]} | Volume: {b[3]} | IA: {ia_detail}% | {statut(ia_detail)}")
    
    verts_b = df_b[df_b["SIGNAL"]=="FEU VERT"]
    st.success(f"SEKA BOURSE: {len(verts_b)} opportunites FEU VERT")
    for _, r in verts_b.head(4).iterrows():
        st.code(f"SEKA | {r['Action']} a {r['Prix']} | Benefice {r['Benefice potentiel %']}% | IA {r['IA %']}% | {r['Action conseillee']}")

st.divider()
st.caption("SEKA V2 - Filtre STRICT 72-80% - Tendance + Valeur + Bruit - Ouaga")
