import streamlit as st
from datetime import datetime
import random, pandas as pd, urllib.parse

st.set_page_config(page_title="Fabrice Empire V10", page_icon=":", layout="wide")
st.markdown("<style>.stButton>button{width:100%;background:#16a34a!important;color:white!important;font-weight:800!important;padding:12px!important;border-radius:10px!important}.ticket{background:#111827;color:#00ff00;padding:10px;border-radius:8px;font-family:monospace;font-size:11px;margin:5px 0}.green-box{background:#dcfce7;padding:10px;border-radius:8px;border:2px solid #22c55e}</style>", unsafe_allow_html=True)
st.markdown(f"### FABRICE EMPIRE V10 | 20 MATCHS + PMU PRO + BOURSE | {datetime.now().strftime('%d/%m %H:%M')}")

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
   
