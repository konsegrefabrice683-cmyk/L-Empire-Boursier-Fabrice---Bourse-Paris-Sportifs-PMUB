import streamlit as st
import pandas as pd
import math
from datetime import datetime

st.set_page_config(page_title="SEKA ULTRA", layout="wide")
st.title("SEKA ULTRA SOLIDE V16")
st.caption(f"ULTRA = MARGE RETIREE + ELO + VALUE + KELLY | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

def remove_vig(cotes):
    somme = sum([1/c for c in cotes])
    marge = (somme - 1) * 100
    probas = [(1/c) / somme for c in cotes]
    return probas, marge

def proba_ultra(xg, elo_dom, elo_ext, forme_dom, forme_ext):
    elo_diff = (elo_dom - elo_ext) / 400
    proba_elo = 1 / (1 + 10 ** (-elo_diff))
    xg_diff = (xg - 2.0) * 0.10
    forme_diff = (forme_dom - forme_ext) * 0.05
    proba = proba_elo * 0.60 + 0.20 + xg_diff + forme_diff
    proba = max(0.15, min(proba, 0.85))
    confiance = 0.75 - abs(0.50 - proba) * 0.3
    return proba, confiance

def kelly(proba, cote):
    b = cote - 1
    q = 1 - proba
    k = (b * proba - q) / b if b != 0 else 0
    k = max(0, k)
    mise = 100000 * k * 0.25
    return k*100, mise

def analyse_match(nom, cote_lonab, cotes_marche, xg, elo_dom, elo_ext, fd, fe):
    probas_sans_marge, marge = remove_vig(cotes_marche)
    proba_marche = probas_sans_marge[0]
    proba_reelle, confiance = proba_ultra(xg, elo_dom, elo_ext, fd, fe)
    cote_juste = 1 / proba_reelle
    value = (cote_lonab * proba_reelle - 1) * 100
    ecart = (proba_reelle - proba_marche) * 100
    kelly_pct, mise = kelly(proba_reelle, cote_lonab)
    ia = proba_reelle * 100 * (0.90 + confiance*0.20)
    if value >= 8:
        ia += 3
    elif value < 0:
        ia -= 10
    ia = max(50, min(ia, 92))
    if 72 <= ia <= 80 and value >= 5 and kelly_pct >= 2:
        statut = "FEU VERT ULTRA"
    elif value < 0:
        statut = "NO VALUE"
    elif ia > 82:
        statut = "PIEGE"
    else:
        statut = "ATTENTE"
    return {
        "Match": nom,
        "Cote LONAB": cote_lonab,
        "Marge %": round(marge,1),
        "Proba Marche": f"{proba_marche*100:.1f}%",
        "Proba Ultra": f"{proba_reelle*100:.1f}%",
        "Cote Juste": round(cote_juste,2),
        "Ecart %": round(ecart,1),
        "Value %": round(value,1),
        "Confiance": round(confiance*100,1),
        "Kelly %": round(kelly_pct,1),
        "Mise 100k": f"{int(mise)}F",
        "IA %": round(ia,1),
        "STATUT": statut
    }

tab1, tab2, tab3 = st.tabs(["ULTRA PARIS", "PMU ULTRA", "BOURSE ULTRA"])

with tab1:
    st.subheader("ULTRA PARIS - On bat le marche")
    matchs = [
        ["Man City vs Arsenal", 1.85, [2.10, 3.40, 3.20], 2.9, 1850, 1820, 4.4, 4.1],
        ["Liverpool vs Chelsea", 1.88, [1.90, 3.60, 4.00], 3.1, 1830, 1750, 4.2, 3.2],
        ["Real vs Barca", 1.95, [2.20, 3.50, 3.10], 3.2, 1880, 1840, 4.5, 4.3],
        ["Burkina vs Senegal", 2.05, [2.05, 3.10, 3.80], 2.1, 1450, 1650, 4.1, 4.4],
        ["AS Douanes vs Salitas", 1.55, [1.55, 3.80, 6.00], 1.7, 1200, 1000, 4.2, 3.0],
        ["Man City vs Real", 1.60, [1.80, 3.80, 4.50], 3.5, 1860, 1880, 4.5, 4.5],
    ]
    rows = [analyse_match(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7]) for m in matchs]
    df = pd.DataFrame(rows).sort_values(by="IA %", ascending=False)
    st.dataframe(df, use_container_width=True, height=400)
    verts = df[df["STATUT"]=="FEU VERT ULTRA"]
    st.success(f"{len(verts)} FEU VERT ULTRA trouves")
    for _, r in verts.iterrows():
        st.code(f"{r['Match']} | LONAB {r['Cote LONAB']} JUSTE {r['Cote Juste']} | Value {r['Value %']}% Ecart {r['Ecart %']}% | Kelly {r['Kelly %']}% Mise {r['Mise 100k']} | IA {r['IA %']}% ULTRA")

with tab2:
    st.subheader("PMU ULTRA")
    chevaux = [
        ["1 Mogho Power", 2.1, 4.8],
        ["7 Bangr Nooma", 3.2, 4.5],
        ["5 Etalon dOr", 3.8, 4.7],
    ]
    rows_p = []
    for c in chevaux:
        proba = c[2] / 7.5
        juste = 1/proba
        value = (c[1]*proba -1)*100
        ia = proba*100 + (3 if value>5 else 0)
        statut = "FEU VERT ULTRA" if 72<=ia<=80 and value>=5 else "RISQUE"
        rows_p.append({"Cheval": c[0], "Cote LONAB": c[1], "Cote Juste": round(juste,2), "Value %": round(value,1), "IA %": round(ia,1), "STATUT": statut})
    st.dataframe(pd.DataFrame(rows_p), use_container_width=True)

with tab3:
    st.subheader("BOURSE ULTRA")
    bourse = [
        ["SONATEL.SN", 18500, 18000, "FORT", 62],
        ["BTC-USD", 67450, 62000, "FORT", 78],
        ["ONATEL.BF", 3420, 3350, "FAIBLE", 45],
        ["GOLD", 2345, 2200, "FORT", 65],
    ]
    rows_b = []
    for b in bourse:
        var = (b[1]-b[2])/b[2]*100
        rsi = b[4]
        if var>3 and b[3]=="FORT" and rsi<70:
            ia = 76.5
            statut = "FEU VERT ULTRA"
            act = "ACHETER"
        elif rsi>=70:
            ia = 83
            statut = "SURACHETE PIEGE"
            act = "VENDRE"
        else:
            ia = 65
            statut = "ATTENTE"
            act = "ATTENDRE"
        rows_b.append({"Actif": b[0], "Prix": b[1], "MM20": b[2], "Var%": round(var,1), "Vol": b[3], "RSI": rsi, "IA%": ia, "STATUT": statut, "Action": act})
    st.dataframe(pd.DataFrame(rows_b), use_container_width=True)

st.divider()
st.caption("SEKA ULTRA V16 - Verifiable - FABRICE OUAGA")
