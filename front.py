import streamlit as st
from datetime import datetime, time 


def dashboard_():

    st.title("Sistema de CRM e clientes")
    email = st.text_input("Insira seu e-mail")
    data = st.date_input("Data da copmpra", datetime.now())
    hora = st.time_input("Hora da compra")
    valor = st.number_input("Valor do produto")
    quantidade = st.number_input("Quantidade de produto")
    produto = st.selectbox("Produtos", options=["Produto 1","Produto 2","Produto 3"])

    if st.button("Cadastrar"):
        st.write("Dados coletados")
        st.write(f"Email", email)
        st.write(f"data", data)
        st.write(f"hora", hora)
        st.write(f"valor", valor)
        st.write(f"quantidade", quantidade)
        st.write(f"produto", produto)
