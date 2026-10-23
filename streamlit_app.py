import streamlit as st
from datetime import datetime
import random
import pandas as pd
import urllib.parse
st.set_page_config(page_title="Fabrice Empire V10 ULTIMATE", page_icon="👑", layout="wide")
st.markdown("""<style>.stButton>button{width:100%;background:linear-gradient(90deg,#16a34a,#0ea5e9)!important;color:white!important;font-weight:800!important;padding:14px!important;border-radius:12px!important}
.ticket{background:#111827;color:#0f0;padding:14px;border-radius:10px;font-family:monospace;font-size:11px;border:1px solid #22c55e;margin:6px 0}
.green-box{background:#dcfce7;padding:12px;border-radius:10px;border:2px solid #22c55e}</style>""", unsafe_allow_html=True)
now=datetime.now().strftime("%d/%m/%Y %H:%M")
st.markdown(f"### 👑 FABRICE EMPIRE V10 ULTIMATE | 20 MATCHS + PMU PRO + BOURSE WORLD | {now}")
def statut(c):
    if 72 <= c <= 80: return "✅ FEU VERT"
    elif c > 80: return "❌ PIÈGE"
    else: return "⚠️ RISQUÉ"
def calc_paris(cote, marche, xg):
    base=75.0
    if 1.70 <= cote <= 2.15: base+=3
    elif cote>2.6: base-=8
    elif cote<1.50: base-=10
    if "Over" in marche and xg>=2.5: base+=2
    if "Double" in marche or "BTTS" in marche: base+=1.5
    base+=random.uniform(-0.8,0.8)
    c=round(base,2)
    if c<65: c=round(65+random.uniform(0,3),2)
    if c>90: c=round(86+random.uniform(0,4),2)
    return c
def calc_pmu(cotes, formes, type_pari):
    avg_cote=sum(cotes)/len(cotes) if cotes else 3.0
    avg_forme=sum(formes)/len(formes) if formes else 4.0
    base=74.0
    if type_pari=="Gagnant":
        if 1.8 <= avg_cote <= 3.5: base+=5
        if avg_forme>=4.3: base+=4
    elif type_pari=="Placé": base+=6
    elif "Couplé" in type_pari: base+=3
    elif type_pari=="Tiercé": base+=2
    elif type_pari=="Quarté": base+=1
    if avg_forme>=4.2: base+=1.5
    base+=random.uniform(-1.2,1.2)
    c=round(base,2)
    if c<65: c=round(65+random.uniform(0,3),2)
    if c>90: c=round(86+random.uniform(0,4),2)
    return c
def calc_bourse(t, v):
    base=75.0
    if t=="Hausse Forte": base+=4
    elif t=="Hausse": base+=2.5
    elif "Baisse" in t: base-=3
    base+=random.uniform(-1.5,1.5)
    return round(base,2)
def wa(t): return f"https://wa.me/?text={urllib.parse.quote(t)}"
tab1,tab2,tab3=st.tabs(["⚽ PARIS 20 MATCHS","🐎 PMU-B PRO","🌍 BOURSE WORLD"])
with tab1:
    st.markdown("### ⚽ 20 MATCHS ANALYSE AUTO")
    matchs=[
        {"Match":"Man City vs Arsenal","Marché":"Double Chance","Cote":1.85,"xG":2.9,"Heure":"19:00","L":"PL"},
        {"Match":"Liverpool vs Chelsea","Marché":"Over 2.5","Cote":1.88,"x
