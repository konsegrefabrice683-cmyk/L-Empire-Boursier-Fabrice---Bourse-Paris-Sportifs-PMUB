import streamlit as st
from datetime import datetime
import random, pandas as pd, urllib.parse
st.set_page_config(page_title="Fabrice V10", page_icon="👑", layout="wide")
st.markdown("<style>.stButton>button{width:100%;background:#16a34a!important;color:white!important;font-weight:800!important;padding:12px!important;border-radius:10px!important}.ticket{background:#111827;color:#0f0;padding:10px;border-radius:8px;font-family:monospace;font-size:11px;margin:5px 0}.green-box{background:#dcfce7;padding:10px;border-radius:8px;border:2px solid #22c55e}</style>", unsafe_allow_html=True)
st.markdown(f"### 👑 FABRICE EMPIRE V10 | 20 MATCHS + PMU PRO + BOURSE | {datetime.now().strftime('%d/%m %H:%M')}")
def statut(c): return "✅ FEU VERT" if 72<=c<=80 else "❌ PIÈGE" if c>80 else "⚠️ RISQUÉ"
def calc_paris(cote,marche,xg):
    b=75.0
    if 1.7<=cote<=2.15: b+=3
    elif cote>2.6: b-=8
    elif cote<1.5: b-=10
    if "Over" in marche and xg>=2.5: b+=2
    b+=random.uniform(-0.8,0.8)
    c=round(b,2)
    return round(65+random.uniform(0,3),2) if c<65 else round(86+random.uniform(0,4),2) if c>90 else c
def calc_pmu(cotes,formes,typ):
    b=74.0
    if typ=="Gagnant" and 1.8<=sum(cotes)/len(cotes)<=3.5: b+=5
    if typ=="Placé": b+=5
    if "Couplé" in typ: b+=3
    if sum(formes)/len(formes)>=4.2: b+=2
    b+=random.uniform(-1,1)
    c=round(b,2)
    return round(65+random.uniform(0,3),2) if c<65 else round(86+random.uniform(0,4),2) if c>90 else c
def calc_bourse(t,v): return round(75.0+(4 if t=="Hausse Forte" else 2.5 if t=="Hausse" else -3 if "Baisse" in t else 0)+random.uniform(-1,1),2)
def wa(t): return f"https://wa.me/?text={urllib.parse.quote(t)}"
tab1,tab2,tab3=st.tabs(["⚽ PARIS 20 MATCHS","🐎 PMU-B PRO","🌍 BOURSE WORLD"])
with tab1:
    matchs=[{"M":"Man City vs Arsenal","Ma":"Double Chance","C":1.85,"X":2.9,"H":"19:00","L":"PL"},{"M":"Liverpool vs Chelsea","Ma":"Over 2.5","C":1.88,"X":3.1,"H":"18:30","L":"PL"},{"M":"Man Utd vs Tottenham","Ma":"BTTS Oui","C":1.72,"X":2.7,"H":"16:00","L":"PL"},{"M":"Real vs Barca","Ma":"Over 2.5","C":1.95,"X":3.2,"H":"20:45","L":"Liga"},{"M":"Atletico vs Sevilla","Ma":"Double Chance","C":1.75,"X":2.4,"H":"19:00","L":"Liga"},{"M":"PSG vs Marseille","Ma":"BTTS Oui","C":1.78,"X":2.8,"H":"21:00","L":"L1"},{"M":"Lyon vs Monaco","Ma":"Over 2.5","C":1.92,"X":2.9,"H":"19:00","L":"L1"},{"M":"Bayern vs Dortmund","Ma":"Over 2.5","C":1.65,"X":3.4,"H":"18:30","L":"Bun"},{"M":"Leverkusen vs Leipzig","Ma":"Double Chance","C":1.8,"X":2.6,"H":"17:30","L":"Bun"},{"M":"Inter vs Milan","Ma":"Double Chance","C":1.7,"X":2.5,"H":"20:45","L":"SerieA"},{"M":"Juve vs Napoli","Ma":"Under 2.5","C":1.82,"X":1.9,"H":"18:00","L":"SerieA"},{"M":"Burkina vs Sénégal","Ma":"Double Chance","C":2.05,"X":2.1,"H":"18:00","L":"CAN"},{"M":"Al Ahly vs Wydad","Ma":"Under 2.5","C":1.65,"X":1.6,"H":"16:00","L":"CAF"},{"M":"ES Tunis vs Mamelodi","Ma":"Double Chance","C":1.85,"X":2.0,"H":"15:00","L":"CAF"},{"M":"Raja vs Simba","Ma":"BTTS Non","C":1.9,"X":1.8,"H":"20:00","L":"CAF"},{"M":"Etalons U23 vs Ghana","Ma":"Double Chance","C":2.15,"X":2.3,"H":"16:30","L":"U23"},{"M":"AS Douanes vs Salitas","Ma":"1X","C":1.55,"X":1.7,"H":"16:00","L":"BF"},{"M":"Rahimo vs Majestic","Ma":"Over 1.5","C":1.7,"X":2.2,"H":"15:30","L":"BF"},{"M":"Man City vs Real Madrid","Ma":"Over 2.5","C":1.6,"X":3.5,"H":"21:00","L":"UCL"},{"M":"Miami vs Galaxy","Ma":"BTTS Oui","C":1.6,"X":3.0,"H":"02:00","L":"MLS"}]
    if st.button("🔍 ANALYSER LES 20 MATCHS V10"):
        res=[]
        for m in matchs:
            c=calc_paris(m["C"],m["Ma"],m["X"])
            res.append({"Match":m["M"],"Marché":m["Ma"],"Cote":m["C"],"xG":m["X"],"Heure":m["H"],"League":m["L"],"IA %":c,"Statut":statut(c)})
        df=pd.DataFrame(res).sort_values(by="IA %", ascending=False)
        st.dataframe(df, use_container_width=True, hide_index=True)
        verts=df[df["Statut"].str.contains("FEU VERT")]
        if not verts.empty:
            st.markdown(f'<div class="green-box">🔥 {len(verts)} FEU VERT SUR 20 !</div>', unsafe_allow_html=True)
            for _,r in verts.iterrows():
                code=f"LONAB-{random
