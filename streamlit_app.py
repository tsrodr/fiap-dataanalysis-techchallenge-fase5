import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

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
    ## ONG (Passos Mágicos)
    
    A **Associação Passos Mágicos** tem mais de **32 anos de atuação**, dedicando-se a transformar a vida de crianças e jovens de baixa renda, proporcionando-lhes **melhores oportunidades educacionais e sociais**. Fundada por **Michelle Flues e Dimetri Ivanoff**, a iniciativa começou em **1992**, atuando dentro de orfanatos no município de **Embu-Guaçu**. 
    
    Em **2016**, após anos de experiência e aprendizado, a Passos Mágicos expandiu sua atuação, passando a atender um número ainda maior de estudantes, combinando **educação de qualidade, suporte psicológico e psicopedagógico**, ampliação da visão de mundo e desenvolvimento do protagonismo dos alunos. 
    
    Para mais informações, visite o site: [Passos Mágicos](https://passosmagicos.org.br/)           

    ## Objetivo do Projeto
    
    Este projeto faz parte do **Datathon**, uma iniciativa voltada para a análise e previsão do desempenho acadêmico dos alunos atendidos pela ONG **Passos Mágicos**. O foco do estudo é gerar **insights estratégicos** sobre o impacto da instituição na vida dos estudantes, utilizando técnicas de **análise de dados e machine learning**. Com base em dados históricos de **2020 a 2022**, este painel permite:
    
    - **Explorar padrões de desempenho** ao longo dos anos.
    - **Avaliar o impacto de diferentes indicadores educacionais**.
    - **Realizar previsões de risco acadêmico**, identificando alunos que precisam de maior suporte.
    
    Utilize o **menu lateral** para navegar entre as seções e explorar os dados em maior profundidade.
    """)

def mostrar_analise(df):
    st.header("📊 Análise Exploratório do Desempenho Acadêmico")
    
    tab1, tab2, tab3 = st.tabs(['Gráficos','Visão Geral', 'Indicadores e Comparações'])

    with tab1:
        st.markdown("""
        ## Evolução dos Indicadores Educacionais
        
        A análise dos indicadores educacionais ao longo dos anos permite compreender a evolução dos alunos atendidos pela Passos Mágicos. O gráfico abaixo mostra a tendência dos principais indicadores de 2020 a 2022.
        
        ### Contexto Histórico
        - **2020**: Primeiro ano de análise, antes da pandemia, refletindo um cenário de ensino tradicional.
        - **2021**: Impacto da pandemia e transição para o ensino remoto, resultando em quedas nos indicadores de engajamento e aprendizado.
        - **2022**: Recuperação gradual com a retomada das aulas presenciais e reforço das estratégias pedagógicas.
        
        O gráfico a seguir destaca essas variações:
        """)
        
        fig, axes = plt.subplots(2, 3, figsize=(18, 10))  # Ajustado para remover o último gráfico em branco
        fig.suptitle("Evolução dos Indicadores Educacionais por Ano", fontsize=16)
        
        indicadores = ['inde', 'ida', 'ieg', 'ips', 'ipp', 'iaa']  # Removido 'ipv' para evitar gráfico extra
        titulos = [
            'INDE (Desenvolvimento Educacional)', 'IDA (Indicador de Aprendizagem)',
            'IEG (Engajamento)', 'IPS (Psicossocial)', 'IPP (Psicopedagógico)',
            'IAA (Autoavaliação)'
        ]
        cores = ['blue', 'green', 'orange', 'purple', 'red', 'cyan']
        
        for i, ax in enumerate(axes.flatten()):
            df_grouped = df.groupby('ano', as_index=False)[indicadores[i]].mean()
            ax.plot(df_grouped['ano'], df_grouped[indicadores[i]], marker='o', color=cores[i])
            ax.set_title(titulos[i])
            ax.set_xlabel('Ano')
            ax.set_ylabel('Média')
            ax.grid(True)
            ax.set_xticks(df_grouped['ano'])  # Corrigindo eixo X quebrado
        
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        st.pyplot(fig)
        
        st.markdown("""
        Os resultados demonstram que o impacto da pandemia em **2021** foi significativo, especialmente nos indicadores de engajamento (**IEG**) e desempenho acadêmico (**IDA**). Em **2022**, observa-se uma retomada na maioria dos indicadores, indicando que a adaptação ao ensino híbrido e o suporte pedagógico oferecido foram essenciais para a recuperação dos alunos.
        """)
    
    with tab2:
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

    with tab3:
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
        ian = st.number_input("IAN (Adequação de Nível)", 0, 10, 5)
    
    if st.button("Prever Risco Acadêmico"):
        dados_entrada = pd.DataFrame([[iaa, ieg, ips, ida, ipp, ipv, ian]], columns=['iaa', 'ieg', 'ips', 'ida', 'ipp', 'ipv', 'ian'])
        resultado = previsao_performance(dados_entrada, modelo)
        
        if resultado == 0:
            st.error("⚠️ O aluno tem risco de baixa performance! Recomenda-se uma ação imediata para suporte e acompanhamento.")
        else:
            st.success("✅ O aluno apresenta alta performance! O modelo sugere continuidade no suporte educacional.")

def mostrar_conclusao():
    st.title("📌 Conclusão Final do Projeto")
    st.markdown("""
        O projeto de análise e previsão do desempenho acadêmico dos alunos da **Passos Mágicos** proporcionou uma visão detalhada sobre os fatores que influenciam a evolução educacional dos estudantes. Através da **análise exploratória de dados (EDA)**, da **modelagem preditiva** e da **criação de dashboards interativos**, foi possível mapear tendências, identificar desafios e propor soluções baseadas em dados.

        ---

        ## 🔍 Principais Descobertas  

        ### 1️⃣ **Impacto do Engajamento no Desempenho**  
        - O **Indicador de Engajamento (IEG)** apresentou forte correlação com o **Índice de Desenvolvimento Educacional (INDE)** e o **Ponto de Virada (IPV)**.  
        - Isso demonstra que **alunos mais engajados tendem a apresentar melhor desempenho**, destacando a importância de **mentorias, atividades extracurriculares e acompanhamento personalizado**.

        ### 2️⃣ **Influência do Ensino Remoto na Queda dos Indicadores**  
        - Os dados de **2021** mostraram uma **queda significativa** no aprendizado devido à transição para o ensino remoto.  
        - Em **2022**, observamos uma **recuperação gradual**, reforçando a importância do **retorno presencial e do suporte psicopedagógico** oferecido pela ONG.

        ### 3️⃣ **Ponto de Virada como Indicador Crítico**  
        - O **IPV (Ponto de Virada)** demonstrou ser um fator essencial na **trajetória educacional** dos alunos.  
        - Monitorar e atuar de forma proativa nesses momentos pode evitar quedas no aprendizado e garantir melhores resultados.

        ### 4️⃣ **Desafios do Bem-Estar Psicossocial**  
        - O **IPS (Indicador Psicossocial)** teve correlação baixa com os outros indicadores, sugerindo que fatores emocionais e sociais podem não impactar diretamente as notas.  
        - No entanto, um acompanhamento contínuo pode evitar problemas a longo prazo.

        ### 5️⃣ **Modelagem Preditiva como Suporte para Tomada de Decisão**  
        - O modelo de **Machine Learning**, utilizando **Random Forest, XGBoost e SVM**, permitiu identificar alunos em risco de queda no desempenho.  
        - Esse modelo pode ser usado para antecipar dificuldades e agir preventivamente.

        ---

        ## 🚀 Recomendações e Próximos Passos  

        ✅ **1. Fortalecer as Estratégias de Engajamento**  
        - Criar **programas de mentoria** e incentivar a participação ativa dos alunos.  
        - Expandir atividades extracurriculares que aumentem a conexão do aluno com o aprendizado.  

        ✅ **2. Monitoramento Ativo dos Alunos com Maior Risco**  
        - Implementar um **sistema de alerta** baseado nos modelos preditivos para identificar alunos com maior risco de queda de desempenho.  
        - Aplicar intervenções personalizadas e acompanhamento pedagógico para cada caso.  

        ✅ **3. Melhorar a Infraestrutura Digital e Métodos de Ensino Híbrido**  
        - Garantir que os alunos tenham acesso a **tecnologia e suporte adequado** para manter a qualidade do aprendizado, mesmo em situações de ensino remoto ou híbrido.  
        - Capacitar professores para atuar com metodologias ativas e inovadoras.  

        ✅ **4. Fortalecer o Suporte Psicopedagógico**  
        - Criar iniciativas para identificar alunos com dificuldades emocionais e oferecer **acompanhamento psicológico**.  
        - Estabelecer parcerias para ampliar o suporte psicossocial dentro e fora da ONG.  

        ✅ **5. Aprimorar a Modelagem Preditiva**  
        - Testar novos modelos e aprimorar as previsões utilizando mais dados históricos.  
        - Explorar algoritmos mais avançados, como **redes neurais e aprendizado profundo**, para refinar as análises.  

        ✅ **6. Expansão do Dashboard e Storytelling dos Dados**  
        - Criar dashboards mais interativos com integração direta ao banco de dados.  
        - Incorporar análises preditivas diretamente no painel para facilitar a tomada de decisão.  

        ---

        ## ⚠️ Pontos de Atenção  

        ⚠️ **Dados Incompletos e Qualidade da Informação**  
        - Algumas bases de dados apresentaram **lacunas e valores ausentes**. É essencial estruturar um sistema de coleta mais eficiente para garantir dados completos e confiáveis.

        ⚠️ **Risco de Interpretação Equivocada dos Indicadores**  
        - Alguns alunos podem apresentar **notas altas, mas baixo engajamento**, o que pode mascarar problemas futuros. A análise deve ser sempre combinada com acompanhamento pedagógico.

        ⚠️ **Necessidade de Adaptação Contínua**  
        - O cenário educacional muda constantemente. Estratégias eficazes hoje podem não ser as mesmas no futuro, exigindo **monitoramento e ajustes frequentes nas políticas educacionais**.

        ---

        ## 🎯 Conclusão Final  

        Este projeto demonstrou que **dados bem estruturados e análises avançadas podem transformar a educação**, permitindo intervenções mais precisas e impactantes. A **Passos Mágicos** já desempenha um papel essencial no desenvolvimento educacional dos alunos e, com a implementação das recomendações, pode potencializar ainda mais seus resultados.

        O uso de **machine learning, análise preditiva e storytelling de dados** permitiu criar um sistema capaz de **identificar alunos em risco, otimizar estratégias pedagógicas e tomar decisões baseadas em evidências**. O próximo passo é expandir essa abordagem, garantindo que cada aluno receba o suporte necessário para alcançar seu máximo potencial. 🚀📚  

        > **"Educação não transforma o mundo. Educação muda pessoas. Pessoas transformam o mundo."** – Paulo Freire  

    """)

if __name__ == "__main__":
    main()
