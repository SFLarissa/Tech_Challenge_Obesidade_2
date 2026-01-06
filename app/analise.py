import streamlit as st


def render():
    st.title("📈 Painel Analítico")
    st.components.v1.iframe(
    "",
    width=1200,
    height=700
)