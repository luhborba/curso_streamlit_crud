"""Arquivo de edição do Cliente."""

import pandas as pd
import streamlit as st


def editar_clientes():
    """Função de edição de Clientes."""
    try:
        df = pd.read_csv("data/clientes.csv")

        cliente_edicao = st.selectbox(
            "Cliente",
            df["nome"].tolist(),
            index=None,
            placeholder="Escolha o Cliente que deseja Editar:",
        )
    except:
        st.error("Não existem clientes cadastrados.")
