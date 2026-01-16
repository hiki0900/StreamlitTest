import streamlit as st
import joblib

@st.cache_resource
def load_model():
  return joblib.load('model.pkl')

model = load_model()
prediction = model.prediction([[1,2,3]])
st.write(prediction)
