import streamlit as st

st.title("ESSAI")
st.success("Gagné")
st.error("Perdu")
st.info("Info")

if st.button('Envoyer'):
    st.balloons()
    
st.warning('This is a warning', icon="⚠️")

st.snow()

st.markdown("Papa")

st.write("TITI")
