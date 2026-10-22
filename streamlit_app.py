 streamlit  st

st.set_page_config(
    page_title="Empire Fabrice",
    layout="wide"
)

st.title("L-EMPIRE BOURSIER FABRICE")
st.success("VERT - APPLICATION EN LIGNE")
st.write("Bourse Paris | Paris Sportifs | PMU'B - Burkina")

col1, col2, col3 = st.columns(3)

col1:
    st.subheader("Bourse Paris")
    st.metric("CAC 40", "8145", "+1.2%")
    st.write("En direct")

 col2:
    st.subheader("Paris Sportifs")
    match = st.selectbox("Match", ["Salitas vs EFO", "Etalons vs Ghana", "PSG vs Real"])
    mise = st.number_input("Mise FCFA", 1000)
     st.button("Parier"):
        st.balloons()
        st.success("Pari valide")

 col3:
    st.subheader("PMU'B")
    chevaux = st.multiselect("Chevaux", ["1 Tonnerre", "2 Eclair", "3 Foudre", "4 Ouragan"])
     st.button("Valider PMU"):
        st.success("Ticket valide")

st.write("Cree par Fabrice - Ouagadougou")
