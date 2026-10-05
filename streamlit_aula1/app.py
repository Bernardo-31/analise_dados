import streamlit as st
import pandas as pd

nome = "Bernardo"
idade = 17

st.write("Olá, mundo")

st.write("Meu nome é", nome, "e eu tenho", idade, "anos.")

st.title("Meu primeiro dash")

st.subheader(nome)

df = pd.DataFrame({
    "Matéria": ["Português", "Matemática", "Python", "Frame"],
    "Nota": [45, 40, 56, 50]
})

st.write(df)

st.subheader("Itens de supermercado")

produtos = {
    "Arroz": 25.00,
    "Feijão": 8.00,
    "Macarrão": 5.00,
    "Leite": 6.00,
    "Café": 15.00
}

produto = st.selectbox("Escolha um produto:", list(produtos.keys()))

quantidade = st.number_input("Quantidade:", min_value=1, value=1)

def calcular_preco(produto, quantidade):
    return produtos[produto] * quantidade

preco = calcular_preco(produto, quantidade)

st.write("Produto:", produto)
st.write("Quantidade:", quantidade)
st.write("Preço da compra: R$", preco)