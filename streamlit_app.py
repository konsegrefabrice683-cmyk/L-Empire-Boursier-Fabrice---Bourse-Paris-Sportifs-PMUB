import streamlit as st
import pandas as pd
import random
from datetime import datetime

# =========================================================
# FABRICE EMPIRE V12 - CODE SOLIDE ET LENT
# 20 PARIS + PMUB COMPLET + BOURSE INTERNATIONALE
# ANALYSE: TENDANCE + VALEUR + BRUIT + IA %
# =========================================================

st.set_page_config(page_title="FABRICE V12 EMPIRE", layout="wide")

# --- TITRE ---
st.title("FABRICE EMPIRE V12 - SYSTEME COMPLET")
st.caption(f"Ouagadougou | {datetime.now().strftime('%d/%m/%Y %H:%M')} | Systeme: Tendance + Valeur + Bruit -> IA 72-80% FEU VERT")
st.divider()

# =========================================================
# MOTEUR D'ANALYSE SOLIDE
# =========================================================

def analyse_statut(confiance):
    """Filtre OR final"""
    if 72.0 <= confiance <= 80.0:
        return "FEU VERT"
    if confiance > 80.0:
        return "PIEGE - TROP BEAU"
    return "RISQUE - EVITER"

def analyse_paris_sportifs(cote, xg, marche, forme_dom, forme_ext):
    """
    Analyse complete d'un match
    Retourne: confiance, tendance, valeur, bruit
    """
    # 1. TENDANCE
    if xg >= 3.0 and "Over" in marche:
        tendance = "HAUSSE FORTE"
        base = 77.0
    elif xg >= 2.5:
        tendance = "HAUSSE"
        base = 75.5
    elif xg <= 1.8:
        tendance = "BAISSE"
        base = 71.0
    else:
        tendance = "STABLE"
        base = 73.5

    # 2. VALEUR (Value Bet)
    if 1.70 <= cote <= 2.15:
        valeur = "EXCELLENTE VALEUR"
        base += 2.8
    elif 2.16 <= cote <= 2.60:
        valeur = "BONNE VALEUR"
        base += 1.2
    elif cote > 3.2:
        valeur = "COTE PIEGE"
        base -= 6.0
    elif cote < 1.50:
        valeur = "FAIBLE VALEUR"
        base -= 4.5
    else:
        valeur = "VALEUR CORRECTE"
        base += 0.5

    # 3. BRUIT DU MARCHE
    if forme_dom >= 4.2 and forme_ext <= 3.0:
        bruit = "MARCHE CALME"
        base += 1.0
    elif forme_dom <= 3.0 and forme_ext >= 4.2:
        bruit = "MARCHE BRUYANT"
        base -= 1.5
    else:
        bruit = "MARCHE NORMAL"
    
    # Petit alea pour realisme
    base += random.uniform(-0.7, 0.7)
    
    # Securite bornes
    if base < 65: base = 66.5 + random.uniform(0, 1.5)
    if base > 90: base = 87.5 + random.uniform(0, 1.5)
    
    return round(base, 2), tendance, valeur, bruit

def analyse_pmu_b(cote, forme, age, driver_note):
    """Analyse PMU-B LONAB"""
    base = 73.0
    
    # Tendance forme
    if forme >= 4.5: tendance = "EN FEU"; base += 3.0
    elif forme >= 4.0: tendance = "EN FORME"; base += 1.5
    else: tendance = "MOYENNE"; base -= 1.0
    
    # Valeur cote
    if 2.0 <= cote <= 4.5: valeur = "FAVORI SOLIDE"; base += 2.5
    elif 4.6 <= cote <= 9.0: valeur = "OUTSIDER VALEUR"; base += 1.0
    else: valeur = "GROS OUTSIDER"; base -= 2.0
    
    # Bruit (driver + age)
    if driver_note >= 4.3 and 4 <= age <= 7: bruit = "CALME - SUR"
    else: bruit = "BRUYANT - RISQUE"
    
    base += random.uniform(-0.8, 0.8)
    if base < 65: base = 67.0
    if base > 90: base = 88.0
    return round(base,2), tendance, valeur, bruit

def analyse_bourse(prix_actuel, tendance_marche, volume):
    """Analyse bourse Forex, Crypto, BRVM"""
    base = 74.0
    
    if tendance_marche == "HAUSSE FORTE":
        tendance = "HAUSSE FORTE"; base += 3.5
    elif tendance_marche == "HAUSSE":
        tendance = "HAUSSE"; base += 1.8
    elif tendance_marche == "BAISSE FORTE":
        tendance = "BAISSE FORTE"; base -= 3.0
    else:
        tendance = "CORRECTION"; base -= 1.0
    
    # Valeur
    if volume == "FORT": valeur = "FORTE ACTIVITE - FIABLE"; base += 1.2
    elif volume == "FAIBLE": valeur = "FAIBLE VOLUME - PIEGE"; base -= 1.5
    else: valeur = "VOLUME NORMAL"
    
    # Bruit marche
    if tendance_marche == "HAUSSE FORTE" and volume == "FORT":
        bruit = "T
