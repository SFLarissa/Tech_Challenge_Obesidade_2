import streamlit as st

def render():
    st.image("assets/2.png", use_container_width=True)

    st.subheader("Tecnologia inteligente para apoio do diagnóstico e à prevenção da obesidade")

    st.markdown("""
    O **Peso Saudável** é uma solução baseada em Machine Learning desenvolvida 
    para auxiliar profissionais da saúde na avaliação do risco de obesidade.

    ⚠️ Este sistema não substitui o diagnóstico médico, atuando como ferramenta
    de apoio à decisão clínica.

    ### Funcionalidades:
    - Coleta de dados do paciente
    - Histórico de avaliações
    - Visualização analítica via Power BI
    """)