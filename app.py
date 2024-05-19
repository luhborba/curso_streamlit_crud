"""Arquivo principal."""

import streamlit as st


def main():
    """Função principal."""
    st.set_page_config(page_title="Sistema Gerencial", layout="wide")
    st.title("Sistema Gerencial")

    with st.form("cadastrocliente"):
        col1, col2, col3 = st.columns(3)
        with col1:
            nome = st.text_input("Nome Completo")
            email = st.text_input("Email")
            endereco_rua = st.text_input("Logradouro")
            endereco_bairro = st.text_input("Bairro")
        with col2:
            dt_nascimento = st.date_input("Data de Nascimento", value=None)
            cpf = st.text_input("CPF")
            endereco_numero = st.number_input("Nº", value=0, step=1)
            endereco_cidade = st.text_input("Cidade")
        with col3:
            sexo = st.selectbox(
                "Sexo", ["Masculino", "Feminino"], placeholder="", index=None
            )
            estado_civil = st.selectbox(
                "Estado Civil",
                ["Solteiro(a)", "Casado(a)", "Viuvo(a)", "Divorciado(a)"],
                placeholder="",
                index=None,
            )
            endereco_complemento = st.text_input("Complemento")
            endereco_uf = st.text_input("UF")

        cadastrar = st.form_submit_button()


if __name__ == "__main__":
    main()
