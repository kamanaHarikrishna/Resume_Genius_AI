import streamlit as st
import cohere

cohere_key = st.secrets["COHERE_API_KEY"]
co = cohere.Client(cohere_key)

