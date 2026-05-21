import streamlit as st
import pandas as pd

# Link CSV da planilha
url = "https://docs.google.com/spreadsheets/d/1Xye3Pxd9J_qtwiAPEV5Xm5ZzCIloS4Wu/export?format=csv&gid=1922911174"

# Ler planilha
df = pd.read_csv(url)

# Transformar coluna Nome em maiúsculo
df["Nome"] = df["Nome"].astype(str).str.upper().str.strip()

st.title("Consulta de Notas")

# Campo de busca
nome = st.text_input("Digite seu nome completo")

if nome:

    # Converter entrada do usuário para maiúsculo
    nome = nome.upper().strip()

    # Buscar aluno
    resultado = df[df["Nome"] == nome]

    if not resultado.empty:

        st.success("Aluno encontrado!")

        # Mostrar linha inteira
        st.dataframe(
            resultado,
            use_container_width=True
        )

    else:
        st.error("Nome não encontrado.")