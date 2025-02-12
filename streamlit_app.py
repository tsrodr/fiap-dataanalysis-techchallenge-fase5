import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

def previsao_performance(dados, modelo):
    return modelo.predict(dados)[0]

def criar_grafico_linhas(df, eixo_x, eixo_y, titulo, rotulo_x, rotulo_y, legenda={}):
    fig = px.line(df, x=eixo_x, y=eixo_y, title=titulo)
    fig.update_layout(xaxis_title=rotulo_x, yaxis_title=rotulo_y, legend_title="Legenda")
    if legenda:
        fig.for_each_trace(lambda t: t.update(name=legenda.get(t.name, t.name)))
    return fig

def criar_grafico_barras(df, eixo_x, eixo_y, titulo, rotulo_x, rotulo_y):
    fig = px.bar(df, x=eixo_x, y=eixo_y, title=titulo)
    fig.update_layout(xaxis_title=rotulo_x, yaxis_title=rotulo_y, legend_title="Legenda")
    return fig

def criar_grafico_dispersao(df, eixo_x, eixo_y, titulo, rotulo_x, rotulo_y, cor=None):
    fig = px.scatter(df, x=eixo_x, y=eixo_y, title=titulo, color=cor, trendline="ols")
    fig.update_layout(xaxis_title=rotulo_x, yaxis_title=rotulo_y, legend_title="Legenda")
    return fig

st.set_page_config(page_title="Painel de Desempenho Acadêmico", layout="wide")

def main():
    df_alunos = pd.read_csv('base_streamlit/aluno.csv')
    df_modelo = pd.read_csv('base_streamlit/treino_resultado.csv', sep=';')
    modelo_svm = joblib.load('melhor_modelo_support_vector_machine.pkl')
    
    opcoes_menu = [
        "Início",
        "Análise de Desempenho",
        "Predição de Risco Acadêmico",
        "Conclusão"
    ]
    
    pagina = st.sidebar.radio("Menu de Navegação", opcoes_menu)
    
    if pagina == "Início":
        mostrar_inicio()
    elif pagina == "Análise de Desempenho":
        mostrar_analise(df_alunos)
    elif pagina == "Predição de Risco Acadêmico":
        mostrar_predicao(df_modelo, modelo_svm)
    elif pagina == "Conclusão":
        mostrar_conclusao()

def mostrar_inicio():
    st.title("🏫 Análise do Desempenho Acadêmico")
    st.markdown("""
    Este projeto faz parte do **Datathon**, uma iniciativa voltada para a análise e previsão do desempenho acadêmico dos alunos da ONG **Passos Mágicos**. A ONG atua transformando a educação de crianças e jovens em situação de vulnerabilidade social, fornecendo suporte pedagógico e emocional para melhorar suas oportunidades futuras.
    
    O objetivo deste estudo é fornecer **insights estratégicos** sobre o impacto da ONG na vida dos estudantes, utilizando técnicas de **análise de dados e machine learning**. Com base em dados históricos de 2020 a 2022, este painel permite:
    
    - **Explorar padrões de desempenho** ao longo dos anos.
    - **Avaliar o impacto de diferentes indicadores educacionais**.
    - **Realizar previsões de risco acadêmico**, identificando alunos que precisam de maior suporte.
    
    Utilize o menu lateral para navegar entre as seções e obter informações detalhadas.
    """)

def mostrar_analise(df):
    st.header("📊 Análise Exploratório do Desempenho Acadêmico")
    
    tab1, tab2 = st.tabs(['Visão Geral', 'Indicadores e Gráficos'])
    
    with tab1:
        st.markdown("""
        A **análise exploratória** tem como propósito entender os padrões educacionais, permitindo visualizar como diferentes fatores impactam o aprendizado dos alunos.
        
        **Principais pontos analisados:**
        - **Relação entre indicadores acadêmicos e psicopedagógicos**.
        - **Tendências ao longo dos anos (2020 a 2022)**.
        - **Impacto das ações da ONG no desempenho dos alunos**.
        
        Os gráficos abaixo ajudam a identificar **como os indicadores evoluem ao longo do tempo e quais fatores estão mais correlacionados com o sucesso acadêmico.**
        """)

        lIndicadores = ['inde', 'iaa', 'ieg', 'ips', 'ida', 'ipp', 'ipv', 'ian']
        
        col1, col2 = st.columns(2)
        
        with col1:
            ano_selecionado = st.selectbox("Selecione o Ano:", df['ano'].unique())
            df_filtrado = df[df['ano'] == ano_selecionado]
        
        with col2:
            indicador = st.selectbox("Selecione um Indicador:", lIndicadores)
        
        st.plotly_chart(criar_grafico_dispersao(df_filtrado, 'inde', indicador, "Relação entre INDE e Indicadores", "INDE", indicador, cor='pedra'))
        
        st.markdown("""Os dados indicam que alunos com **maior engajamento** e **melhor suporte psicopedagógico** tendem a apresentar **melhores resultados acadêmicos**. Isso reforça a necessidade de políticas educacionais que promovam um ensino mais inclusivo e personalizado.""")

        with tab2:
            lano = {'Todos': 'Todos','2020': 2020, '2021': 2021, '2022':2022}
            lpedras = ['Topázio', 'Ametista', 'Ágata', 'Quartzo']
            cbano = st.selectbox('Selecione o ano:', list(lano.keys()), key = "cbano")

            df_ano = df    
            if(cbano != 'Todos'):
                df_ano = df[df['ano'] == lano[cbano]]
                if(lano[cbano] > 2020):
                    df_ano_anterior = df[df['ano'] == lano[cbano]-1]

            num_colunas_pedras = len(lpedras)
            colunas_2 = st.columns(num_colunas_pedras, border=True)
            for i, dados in enumerate(lpedras):
                coluna_atual = colunas_2[i % num_colunas_pedras]
                with coluna_atual:
                    if(cbano != 'Todos' and lano[cbano] > 2020):
                        st.metric(dados, label_visibility='visible', help='Comparativo em relação ao ano anterior', value=np.sum(df_ano['pedra'] == dados), delta= int(np.sum(df_ano['pedra'] == dados) - np.sum(df_ano_anterior['pedra'] == dados)))
                    else:
                        st.metric(dados, np.sum(df_ano['pedra'] == dados), delta=None)            

            num_colunas = len(lIndicadores)
            colunas_1 = st.columns(num_colunas, border=True)

            for i, dados in enumerate(lIndicadores):
                coluna_atual = colunas_1[i % num_colunas]
                with coluna_atual:
                    st.subheader(dados, help='Comparativo em relação ao ano anterior')
                    if(cbano != 'Todos' and lano[cbano] > 2020):
                        st.metric('Média:', df_ano[dados].mean().round(2), border=False, delta=round(df_ano[dados].mean().round(2) - df_ano_anterior[dados].mean().round(2),2))
                        st.metric('Mediana:', df_ano[dados].median().round(2), border=False, delta=round(df_ano[dados].median().round(2) - df_ano_anterior[dados].median().round(2),2))
                        st.metric('Min:', df_ano[dados].min().round(2), border=False, delta=round(df_ano[dados].min().round(2) - df_ano_anterior[dados].min().round(2),2))
                        st.metric('Max:', df_ano[dados].max().round(2), border=False, delta=round(df_ano[dados].max().round(2) - df_ano_anterior[dados].max().round(2), 2))
                    else:
                        st.metric('Média:', df_ano[dados].mean().round(2),border=False, delta=None, delta_color='off')
                        st.metric('Mediana:', df_ano[dados].median().round(2),border=False, delta=None, delta_color='off')
                        st.metric('Min:', df_ano[dados].min().round(2),border=False, delta=None, delta_color='off')
                        st.metric('Max:', df_ano[dados].max().round(2),border=False, delta=None, delta_color='off')


def mostrar_predicao(df_modelo, modelo):
    st.header("🔮 Predição de Risco Acadêmico")
    
    st.markdown("""
    O **modelo preditivo** utiliza **machine learning** para prever quais alunos apresentam **maior risco acadêmico**. Com isso, gestores podem intervir antecipadamente, fornecendo suporte direcionado.
    
    **Como funciona?**
    - O modelo analisa **indicadores educacionais e psicossociais**.
    - Ele calcula a **probabilidade de um aluno ter baixo desempenho**.
    - A recomendação final é baseada no histórico dos dados da ONG.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        iaa = st.number_input("IAA (Autoavaliação)", 0, 10, 5)
        ieg = st.number_input("IEG (Engajamento)", 0, 10, 5)
    
    with col2:
        ips = st.number_input("IPS (Psicossocial)", 0, 10, 5)
        ida = st.number_input("IDA (Aprendizagem)", 0, 10, 5)
    
    with col3:
        ipp = st.number_input("IPP (Psicopedagógico)", 0, 10, 5)
        ipv = st.number_input("IPV (Ponto de Virada)", 0, 10, 5)
    
    with col4:
        ian = st.number_input("IAN (Autoavaliação)", 0, 10, 5)
    
    if st.button("Prever Risco Acadêmico"):
        dados_entrada = pd.DataFrame([[iaa, ieg, ips, ida, ipp, ipv, ian]], columns=['iaa', 'ieg', 'ips', 'ida', 'ipp', 'ipv', 'ian'])
        resultado = previsao_performance(dados_entrada, modelo)
        
        if resultado == 0:
            st.error("⚠️ O aluno tem risco de baixa performance! Recomenda-se uma ação imediata para suporte e acompanhamento.")
        else:
            st.success("✅ O aluno apresenta alta performance! O modelo sugere continuidade no suporte educacional.")

def mostrar_conclusao():
    st.title("📌 Conclusão")
    st.markdown("""
    O impacto da ONG **Passos Mágicos** na comunidade é evidente pelos avanços nos indicadores de desempenho acadêmico e engajamento. O modelo preditivo permite uma abordagem **proativa e personalizada**, garantindo que **nenhum aluno fique para trás**.
    
    A implementação de estratégias baseadas em dados fortalece a educação e permite um planejamento mais eficiente para o futuro.
    """)

if __name__ == "__main__":
    main()
