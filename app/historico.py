import streamlit as st
import pandas as pd

def render():
    st.title("📊 Histórico de Avaliações")

    if "history" not in st.session_state or not st.session_state.history:
        st.info("Nenhuma avaliação realizada ainda.")
        return

    df = pd.DataFrame(st.session_state.history)

    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Exportar histórico (CSV)",
        data=csv,
        file_name="historico_avaliacoes.csv",
        mime="text/csv"
    )