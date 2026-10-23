import streamlit as st
import pandas as pd
import math
from datetime import datetime

# =========================================================
# SEKA PRO V15 - MOTEUR PROFESSIONNEL SANS HASARD
# PAR: FABRICE - OUAGADOUGOU
# LOGIQUE: PROBA REELLE + COTE JUSTE + VALUE + BRUIT
# =========================================================

st.set_page_config(page_title="SEKA PRO", layout="wide")
st.markdown("<h1 style='text-align:center;color:#FFD700;'>SEKA PRO V15</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center;'>MOTEUR PRO | PROBA + VALUE + TENDANCE + BRUIT | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA</p>", unsafe_allow_html=True)

# =========================================================
# MOTEUR PRO - 0% RANDOM - 100% CALCUL
# =========================================================

def proba_poisson(xg, marche):
    """Calcule la proba réelle avec xG - Loi de Poisson simplifiée"""
    # Proba de base selon xG
    if "Over" in marche:
        # Plus xG est haut, plus Over a de chance
        proba = 1 - math.exp(-xg * 0.85)
    elif "Under" in marche:
        proba = math.exp(-xg * 0.7)
    elif "BTTS" in marche:
        # BTTS Oui = les 2 équipes marquent
        proba = 0.45 + (xg - 2.0) * 0.12
    elif "Double" in marche or "1X" in marche:
        proba = 0.68 + (xg - 2.0) * 0.05
    else:
        proba = 0.60
    
    # Borne 0.35 à 0.85 max pour rester réaliste
    proba = max(0.35, min(proba, 0.85))
    return proba

def facteur_forme(forme_dom, forme_ext):
    """Ajuste la proba avec la forme"""
    diff = forme_dom - forme_ext
    facteur = 1.0 + (diff * 0.08)  # chaque point de forme = 8% d'impact
    return max(0.85, min(facteur, 1.25))

def analyse_value(cote_lonab, proba_reelle):
    """Calcule la VALUE BET - coeur du trading pro"""
    cote_juste = 1 / proba_reelle
    value_percent = (cote_lonab * proba_reelle - 1) * 100
    esperance_gain = (cote_lonab * proba_reelle) - 1
    
    if value_percent >= 15:
        valeur_label = f"VALUE EXCEPTIONNELLE +{value_percent:.1f}%"
    elif value_percent >= 5:
        valeur_label = f"BONNE VALUE +{value_percent:.1f}%"
    elif value_percent >= 0:
        valeur_label = f"VALUE FAIBLE +{value_percent:.1f}%"
    else:
        valeur_label = f"PAS DE VALUE {value_percent:.1f}%"
    
    return cote_juste, value_percent, esperance_gain, valeur_label

def analyse_bruit(cote_lonab, cote_juste, value_percent):
    """Détecte si le marché est piégé"""
    ecart_cote = abs(cote_lonab - cote_juste) / cote_juste
    
    if cote_lonab < 1.50:
        return "MARCHE SURJOUE - COTE ECRASEE - BRUIT FORT"
    elif cote_lonab > 3.50 and value_percent < 0:
        return "PIEGE BOOKMAKER - COTE TROP BELLE"
    elif ecart_cote > 0.40 and value_percent < 0:
        return "BRUIT FORT - EVITER"
    elif value_percent >= 5:
        return "MARCHE CALME - VALUE CONFIRMEE"
    else:
        return "MARCHE NORMAL"

def statut_pro(proba_reelle, value_percent):
    """Statut final 72-80% = FEU VERT"""
    ia_percent = proba_reelle * 100
    
    # On booste l'IA si la value est bonne
    if value_percent >= 10:
        ia_percent += 4
    elif value_percent >= 5:
        ia_percent += 2
    elif value_percent < 0:
        ia_percent -= 8
    
    ia_percent = max(55, min(ia_percent, 92))
    
    if 72.0 <= ia_percent <= 80.0 and value_percent >= 3:
        statut = "FEU VERT"
    elif ia_percent > 80.0:
        statut = "PIEGE - TROP BEAU"
    elif value_percent < 0:
        statut = "RISQUE - PAS DE VALUE"
    else:
        statut = "RISQUE"
    
    return round(ia_percent, 2), statut

# PMU PRO
def analyse_pmu_pro(vitesse_forme, age, cote):
    vitesse = vitesse_forme * (1.1 if 4 <= age <= 6 else 0.9)
    proba = vitesse / 30  # normalisation simple
    proba = max(0.08, min(proba, 0.65))
    cote_juste = 1 / proba
    value = (cote * proba - 1) * 100
    ia = proba * 100 + (5 if value >= 5 else -5 if value < 0 else 0)
    ia = max(60, min(ia, 90))
    return proba, cote_juste, value, round(ia,2)

# BOURSE PRO
def analyse_bourse_pro(prix_actuel, prix_ref, volume, tendance_marche):
    # Tendance = prix actuel vs ref (moyenne 20j)
    variation = (prix_actuel - prix_ref) / prix_ref * 100
    
    if variation > 5:
        tendance = "HAUSSE FORTE"
        proba_hausse = 0.78
    elif variation > 1:
        tendance = "HAUSSE"
        proba_hausse = 0.65
    elif variation < -5:
        tendance = "BAISSE FORTE"
        proba_hausse = 0.25
    else:
        tendance = "STABLE"
        proba_hausse = 0.50
    
    # Volume = confirmation
    if volume == "FORT" and "HAUSSE" in tendance:
        bruit = "TENDANCE CONFIRMEE - VOLUME FORT"
        proba_hausse += 0.07
    elif volume == "FAIBLE" and "HAUSSE" in tendance:
        bruit = "FAUX SIGNAL - VOLUME FAIBLE - BRUIT"
        proba_hausse -= 0.15
    else:
        bruit = "MARCHE LISIBLE"
    
    ia = proba_hausse * 100
    if volume == "FORT": ia += 3
    ia = max(55, min(ia, 90))
    
    benefice = variation + (3 if volume=="FORT" else 0)
    
    return tendance, bruit, round(ia,2), round(benefice,2), round(variation,2)

# =========================================================
# INTERFACE 3 ONGLETS - COMME EMPIRE V2
# =========================================================

tab1, tab2, tab3 = st.tabs(["PARIS PRO 72-80%", "PMU-B LONAB PRO", "BOURSE PRO"])

with tab1:
    st.subheader("SEKA PRO - PARIS SPORTIFS - CALCUL REEL")
    st.info("FORMULE PRO: Proba reelle (Poisson xG) + Cote Juste (1/Pro
