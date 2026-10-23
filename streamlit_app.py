import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="SEKA", layout="wide")
st.title("SEKA - SYSTEME COMPLET")
st.caption(f"Ouagadougou | {datetime.now().strftime('%d/%m/%Y %H:%M')} | Tendance + Valeur + Bruit -> IA 72-80% FEU VERT")
st.divider()

def analyse_statut(confiance):
    if 72.0 <= confiance <= 80.0:
        return "FEU VERT"
    if confiance > 80.0:
        return "PIEGE - TROP BEAU"
    return "RISQUE - EVITER"

def analyse_paris_sportifs(cote, xg, marche, forme_dom, forme_ext):
    if xg >= 3.0 and "Over" in marche:
        tendance = "HAUSSE FORTE"; base = 77.0
    elif xg >= 2.5:
        tendance = "HAUSSE"; base = 75.5
    elif xg <= 1.8:
        tendance = "BAISSE"; base = 71.0
    else:
        tendance = "STABLE"; base = 73.5

    if 1.70 <= cote <= 2.15:
        valeur = "EXCELLENTE VALEUR"; base += 2.8
    elif 2.16 <= cote <= 2.60:
        valeur = "BONNE VALEUR"; base += 1.2
    elif cote > 3.2:
        valeur = "COTE PIEGE"; base -= 6.0
    elif cote < 1.50:
        valeur = "FAIBLE VALEUR"; base -= 4.5
    else:
        valeur = "VALEUR CORRECTE"; base += 0.5

    if forme_dom >= 4.2 and forme_ext <= 3.0:
        bruit = "MARCHE CALME"; base += 1.0
    elif forme_dom <= 3.0 and forme_ext >= 4.2:
        bruit = "MARCHE BRUYANT"; base -= 1.5
    else:
        bruit = "MARCHE NORMAL"
    
    base += random.uniform(-0.7, 0.7)
    if base < 65: base = 66.5 + random.uniform(0, 1.5)
    if base > 90: base = 87.5 + random.uniform(0, 1.5)
    return round(base, 2), tendance, valeur, bruit

def analyse_pmu_b(cote, forme, age, driver_note):
    base = 73.0
   
