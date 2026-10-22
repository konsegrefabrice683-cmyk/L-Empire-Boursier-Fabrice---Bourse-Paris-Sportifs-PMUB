import streamlit as st

st.set_page_config(page_title="Empire Fabrice", layout="wide")

st.title("L-EMPIRE BOURSIER FABRICE")
st.success("VERT - APPLICATION EN LIGNE")
st.write("Bourse Paris | Paris Sportifs | PMUB")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Bourse Paris")
    st.metric("CAC 40", "8145", "+1.2%")
    st.write("En direct")

with col2:
    st.subheader("Paris Sportifs")
    match = st.selectbox("Match", ["Salitas vs EFO", "Etalons vs Ghana", "PSG vs Real"])
    mise = st.number_input("Mise FCFA", 1000)
    if st.button("Parier"):
        st.balloons()
        st.success("Pari valide")

with col3:
    st.subheader("PMUB")
    chevaux = st.multiselect("Chevaux", ["1 Tonnerre", "2 Eclair", "3 Foudre", "4 Ouragan"])
    if st.button("Valider PMU"):
        st.success("Ticket valide")

st.write("Cree par Fabrice - Ouagadougou")
