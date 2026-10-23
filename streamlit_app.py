import streamlit as st
from datetime import datetime
import random
import pandas as pd
import urllib.parse

st.set_page_config(page_title="Fabrice AI Empire V6 FINAL", page_icon="👑", layout="centered")
st.markdown("""<style>.stButton>button {width:100%;background:#ef4444 !important;color:white !important;font-weight:800 !important;padding:12px !important;border-radius:12px !important}
.green-box {background:#dcfce7;padding:15px;border-radius:12px;border:2px solid #22c55e}
.ticket {background:#111827;color:#fff;padding:20px;border-radius:12px;font-family:monospace}
</style>""", unsafe_allow_html=True)

now = datetime.now().strftime("%d/%m/%Y %H:%M")
st.caption(f"👑 EMPIRE V6 FINAL | 72-80% STRICT | {now} | Ouaga 🇧🇫")

def calcul_ia(cote, marche, xg):
    base = 75.0
    if 1.70 <= cote <= 2.15: base += 3
    elif 2.15 < cote <= 2.5: base += 0.5
    elif cote > 2.6: base -= 8
    elif cote < 1.50: base -= 10
    if "Over" in marche and xg >= 2.5: base += 2
    if "Over" in marche and xg < 1.8: base -= 6
    if "Double" in marche or "1X" in marche or "X2" in marche: base += 1.5
    if "BTTS" in marche and xg >= 2.8: base += 2
    base += random.uniform(-0.8, 0.8)
    conf = round(base, 2)
    if conf < 65: conf = round(65 + random.uniform(0,3),2)
    if conf > 90: conf = round(87 + random.uniform(0,3),2)
    return conf

def statut(conf):
    if 72 <= conf <= 80: return "✅ FEU VERT"
    elif conf > 80: return "❌ PIÈGE"
    else: return "⚠️ RISQUÉ"

def whatsapp_link(text):
    enc = urllib.parse.quote(text)
    return f"https://wa.me/?text={enc}"

tab1, tab2, tab3 = st.tabs(["⚽ PARIS 72-80%", "🐎 PMU-B LONAB", "📈 BOURSE"])

with tab1:
    st.markdown("### ⚽ PARIS - V6 FINAL")
    matchs_jour = [
        {"Match": "Man City vs Arsenal", "Marché": "Double Chance", "Cote": 1.85, "xG": 2.9, "Heure": "19:00"},
        {"Match": "Real Madrid vs Barca", "Marché": "Over 2.5 Buts", "Cote": 1.95, "xG": 3.2, "Heure": "20:45"},
        {"Match": "Burkina Faso vs Sénégal", "Marché": "Double Chance", "Cote": 2.05, "xG": 2.1, "Heure": "18:00"},
        {"Match": "PSG vs Marseille", "Marché": "BTTS Oui", "Cote": 1.78, "xG": 2.8, "Heure": "21:00"},
        {"Match": "Al Ahly vs Wydad", "Marché": "Under 2.5 Buts", "Cote": 1.65, "xG": 1.6, "Heure": "16:00"},
    ]
    
    if st.button("🔍 ANALYSER TOUS LES MATCHS DU JOUR - V6"):
        res = []
        for m in matchs_jour:
            c = calcul_ia(m["Cote"], m["Marché"], m["xG"])
            res.append({**m, "IA %": c, "Statut": statut(c)})
        df = pd.DataFrame(res).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        verts = df[df["Statut"].str.contains("FEU VERT")]
        if not verts.empty:
            st.markdown(f'<div class="green-box">🔥 <b>{len(verts)} FEU VERT DÉTECTÉS !</b><br>Mise conseillée: 2000F - 5000F par ticket<br>Zone OR 72-80% validée</div>', unsafe_allow_html=True)
            st.balloons()
            
            # GENERATEUR TICKET LONAB
            st.divider()
            st.markdown("### 🎫 Générateur Ticket LONAB")
            for i, row in verts.iterrows():
                ticket_code = f"LONAB-{random.randint(10000,99999)}-{row['Heure'].replace(':','')}"
                st.markdown(f"""
                <div class="ticket">
                🎫 TICKET LONAB V6<br>
                -------------------<br>
                Match: {row['Match']}<br>
                Marché: {row['Marché']}<br>
                Cote: {row['Cote']} | IA: {row['IA %']}%<br>
                Heure: {row['Heure']}<br>
                Code: {ticket_code}<br>
                Mise: 3000F<br>
                Gain potentiel: {int(3000*row['Cote'])}F<br>
                -------------------<br>
                ✅ FEU VERT 72-80%<br>
                </div>
                """, unsafe_allow_html=True)
                
                msg = f"👑 FABRICE EMPIRE V6 - FEU VERT!\nMatch:{row['Match']}\nMarché:{row['Marché']}\nCote:{row['Cote']} IA:{row['IA %']}%\nCode:{ticket_code}\nMise 3000F Gain {int(3000*row['Cote'])}F"
                st.link_button(f"📲 Partager sur WhatsApp - {row['Match'][:15]}", whatsapp_link(msg))
                st.write("")

    st.divider()
    st.markdown("#### ✍️ Analyse Rapide")
    c1, c2 = st.columns(2)
    with c1:
        match = st.text_input("Match", placeholder="Etalons vs Lions", key="m1")
        marche = st.selectbox("Marché", ["Double Chance", "Over 2.5 Buts", "Over 1.5 Buts", "BTTS Oui", "1X", "X2"], key="mar1")
    with c2:
        cote = st.number_input("Cote LONAB", value=2.05, step=0.01, key="c1")
        xg = st.slider("xG", 0.0, 6.0, 2.80, 0.1, key="xg1")
    
    if st.button("🔍 ANALYSER CE MATCH - V6", key="b1"):
        c = calcul_ia(cote, marche, xg)
        st.metric(f"IA {match}", f"{c}% {statut(c)}")
        if 72 <= c <= 80:
            st.success(f"✅ FEU VERT {c}% - Mise 2000F-5000F")
            ticket = f"LONAB-{random.randint(10000,99999)}"
            st.code(f"TICKET: {match} | {marche} | Cote {cote} | IA {c}% | Code {ticket} | Gain {int(3000*cote)}F", language="text")
            msg = f"FEU VERT V6: {match} {marche} Cote {cote} IA {c}% Code {ticket}"
            st.link_button("📲 WhatsApp", whatsapp_link(msg))
            st.balloons()
        elif c > 80: st.error(f"❌ PIÈGE {c}% >80%")
        else: st.warning(f"⚠️ RISQUÉ {c}%")

with tab2:
    st.markdown("### 🐎 PMU-B LONAB V6")
    courses = [
        {"Course": "R1C4 Ouaga", "Cheval": "N°7 Bangr Nooma", "Cote": 3.2, "Forme": 4.5},
        {"Course": "R2C1 Sprint", "Cheval": "N°3 Wend Panga", "Cote": 2.8, "Forme": 4.0},
        {"Course": "R1C2 Bobo", "Cheval": "N°1 Mogho Power", "Cote": 1.9, "Forme": 4.8},
    ]
    if st.button("🐎 ANALYSER PMU V6", key="pmu6"):
        res=[]
        for cr in courses:
            base=74.0
            if 2.0 <= cr["Cote"] <= 3.5: base+=4
            if cr["Forme"]>=4.2: base+=3
            if cr["Cote"]>6: base-=7
            c=round(base+random.uniform(-1,1),2)
            res.append({**cr, "IA %": c, "Statut": statut(c)})
        df=pd.DataFrame(res).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        verts=df[df["Statut"].str.contains("FEU VERT")]
        if not verts.empty:
            st.success(f"🐎 {len(verts)} CHEVAUX FEU VERT")
            for _,r in verts.iterrows():
                msg=f"PMU FEU VERT V6: {r['Course']} {r['Cheval']} Cote {r['Cote']} IA {r['IA %']}%"
                st.link_button(f"📲 WhatsApp {r['Cheval']}", whatsapp_link(msg))
            st.balloons()

    cheval = st.text_input("Cheval", placeholder="R1C4 N°7", key="ch1")
    cote_pmu = st.number_input("Cote PMU", value=3.2, step=0.1, key="cp1")
    forme = st.slider("Forme /5", 0.0, 5.0, 4.2, 0.1, key="f1")
    if st.button("🐎 ANALYSER CHEVAL V6", key="bp1"):
        base=74.0
        if 2.0 <= cote_pmu <= 3.5: base+=4
        if forme>=4.2: base+=3
        c=round(base+random.uniform(-1,1),2)
        st.metric(f"IA {cheval}", f"{c}% {statut(c)}")
        if 72 <= c <= 80: st.success("✅ FEU VERT PMU"); st.balloons()
        else: st.warning(f"{statut(c)}")

with tab3:
    st.markdown("### 📈 BOURSE BRVM V6")
    actions = [
        {"Action": "SONATEL SNTS", "Prix": 18500, "Tendance": "Hausse", "Vol": "Fort"},
        {"Action": "ONATEL BF", "Prix": 3420, "Tendance": "Hausse", "Vol": "Moyen"},
        {"Action": "SGBCI", "Prix": 11200, "Tendance": "Stable", "Vol": "Faible"},
    ]
    if st.button("📈 ANALYSER BOURSE V6", key="bourse6"):
        res=[]
        for a in actions:
            base=75.0
            if a["Tendance"]=="Hausse": base+=2.5
            if a["Tendance"]=="Baisse": base-=4
            if a["Vol"]=="Fort": base+=1
            c=round(base+random.uniform(-1.5,1.5),2)
            res.append({**a, "IA %": c, "Signal": statut(c)})
        df=pd.DataFrame(res).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        verts=df[df["Signal"].str.contains("FEU VERT")]
        if not verts.empty:
            st.success(f"📈 {len(verts)} SIGNAUX ACHAT BRVM")
            st.balloons()

st.divider()
st.markdown("### ✅ V6 FINALE - TON EMPIRE EST FINI !")
st.caption("👑 Fabrice AI Empire V6 FINAL | 3 onglets + Ticket LONAB + WhatsApp | Ouaga 🇧🇫 | 72-80% STRICT")
