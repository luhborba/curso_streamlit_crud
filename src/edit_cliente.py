"""Arquivo de edição do Cliente."""

import time

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

        if cliente_edicao:
            cliente_index = df[df["nome"] == cliente_edicao].index[0]

            with st.form("editar_cliente"):
                col1, col2, col3 = st.columns(3)

                with col1:
                    nome = st.text_input(
                        "Nome Completo", value=df.loc[cliente_index, "nome"]
                    )
                    email = st.text_input("Email", value=df.loc[cliente_index, "email"])
                    endereco_rua = st.text_input(
                        "Logradouro", value=df.loc[cliente_index, "endereco_rua"]
                    )
                    endereco_bairro = st.text_input(
                        "Bairro", value=df.loc[cliente_index, "endereco_bairro"]
                    )
                with col2:
                    dt_nascimento = st.date_input(
                        "Data de Nascimento",
                        value=pd.to_datetime(
                            df.loc[cliente_index, "dt_nascimento"]
                        ).date(),
                    )
                    cpf = st.text_input("CPF", value=df.loc[cliente_index, "cpf"])
                    endereco_numero = st.number_input(
                        "Nº",
                        value=int(df.loc[cliente_index, "endereco_numero"]),
                        step=1,
                    )
                    endereco_cidade = st.text_input(
                        "Cidade", value=df.loc[cliente_index, "endereco_cidade"]
                    )
                with col3:
                    sexo = st.selectbox(
                        "Sexo",
                        ["Masculino", "Feminino"],
                        index=["Masculino", "Feminino"].index(
                            df.loc[cliente_index, "sexo"]
                        ),
                    )
                    estado_civil = st.selectbox(
                        "Estado Civil",
                        ["Solteiro(a)", "Casado(a)", "Viuvo(a)", "Divorciado(a)"],
                        index=[
                            "Solteiro(a)",
                            "Casado(a)",
                            "Viuvo(a)",
                            "Divorciado(a)",
                        ].index(df.loc[cliente_index, "estado_civil"]),
                    )
                    endereco_complemento = st.text_input(
                        "Complemento",
                        value=df.loc[cliente_index, "endereco_complemento"],
                    )
                    endereco_uf = st.text_input(
                        "UF", value=df.loc[cliente_index, "endereco_uf"]
                    )

                editar = st.form_submit_button("Editar")

                if editar:
                    df.at[cliente_index, "nome"] = nome
                    df.at[cliente_index, "email"] = email
                    df.at[cliente_index, "dt_nascimento"] = dt_nascimento
                    df.at[cliente_index, "cpf"] = cpf
                    df.at[cliente_index, "endereco_rua"] = endereco_rua
                    df.at[cliente_index, "endereco_bairro"] = endereco_bairro
                    df.at[cliente_index, "endereco_cidade"] = endereco_cidade
                    df.at[cliente_index, "sexo"] = sexo
                    df.at[cliente_index, "estado_civil"] = estado_civil
                    df.at[cliente_index, "endereco_numero"] = endereco_numero
                    df.at[cliente_index, "endereco_complemento"] = endereco_complemento
                    df.at[cliente_index, "endereco_uf"] = endereco_uf

                    df.to_csv("data/clientes.csv", index=False)
                    time.sleep(10)
                    st.success("Cliente editado com sucesso.")
                    st.rerun()
    except:
        st.error("Não existem clientes cadastrados.")
