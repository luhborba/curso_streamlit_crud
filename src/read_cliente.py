"""Arquivo onde ficaram os codigos de Leitura e demonstração de clientes."""

import pandas as pd
import streamlit as st


def ler_clientes():
    """Leitura dos Clientes."""
    try:
        df = pd.read_csv("data/clientes.csv")
        st.table(df)
    except:
        st.error("Não existem clientes cadastrados.")
