
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Supermercado Econômico",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Supermercado Econômico")
st.subheader("Itens de supermercado")

# Lista de produtos e preços
produtos = {
    "Arroz": 25.00,
    "Feijão": 8.00,
    "Macarrão": 5.00,
    "Leite": 6.00,
    "Café": 15.00
}

# Seleção do produto
produto = st.selectbox(
    "Escolha um produto:",
    list(produtos.keys())
)

# Quantidade de produtos
quantidade = st.number_input(
    "Quantidade:",
    min_value=1,
    value=1,
    step=1
)

# Função para calcular o preço
def calcular_preco(produto, quantidade):
    return produtos[produto] * quantidade

# Calcula o preço total
preco = calcular_preco(produto, quantidade)

st.write("Produto:", produto)
st.write("Preço unitário: R$", f"{produtos[produto]:.2f}")
st.write("Quantidade:", quantidade)
st.write("Preço da compra: R$", f"{preco:.2f}")

st.divider()

# Calculadora de pagamento e troco
st.subheader("💵 Pagamento e troco")

col1, col2 = st.columns(2)

with col1:
    valor_pago = st.number_input(
        "Valor pago (R$):",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

with col2:
    st.metric(
        "Total da compra",
        f"R$ {preco:.2f}"
    )

# Botão para calcular o troco
if st.button("Calcular troco", type="primary"):

    if valor_pago < preco:
        st.error("Pagamento insuficiente! O valor pago é menor que o total da compra.")

    else:
        troco = valor_pago - preco
        st.success(f"Troco: R$ {troco:.2f}")

        if troco == 0:
            st.info("Pagamento exato! Não há troco.")


if valor_pago < preco:
    st.error("Pagamento insuficiente!")
else:
    troco = valor_pago - preco
    st.success(f"Troco: R$ {troco:.2f}")