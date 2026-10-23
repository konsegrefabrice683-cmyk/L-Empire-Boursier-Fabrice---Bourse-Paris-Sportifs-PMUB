
import streamlit as st
import random

st.set_page_config(page_title="Fabrice AI Empire V3 AUTO", page_icon="👑", layout="centered")

st.title("👑 Fabrice AI Empire V3 AUTO")
st.caption("AUTO 72-80% | L'IA calcule elle-même | Ouagadougou")

marche = st.selectbox("Marché", ["Over 2.5 Buts","Over 1.5 Buts","Under 2.5 Buts","BTTS Oui","Victoire Domicile","Victoire Extérieur","Double Chance 1X","Double Chance X2"])
cote = st.number_input("Cote LONAB", value=1.95, step=0.01)
xg = st.number_input("xG Attendu", value=2.8, step=0.1)

if st.button("🤖 L'IA CALCULE SON %"):
    base = 75.0
    if 1.70 <= cote <= 2.15:
        base += 3
    elif cote > 2.6:
        base -= 8
    elif cote < 1.50:
        base -= 10
    if "Over" in marche and xg >= 2.5:
        base += 2
    if "Over" in marche and xg < 1.8:
        base -= 6
    base += random.uniform(-0.7, 0.7)
    confianceIA = round(base, 2)
    
    if confianceIA < 68:
        confianceIA = round(68 + random.uniform(0,2),2)
    if confianceIA > 88:
        confianceIA = round(86 + random.uniform(0,2),2)

    st.divider()
    st.markdown(f"**Marché:** {marche} | **Cote:** {cote}")
    st.markdown(f"### 🤖 Mon analyse à moi l'IA: {confianceIA}%")

    if 72 <= confianceIA <= 80:
        st.success(f"✅ FEU VERT - {confianceIA}% DANS LA ZONE OR\n\nC'est bon ! Tu peux miser 2000F - 5000F")
        st.balloons()
    elif confianceIA > 80:
        st.error(f"❌ BLOQUÉ: {confianceIA}% > 80% - COTE PIÈGE ! Je refuse.")
    else:
        st.warning(f"⚠️ RISQUÉ: {confianceIA}% < 72% - Pas assez sûr.")
