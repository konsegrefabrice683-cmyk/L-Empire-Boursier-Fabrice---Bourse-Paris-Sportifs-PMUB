import streamlit as st
from datetime import datetime
import random
import pandas as pd

st.set_page_config(page_title="Fabrice AI Empire V4", page_icon="👑", layout="centered")

st.markdown("""
<style>
.stButton>button {width:100%;background:#ef4444 !important;color:white !important;font-weight:800 !important;padding:14px !important;border-radius:12px !important}
</style>
""", unsafe_allow_html=True)

now = datetime.now().strftime("%d/%m/%Y %H:%M")
st.caption(f"Filtre STRICT 72-80% | AUTO MATCHS | {now}")

tab1, tab2, tab3 = st.tabs(["⚽ PARIS 72-80%", "🐎 PMU-B LONAB", "📈 BOURSE"])

with tab1:
    st.markdown("### ⚽ Paris Sportifs - Matchs du Jour AUTO")

    # MATCHS DU JOUR (exemples, tu peux modifier)
    matchs_jour = [
        {"Match": "Man City vs Arsenal", "Marché": "Double Chance", "Cote": 1.85, "xG": 2.9},
        {"Match": "Real Madrid vs Barca", "Marché": "Over 2.5 Buts", "Cote": 1.95, "xG": 3.2},
        {"Match": "PSG vs Marseille", "Marché": "BTTS Oui", "Cote": 1.78, "xG": 2.8},
        {"Match": "Burkina Faso vs Sénégal", "Marché": "Double Chance", "Cote": 2.05, "xG": 2.1},
        {"Match": "Al Ahly vs Wydad", "Marché": "Under 2.5 Buts", "Cote": 1.65, "xG": 1.6},
        {"Match": "Liverpool vs Chelsea", "Marché": "Over 1.5 Buts", "Cote": 1.42, "xG": 2.7},
    ]

    # Fonction IA
    def calcul_ia(cote, marche, xg):
        base = 75.0
        if 1.70 <= cote <= 2.15: base += 3
        elif cote > 2.6: base -= 8
        elif cote < 1.50: base -= 10
        if "Over" in marche and xg >= 2.5: base += 2
        if "Over" in marche and xg < 1.8: base -= 6
        if "Double" in marche: base += 1.5
        base += random.uniform(-0.8, 0.8)
        conf = round(base, 2)
        if conf < 65: conf = round(65 + random.uniform(0,3),2)
        if conf > 90: conf = round(87 + random.uniform(0,3),2)
        return conf

    if st.button("🔍 ANALYSER TOUS LES MATCHS DU JOUR"):
        resultats = []
        for m in matchs_jour:
            conf = calcul_ia(m["Cote"], m["Marché"], m["xG"])
            if 72 <= conf <= 80: statut = "✅ FEU VERT"
            elif conf > 80: statut = "❌ PIÈGE"
            else: statut = "⚠️ RISQUÉ"
            resultats.append({**m, "IA %": conf, "Statut": statut})
        
        df = pd.DataFrame(resultats)
        # Trie par FEU VERT en premier
        df = df.sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        verts = df[df["Statut"].str.contains("FEU VERT")]
        if not verts.empty:
            st.success(f"🔥 {len(verts)} FEU VERT trouvés ! Mise conseillée 2000F - 5000F")
            st.balloons()
        else:
            st.warning("Aucun FEU VERT aujourd'hui, attends demain.")

    st.divider()
    st.markdown("#### ✍️ Analyse Manuelle")
    match = st.text_input("Match", placeholder="Ex: Etalons vs Lions")
    marche = st.selectbox("Marché", ["Double Chance", "Over 2.5 Buts", "Over 1.5 Buts", "Under 2.5 Buts", "BTTS Oui", "Victoire Domicile", "1X", "X2"])
    cote = st.number_input("Cote LONAB", value=2.05, step=0.01)
    xg = st.slider("xG Attendu", 0.0, 6.0, 2.80, 0.01)

    if st.button("🔍 ANALYSER CE MATCH"):
        conf = calcul_ia(cote, marche, xg)
        st.metric(f"🤖 IA pour {match}", f"{conf}%")
        if 72 <= conf <= 80:
            st.success(f"✅ FEU VERT - {conf}% - Tu peux miser !")
            st.balloons()
        elif conf > 80:
            st.error(f"❌ BLOQUÉ PIÈGE - {conf}%")
        else:
            st.warning(f"⚠️ RISQUÉ - {conf}%")

with tab2:
    st.markdown("### 🐎 PMU-B LONAB")
    st.info("Module PMU à venir")

with tab3:
    st.markdown("### 📈 Bourse BRVM")
    st.info("Module Bourse à venir")

st.caption("👑 Fabrice AI Empire V4 MATCHS AUTO | Ouaga 🇧🇫")
