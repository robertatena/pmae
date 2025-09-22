import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Dashboard PMAE",
    layout="centered",
    page_icon="📊",
)

# Título
st.title("📊 Resumo Executivo - PMAE")
st.markdown("""
Este painel simula o desempenho do fundo PMAE com base nos parâmetros informados.
""")

# Sidebar com parâmetros
st.sidebar.header("🔧 Parâmetros da Simulação")
valor_total = st.sidebar.number_input("💰 Valor total das operações (R$)", value=12_000_000, step=100_000)
empresas = st.sidebar.number_input("🏢 Número de empresas atendidas", value=1680, step=10)
inadimplencia = st.sidebar.slider("❗ Inadimplência
