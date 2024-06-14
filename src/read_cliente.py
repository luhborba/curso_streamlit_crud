"""Arquivo onde ficaram os codigos de Leitura e demonstração de clientes."""

import pandas as pd
import streamlit as st


def ler_clientes():
    """Leitura dos Clientes."""
    df = pd.read_csv("data/clientes.csv")
    st.table(df)
