"""Arquivo de Criação do Formulário de Clientes."""

import pandas as pd
import streamlit as st


def criar_cliente():
    """Criação do formulário de Clientes."""
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

        cadastrar = st.form_submit_button("Cadastrar")

        if cadastrar:
            novo_cliente = {
                "nome": nome,
                "email": email,
                "dt_nascimento": dt_nascimento,
                "cpf": cpf,
                "endereco_rua": endereco_rua,
                "endereco_bairro": endereco_bairro,
                "endereco_cidade": endereco_cidade,
                "endereco_uf": endereco_uf,
                "endereco_complemento": endereco_complemento,
                "endereco_numero": endereco_numero,
                "sexo": sexo,
                "estado_civil": estado_civil,
                "dt_cadastro": pd.Timestamp("now"),
            }
            try:
                df = pd.read_csv("data/clientes.csv")
            except FileNotFoundError:
                df = pd.DataFrame(columns=novo_cliente.keys())
            df = pd.concat([df, pd.DataFrame([novo_cliente])], ignore_index=True)
            df.to_csv("data/clientes.csv", index=False)
            st.success("Cadastro Realizado com Sucesso!!")
            st.experimental_rerun()
