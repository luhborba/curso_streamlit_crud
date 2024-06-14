"""Arquivo principal."""

import streamlit as st

from src.create_cliente import criar_cliente
from src.read_cliente import ler_clientes


def main():
    """Função principal."""
    st.set_page_config(page_title="Sistema Gerencial", layout="wide")
    st.title("Sistema Gerencial")

    st.title("Página de Clientes")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Home", "Cadastrar", "Listar", "Editar", "Excluir", "Relatórios"]
    )
    with tab1:
        st.header("Home")

    with tab2:
        st.header("Cadastrar")
        criar_cliente()

    with tab3:
        st.header("Listar")
        ler_clientes()

    with tab4:
        st.header("Editar")

    with tab5:
        st.header("Excluir")

    with tab6:
        st.header("Relatórios")


if __name__ == "__main__":
    main()
