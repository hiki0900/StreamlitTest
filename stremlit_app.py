import streamlit as st

st.title("st.session_state")

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

st.header("input")
col1, spacer, col2 = st.columns([2,1,2])
with col1:
    pounds =st.number_input("pound: ", on_change=lbs_to_kg, key="lbs")
with col2:
    kilogram = st.number_input("kilogram: ", on_change=kg_to_lbs, key="kg")
st.header("output")
st.write("st.session_state object: ", st.session_state)
