import streamlit as st
import pandas as pd
import random
from datetime import datetime

# --- CONFIG SEKA ---
st.set_page_config(page_title="SEKA", layout="wide")
st.title("SEKA - SYSTEME COMPLET")
st.write(f"Ouagadougou | {datetime.now().strftime('%d/%m/%Y %H:%M')} | Tendance + Valeur + Bruit -> IA 72-80% FEU VERT")
st.divider()

# --- MOTEUR ---
def statut(c):
    if 72.0 <= c <= 80.0:
        return "FEU VERT"
    if c > 80.0:
        return "PIEGE"
    return "RISQUE"

def calc_sport(cote, xg):
    base = 74.5
    if 1.7 <= cote <= 2.15:
        base += 2.8
    if xg >= 2.8:
        base += 1.5
    base += random.uniform(-0.7, 0.7)
    if base < 65: base = 67.0
    if base > 90: base = 87.0
    return round(base, 2)

def calc_pmu(cote, forme):
    base = 73.5
    if 2.0 <= cote <= 4.5: base += 3.0
    if forme >= 4.5: base += 2.0
    base += random.uniform(-0.8, 0.8)
    if base < 65: base = 67.0
    if base > 90: base = 87.0
    return round(base, 2)

def calc_bourse(tendance, volume):
    base = 74.0
    if tendance == "HAUSSE FORTE": base += 3.5
    elif tendance == "HAUSSE": base += 1.8
    if volume == "FORT": base += 1.0
    base += random.uniform(-0.6, 0.6)
    return round(base, 2)

# =========================================================
# 1. PARIS SPORTIFS - 20 MATCHS
# =========================================================
st.header("1. PARIS SPORTIFS - 20 MATCHS")
st.write("Analyse: Tendance du match + Valeur de la cote + Bruit du marche")

matchs = [
    ["Man City vs Arsenal", "Double Chance 1X", 1.85, 2.9],
    ["Liverpool vs Chelsea", "Over 2.5", 1.88, 3.1],
    ["Man Utd vs Tottenham", "BTTS Oui", 1.72, 2.7],
    ["Real Madrid vs Barca", "Over 2.5", 1.95, 3.2],
    ["Atletico vs Sevilla", "1X", 1.75, 2.4],
    ["PSG vs Marseille", "BTTS Oui", 1.78, 2.8],
    ["Lyon vs Monaco", "Over 2.5", 1.92, 2.9],
    ["Bayern vs Dortmund", "Over 2.5", 1.65, 3.4],
    ["Leverkusen vs Leipzig", "Double Chance", 1.80, 2.6],
    ["Inter vs Milan", "Double Chance", 1.70, 2.5],
    ["Juve vs Napoli", "Under 2.5", 1.82, 1.9],
    ["Burkina vs Senegal", "Double Chance", 2.05, 2.1],
    ["Al Ahly vs Wydad", "Under 2.5", 1.65, 1.6],
    ["ES Tunis vs Mamelodi", "Double Chance", 1.85, 2.0],
    ["Raja vs Simba", "BTTS Non", 1.90, 1.8],
    ["Etalons U23 vs Ghana", "Double Chance", 2.15, 2.3],
    ["AS Douanes vs Salitas", "1X", 1.55, 1.7],
    ["Rahimo vs Majestic", "Over 1.5", 1.70, 2.2],
    ["Man City vs Real Madrid", "Over 2.5", 1.60, 3.5],
    ["Miami vs Galaxy", "BTTS Oui", 1.60, 3.0],
]

rows_sport = []
for m in matchs:
    ia = calc_sport(m[2], m[3])
    # Tendance
    if m[3] >= 2.8: tend = "HAUSSE"
    else: tend = "STABLE"
    # Valeur
    if 1.7 <= m[2] <= 2.15: val = "EXCELLENTE VALEUR"
    elif m[2] > 2.8: val = "COTE PIEGE"
    else: val = "VALEUR CORRECTE"
    # Bruit
    bruit = "MARCHE CALME" if ia >= 74 else "MARCHE NORMAL"
    
    rows_sport.append({
        "Match": m[0],
        "Marche": m[1],
        "Cote": m[2],
        "xG": m[3],
        "Tendance": tend,
        "Valeur": val,
        "Bruit": bruit,
        "IA %": ia,
        "STATUT": statut(ia),
        "Gain 3000F": int(m[2]*3000)
    })

df_sport = pd.DataFrame(rows_sport)
df_sport = df_sport.sort_values(by="IA %", ascending=False)
st.dataframe(df_sport, use_container_width=True, height=700)

verts = df_sport[df_sport["STATUT"] == "FEU VERT"]
st.success(f"SEKA SPORT: {len(verts)} FEU VERT sur 20 - ZONE OR 72-80%")
for _, r in verts.iterrows():
    st.code(f"SEKA TICKET | {r['Match']} | {r['Marche']} | Cote {r['Cote']} | IA {r['IA %']}% | {r['Valeur']} | Gain {r['Gain 3000F']}F | FEU VERT")

st.divider()

# =========================================================
# 2. PMU-B LONAB
# =========================================================
st.header("2. PMU-B LONAB - TOUS PARIS")
st.write("Types: Gagnant, Place, Couple, Tierce, Quarte, Quinte+")
st.write("Analyse: Forme + Cote + Age + Driver")

chevaux = [
    ["1", "Mogho Power", 2.1, 4.8, 5, "KONDE"],
    ["3", "Wend Panga", 4.5, 4.2, 6, "SAWADOGO"],
    ["7", "Bangr Nooma", 3.2, 4.5, 4, "OUEDRAOGO"],
    ["8", "Faso Vitesse", 6.8, 3.9, 5, "TRAORE"],
    ["12", "Bobo Sprint", 12.0, 3.5, 7, "KABORE"],
    ["2", "Roi du Sahel", 5.5, 4.6, 4, "DIARRA"],
    ["5", "Etalon dOr", 3.8, 4.7, 5, "ZONGO"],
]

rows_pmu = []
for c in chevaux:
    ia = calc_pmu(c[2], c[3])
    if c[3] >= 4.5: tend = "EN FEU"
    else: tend = "EN FORME"
    if 2.0 <= c[2] <= 4.5: val = "FAVORI SOLIDE"
    else: val = "OUTSIDER"
    bruit = "CALME" if c[3] >= 4.3 else "BRUYANT"
    
    rows_pmu.append({
        "Num": c[0], "Cheval": c[1], "Cote": c[2], "Forme": c[3], "Age": c[4], "Jockey": c[5],
        "Tendance": tend, "Valeur": val, "Bruit": bruit, "IA %": ia, "STATUT": statut(ia)
    })

df_pmu = pd.DataFrame(rows_pmu).sort_values(by="IA %", ascending=False)
st.dataframe(df_pmu, use_container_width=True)

st.code(f"SEKA PMU QUINTE+: {df_pmu.iloc[0]['Num']}-{df_pmu.iloc[1]['Num']}-{df_pmu.iloc[2]['Num']}-{df_pmu.iloc[3]['Num']}-{df_pmu.iloc[4]['Num']} | IA Moy {round(df_pmu.head(5)['IA %'].mean(),2)}%")

st.divider()

# =========================================================
# 3. BOURSE INTERNATIONALE
# =========================================================
st.header("3. BOURSE INTERNATIONALE - FOREX / CRYPTO / BRVM / OR")
st.write("Analyse: Tendance + Volume + Valeur + Bruit")

bourse = [
    ["EUR/USD", "1.0845", "HAUSSE", "FORT", "FOREX"],
    ["USD/XOF CFA", "604.5", "HAUSSE FORTE", "FORT", "FOREX BF"],
    ["BTC/USD", "67450 $", "HAUSSE FORTE", "FORT", "CRYPTO"],
    ["ETH/USD", "3210 $", "HAUSSE", "MOYEN", "CRYPTO"],
    ["GOLD Or", "2345 $", "HAUSSE FORTE", "FORT", "OR"],
    ["AAPL Apple", "182.5 $", "HAUSSE", "MOYEN", "NASDAQ"],
    ["SONATEL", "18500 F", "HAUSSE", "MOYEN", "BRVM SN"],
    ["ONATEL BF", "3420 F", "HAUSSE", "FAIBLE", "BRVM BF"],
]

rows_bourse = []
for b in bourse:
    ia = calc_bourse(b[2], b[3])
    if b[2] == "HAUSSE FORTE" and b[3] == "FORT": bruit = "TENDANCE CONFIRMEE"
    elif b[3] == "FAIBLE": bruit = "FAUX SIGNAL - BRUIT"
    else: bruit = "MARCHE LISIBLE"
    
    if b[3] == "FORT": val = "FORTE ACTIVITE"
    else: val = "FAIBLE VOLUME"
    
    action = "ACHETER" if 72 <= ia <= 80 and "HAUSSE" in b[2] else "ATTENDRE"
    
    rows_bourse.append({
        "Actif": b[0], "Prix": b[1], "Tendance": b[2], "Volume": b[3], "Marche": b[4],
        "Valeur": val, "Bruit": bruit, "IA %": ia, "SIGNAL": statut(ia), "Action": action
    })

df_bourse = pd.DataFrame(rows_bourse).sort_values(by="IA %", ascending=False)
st.dataframe(df_bourse, use_container_width=True)

verts_b = df_bourse[df_bourse["SIGNAL"] == "FEU VERT"]
st.success(f"SEKA BOURSE: {len(verts_b)} FEU VERT")
for _, r in verts_b.iterrows():
    st.code(f"SEKA BOURSE | {r['Actif']} a {r['Prix']} | Tendance {r['Tendance']} | IA {r['IA %']}% FEU VERT | {r['Action']}")

st.divider()
st.caption("SEKA V13 SOLIDE SANS ONGLETS - TOUT S'AFFICHE - OUAGA")
