import streamlit as st
import pandas as pd

dados = [
    ["ABRAÃO BARROS DA SILVA", 10, 10, 10, 10, 9, 9.333333333, 9.566666667, "Excelente"],
    ["ALEX GUTEMBERG FIGUEIREDO", 10, 10, 10, 10, 7, 6, 7.7, "Bom"],
    ["ARYANNE REIS DOS SANTOS", 10, 10, 10, 10, 8, 6.666666667, 8.133333333, "Bom"],
    ["CAMILA VITORIA LUCAS BEZERRA DA SILVA", 10, 10, 10, 10, 0, 8, 8, "Bom"],
    ["CONCEIÇÃO DE MARIA TEIXEIRA MENDES DE SOUZA", 0, 0, 0, 10, 0, 0, 1, "Insuficiente"],
    ["DIOGO DANIEL SENA COSTA", 0, 0, 0, 0, 9, 0, 0.9, "Insuficiente"],
    ["ERNANI JOÃO DE MELO", 10, 10, 10, 10, 9, 8.666666667, 9.233333333, "Ótimo"],
    ["FERNANDA GABRIELA SOBRINHO DOS ANJOS", 10, 10, 10, 10, 10, 8.666666667, 9.333333333, "Ótimo"],
    ["GABRIEL EZIDIO DA SILVA BRILHANTE", 10, 10, 10, 10, 10, 8.666666667, 9.333333333, "Ótimo"],
    ["GABRIEL WINICIUS DE OLIVEIRA LIMA", 10, 10, 10, 10, 10, 3.333333333, 6.666666667, "Ainda não suficiente"],
    ["GEORGE JOSÉ DOS SANTOS VERA CRUZ FILHO", 10, 10, 10, 10, 9, 7.333333333, 8.566666667, "Ótimo"],
    ["GUILHERME DE SANTANA NASCIMENTO", 10, 0, 10, 10, 10, 8.666666667, 8.333333333, "Bom"],
    ["ITALO ROBERT RODRIGUES DA SILVA", 0, 0, 0, 0, 4, 6.666666667, 3.733333333, "Insuficiente"],
    ["JADSON DA SILVA", 10, 0, 0, 10, 10, 8, 7, "Bom"],
    ["JAIR LUIZ DOS SANTOS", 10, 10, 10, 10, 7, 4.666666667, 7.033333333, "Bom"],
    ["JEANE MARIA BARBOSA E SILVA", 10, 10, 10, 10, 7, 6.666666667, 8.033333333, "Bom"],
    ["JEFFERSON DOS SANTOS FIGUEIRA", 10, 10, 10, 10, 9, 5.333333333, 7.566666667, "Bom"],
    ["JOSÉ CARLOS OLIVEIRA DA SILVA", 10, 10, 10, 10, 6, 7.333333333, 8.266666667, "Bom"],
    ["JOSE GLEBSON MONTEIRO", 10, 10, 10, 10, 9, 7.333333333, 8.566666667, "Ótimo"],
    ["KAUÃ SILVA DE LIMA", 10, 10, 10, 10, 9, 8, 8.9, "Ótimo"],
    ["KAYO MANOEL PEREIRA BATISTA", 10, 10, 10, 10, 0, 7.333333333, 7.666666667, "Bom"],
    ["LAIS MICAELE RAMOS BRASIL", 10, 10, 10, 10, 0, 7.333333333, 7.666666667, "Bom"],
    ["LINDOBERTO ABIDIJAN MOTA DOS SANTOS", 10, 10, 10, 10, 10, 6.666666667, 8.333333333, "Bom"],
    ["LUCAS DANIEL ROQUE DE LIMA", 0, 0, 0, 10, 10, 0, 2, "Insuficiente"],
    ["MARIA DAS GRAÇAS DE LIMA TAVARES", 10, 10, 10, 10, 9, 6, 7.9, "Bom"],
    ["MARIA GABRIELA DE MOURA", 0, 0, 0, 10, 0, 4, 3, "Insuficiente"],
    ["MAX DIOGO FERREIRA DE SOUZA", 10, 10, 10, 10, 10, 0, 5, "Ainda não suficiente"],
    ["MAYSA CRISTINA DA SILVA", 10, 0, 0, 10, 0, 0, 2, "Insuficiente"],
    ["MELQUISEDEQUE ANDRADE SILVA", 0, 0, 0, 0, 0, 0, 0, "Insuficiente"],
    ["NICOLLAS VIDAL HOLANDA", 10, 0, 0, 10, 9, 8.666666667, 7.233333333, "Bom"],
    ["PEDRO LUCAS SILVA DE SOUZA", 10, 10, 10, 10, 9, 6, 7.9, "Bom"],
    ["PEDRO MOURA CAVALCANTE", 10, 10, 0, 10, 10, 0, 4, "Insuficiente"],
    ["RENATO SILVESTRE DE LIMA", 10, 10, 10, 10, 7, 7.333333333, 8.366666667, "Bom"],
    ["ROBERTA BATISTA LIMA DA SILVA", 10, 0, 0, 10, 0, 0, 2, "Insuficiente"],
    ["VÍCTOR LUCAS NUNES DE ALMEIDA", 10, 10, 10, 10, 9, 0, 4.9, "Insuficiente"],
    ["WEDSON TRAJANO DA SILVA", 10, 10, 10, 10, 10, 5.333333333, 7.666666667, "Bom"]
]

colunas = [
    "Nome",
    "Fórum 1",
    "Fórum 3",
    "Fórum 5",
    "Atividade1",
    "Atividade2",
    "Teste",
    "NF",
    "Menção"
]

df = pd.DataFrame(dados, columns=colunas)

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
