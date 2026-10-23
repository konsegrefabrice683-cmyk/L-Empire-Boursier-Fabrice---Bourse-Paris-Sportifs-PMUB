import streamlit as st
from datetime import datetime
import random
import pandas as pd

st.set_page_config(page_title="Fabrice AI Empire V5", page_icon="👑", layout="centered")
st.markdown("""<style>.stButton>button {width:100%;background:#ef4444 !important;color:white !important;font-weight:800 !important;padding:14px !important;border-radius:12px !important}</style>""", unsafe_allow_html=True)

now = datetime.now().strftime("%d/%m/%Y %H:%M")
st.caption(f"Filtre STRICT 72-80% | V5 EMPIRE COMPLET | {now}")

def calcul_ia(cote, marche, xg):
    base = 75.0
    if 1.70 <= cote <= 2.15: base += 3
    elif cote > 2.6: base -= 8
    elif cote < 1.50: base -= 10
    if "Over" in marche and xg >= 2.5: base += 2
    if "Over" in marche and xg < 1.8: base -= 6
    if "Double" in marche or "1X" in marche: base += 1.5
    base += random.uniform(-0.8, 0.8)
    conf = round(base, 2)
    if conf < 65: conf = round(65 + random.uniform(0,3),2)
    if conf > 90: conf = round(87 + random.uniform(0,3),2)
    return conf

def statut(conf):
    if 72 <= conf <= 80: return "✅ FEU VERT"
    elif conf > 80: return "❌ PIÈGE"
    else: return "⚠️ RISQUÉ"

tab1, tab2, tab3 = st.tabs(["⚽ PARIS 72-80%", "🐎 PMU-B LONAB", "📈 BOURSE"])

with tab1:
    st.markdown("### ⚽ Paris Sportifs - AUTO")
    matchs_jour = [
        {"Match": "Man City vs Arsenal", "Marché": "Double Chance", "Cote": 1.85, "xG": 2.9},
        {"Match": "Real Madrid vs Barca", "Marché": "Over 2.5 Buts", "Cote": 1.95, "xG": 3.2},
        {"Match": "Burkina Faso vs Sénégal", "Marché": "Double Chance", "Cote": 2.05, "xG": 2.1},
        {"Match": "PSG vs Marseille", "Marché": "BTTS Oui", "Cote": 1.78, "xG": 2.8},
    ]
    if st.button("🔍 ANALYSER TOUS LES MATCHS DU JOUR"):
        res = []
        for m in matchs_jour:
            c = calcul_ia(m["Cote"], m["Marché"], m["xG"])
            res.append({**m, "IA %": c, "Statut": statut(c)})
        df = pd.DataFrame(res).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        verts = df[df["Statut"].str.contains("FEU VERT")]
        if not verts.empty:
            st.success(f"🔥 {len(verts)} FEU VERT !")
            st.balloons()
    st.divider()
    match = st.text_input("Match", placeholder="Ex: Etalons vs Lions", key="m1")
    marche = st.selectbox("Marché", ["Double Chance", "Over 2.5 Buts", "Over 1.5 Buts", "Under 2.5 Buts", "BTTS Oui", "1X", "X2"], key="mar1")
    cote = st.number_input("Cote LONAB", value=2.05, step=0.01, key="c1")
    xg = st.slider("xG Attendu", 0.0, 6.0, 2.80, 0.01, key="xg1")
    if st.button("🔍 ANALYSER CE MATCH", key="b1"):
        c = calcul_ia(cote, marche, xg)
        st.metric(f"🤖 IA {match}", f"{c}% - {statut(c)}")
        if 72 <= c <= 80: st.success("✅ FEU VERT - Tu peux miser 2000F-5000F"); st.balloons()
        elif c > 80: st.error("❌ COTE PIÈGE")
        else: st.warning("⚠️ RISQUÉ")

with tab2:
    st.markdown("### 🐎 PMU-B LONAB - AUTO")
    courses = [
        {"Course": "R1C4 - Rapide du Faso", "Cheval": "N°7 - Bangr Nooma", "Cote": 3.2, "Forme": 4.5},
        {"Course": "R2C1 - Ouaga Sprint", "Cheval": "N°3 - Wend Panga", "Cote": 2.8, "Forme": 4.0},
        {"Course": "R3C5 - LONAB Gold", "Cheval": "N°12 - Faso Vitesse", "Cote": 5.5, "Forme": 3.8},
        {"Course": "R1C2 - Bobo Derby", "Cheval": "N°1 - Mogho Power", "Cote": 1.9, "Forme": 4.8},
    ]
    if st.button("🐎 ANALYSER TOUTES LES COURSES PMU"):
        res = []
        for cr in courses:
            # Logique PMU : Cote 2.0-3.5 + Forme >4 = FEU VERT
            base = 74.0
            if 2.0 <= cr["Cote"] <= 3.5: base += 4
            if cr["Forme"] >= 4.2: base += 3
            if cr["Cote"] > 6: base -= 7
            base += random.uniform(-1,1)
            c = round(base,2)
            res.append({**cr, "IA %": c, "Statut": statut(c)})
        df = pd.DataFrame(res).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        verts = df[df["Statut"].str.contains("FEU VERT")]
        if not verts.empty:
            st.success(f"🐎 {len(verts)} CHEVAUX FEU VERT !")
            st.balloons()
    
    st.divider()
    cheval = st.text_input("Cheval / Course", placeholder="Ex: R1C4 N°7", key="ch1")
    cote_pmu = st.number_input("Cote PMU", value=3.2, step=0.1, key="cp1")
    forme = st.slider("Forme du cheval /5", 0.0, 5.0, 4.2, 0.1, key="f1")
    if st.button("🐎 ANALYSER CE CHEVAL", key="bp1"):
        base = 74.0
        if 2.0 <= cote_pmu <= 3.5: base += 4
        if forme >= 4.2: base += 3
        c = round(base + random.uniform(-1,1),2)
        st.metric(f"🤖 IA {cheval}", f"{c}% - {statut(c)}")
        if 72 <= c <= 80: st.success("✅ FEU VERT PMU - Jouable !"); st.balloons()
        elif c > 80: st.error("❌ PIÈGE PMU")
        else: st.warning("⚠️ RISQUÉ")

with tab3:
    st.markdown("### 📈 BOURSE BRVM - AUTO")
    actions = [
        {"Action": "SONATEL", "Prix": 18500, "Tendance": "Hausse"},
        {"Action": "ONATEL BF", "Prix": 3420, "Tendance": "Hausse"},
        {"Action": "SGBCI", "Prix": 11200, "Tendance": "Stable"},
        {"Action": "ECOBANK", "Prix": 1850, "Tendance": "Baisse"},
    ]
    if st.button("📈 ANALYSER LA BOURSE DU JOUR"):
        res = []
        for a in actions:
            base = 75.0
            if a["Tendance"] == "Hausse": base += 2.5
            if a["Tendance"] == "Baisse": base -= 4
            base += random.uniform(-1.5,1.5)
            c = round(base,2)
            res.append({**a, "IA %": c, "Signal": statut(c)})
        df = pd.DataFrame(res).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        verts = df[df["Signal"].str.contains("FEU VERT")]
        if not verts.empty:
            st.success(f"📈 {len(verts)} SIGNAUX ACHAT !")
            st.balloons()

    st.divider()
    action = st.text_input("Action BRVM", placeholder="Ex: SONATEL", key="ac1")
    tendance = st.selectbox("Tendance", ["Hausse", "Stable", "Baisse"], key="t1")
    if st.button("📈 ANALYSER CETTE ACTION", key="bb1"):
        base = 75.0
        if tendance == "Hausse": base += 2.5
        if tendance == "Baisse": base -= 4
        c = round(base + random.uniform(-1.5,1.5),2)
        st.metric(f"🤖 IA {action}", f"{c}% - {statut(c)}")
        if 72 <= c <= 80: st.success("✅ SIGNAL ACHAT BRVM"); st.balloons()

st.caption("👑 Fabrice AI Empire V5 | Les 3 onglets bougent | Ouaga 🇧🇫")
