import streamlit as st
import joblib
from pathlib import Path

# ============================================
# Caminho do modelo (RELATIVO AO PROJETO)
# ============================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model_data" / "pipeline.joblib"

# ============================================
# Inicialização do session_state
# ============================================

def init_state():
    if "model" not in st.session_state:
        st.session_state.model = joblib.load(MODEL_PATH)

