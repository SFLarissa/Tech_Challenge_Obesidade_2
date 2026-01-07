import streamlit as st


def render():
    st.components.v1.iframe(
    "https://app.powerbi.com/view?r=eyJrIjoiZDEwMmI0YzktYzBlOC00OTRmLWIyNzQtMTgzMGI3OWI1MjU0IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9",
    width=2000,
    height=800
)