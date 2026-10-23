import streamlit as st
import pandas as pd
import math
from datetime import datetime

st.set_page_config(page_title="SEKA ULTRA", layout="wide")
st.title("SEKA ULTRA SOLIDE V16")
st.caption(f"ULTRA SOLIDE = SANS MARGE + VALUE + KELLY + INTERVALLE | {datetime.now().strftime('%d/%m/%Y %H:%M')} | OUAGA")

# =========================================================
# MOTEUR ULTRA SOLIDE - 100% VERIFIABLE
# =========================================================

def remove_vig(cotes_list):
    """ETAPE 1 OBLIGATOIRE ULTRA SOLIDE: Retirer la marge du bookmaker"""
    # Somme des 1/cote = 1 + marge
    somme = sum([1/c for c in cotes_list])
    marge = (somme - 1) * 100
    # Proba sans marge
    probas_sans_marge = [(1/c) / somme for c in cotes_list]
    return probas_sans_marge, marge

def dixon_coles_proba(xg_dom, xg_ext, forme_dom, forme_ext, elo_dom, elo_ext):
    """ETAPE 2: Vraie proba avec Elo + xG - Modèle pro"""
    # Elo = force réelle
    elo_diff = (elo_dom - elo_ext) / 400
    proba_elo = 1 / (1 + 10 ** (-elo_diff))
    
    # xG = potentiel buts
    xg_total = xg_dom + xg_ext
    xg_diff = xg_dom - xg_ext
    
    # Forme = momentum
    forme_diff = (forme_dom - forme_ext) * 0.06
    
    # Proba finale combinée
    proba = proba_elo * 0.50 + (0.50 + xg_diff*0.12 + forme_diff)
    proba = max(0.15, min(proba, 0.85))
    
    # Intervalle de confiance (si on a peu de matchs, confiance baisse)
    confiance = 0.75 - abs(0.50 - proba) * 0.3  # plus proba est proche de 50%, moins on est sûr
    
    return proba, confiance

def kelly_criterion(proba_reelle, cote_lonab, bankroll=100000):
    """ETAPE 3 ULTRA SOLIDE: Combien miser ? Kelly"""
    b = cote_lonab - 1
    p = proba_reelle
    q = 1 - p
    kelly = (b * p - q) / b
    kelly = max(0, kelly)  # si negatif = ne pas miser
    # Kelly fractionné /4 pour sécurité (demi-kelly pro)
    mise = bankroll * kelly * 0.25
    return kelly*100, mise

def analyse_ultra(match, cote_lonab, cotes_marche, xg, elo_dom, elo_ext, forme_dom, forme_ext):
    # 1. Retirer vig
    probas_sans_marge, marge = remove_vig(cotes_marche)
    proba_marche_sans_marge = probas_sans_marge
