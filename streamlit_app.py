import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


def forecast_performance(data, model):
    return model.predict(data)[0]

def lineChart(dataframe, x, y, title, xaxis_title, yaxis_title, legendas = {}):
    fig = px.line(dataframe, x=x, y=y, title=title)

    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        legend_title="Legenda",
    )

    if len(legendas) > 0:
        fig.for_each_trace(lambda t: t.update(name = legendas[t.name]))

    return fig

def barChart(dataframe, x, y, title, xaxis_title, yaxis_title):
    fig = px.bar(dataframe, x=x, y=y, title=title)

    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        legend_title="Legenda",
    )

    return fig

def scatterChart(dataframe, x, y, title, xaxis_title, yaxis_title, color=None):
    fig = px.scatter(dataframe, x=x, y=y, title=title, color=color, trendline="ols", trendline_scope="overall", trendline_color_override="white")

    fig.update_layout(
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        legend_title="Legenda",
    )

    return fig

st.set_page_config(
    page_title="Análise",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    df = pd.read_csv('base_streamlit/aluno.csv')
    df_model= pd.read_csv('base_streamlit/treino_resultado.csv', sep=';')
    sUrl =  'melhor_modelo_support_vector_machine.pkl'
    lano = {'Todos': 'Todos','2020': 2020, '2021': 2021, '2022':2022}
    lIndicadores_1 = ['inde', 'iaa', 'ieg','ips','ida', 'ipp', 'ipv','ian']
    lpedras = ['Topázio', 'Ametista', 'Ágata', 'Quartzo']
    st.sidebar.title("Menu de Navegação")

    pages = [
        "Início",
        "Análise",
        "Modelo de Machine Learning",   
        "Análise com Power BI",
        "Conclusão",
        "Tecnologias Utilizadas",
    ]

    page = st.sidebar.radio("Navegue pelo Projeto", pages)

    if page == "Início":
        show_home()
    elif page == "Análise":
        show_analise(df, lano, lIndicadores_1, lpedras)
    elif page == "Modelo de Machine Learning":
        show_modelo(df_model)
    elif page == "Análise com Power BI":
        show_power_bi()
    elif page == "Conclusão":
        show_conclusao()
    elif page == "Tecnologias Utilizadas":
        show_tecnologias()

def show_home():
    st.title('**Introdução**')

    tab1, tab2, tab3 = st.tabs(['Sobre a Passos Mágicos', 'Sobre o Projeto', 'Dicionário'])

    with tab1:
        st.subheader('**Quem somos?**')
        st.write(""" A Associação Passos Mágicos possui uma história de 31 anos dedicada a transformar a vida de crianças e jovens de baixa renda, oferecendo-lhes melhores perspectivas de futuro. """)
        st.write(""" Essa iniciativa, idealizada por Michelle Flues e Dimetri Ivanoff, teve início em 1992, com atividades realizadas em orfanatos no município de Embu-Guaçu. """)
        st.write(""" Em 2016, após anos de experiência e aprendizado, decidiram expandir o alcance do programa para beneficiar um maior número de jovens. Essa transformação, baseada em uma abordagem que combina educação de qualidade, suporte psicológico e psicopedagógico, ampliação da visão de mundo e incentivo ao protagonismo, resultou na criação da Associação Passos Mágicos como um projeto social e educacional. """)
        st.divider()
        st.subheader('**O que fazemos?**')
        st.write(""" A Passos Mágicos transforma vidas por meio da educação, oferecendo aulas de alfabetização, língua portuguesa e matemática para crianças e adolescentes de 7 a 17 anos residentes em Embu-Guaçu. Os estudantes são organizados em turmas de acordo com seu nível de aprendizado, definido por uma avaliação diagnóstica realizada no momento da inscrição. """)
        st.write(""" Atualmente, a instituição impacta diretamente 1.000 alunos, distribuídos em diferentes etapas de aprendizado: """)
        st.write(""" - Fase Alfabetização: Para alunos em processo de alfabetização ou com dificuldades na leitura e escrita (20% dos alunos).\n
    - Fases 1 e 2: Aprofundamento dos conteúdos do Ensino Fundamental 1 (37% dos alunos).\n
    - Fases 3 e 4: Foco no Ensino Fundamental 2, com ênfase no aprofundamento de matérias (24% dos alunos).\n
    - Fases 5 e 6: Voltadas para o Ensino Médio, atendendo jovens e adolescentes (8% dos alunos).\n
    - Fases 7 e 8: Preparação intensiva para vestibulares e exames do último ano do Ensino Médio (11% dos alunos). """)
        st.write("""Além disso, a Passos Mágicos oferece programas educacionais inovadores, como: """)
        st.write(""" - Preparação para vestibulares e escolas técnicas por meio do programa Vem Ser.\n
    - Cursos avançados em parceria com a USP, incluindo disciplinas como Sustentabilidade, Computação e Programação, oferecendo oportunidades únicas de aprendizado. """)
        st.write(""" Ciente de que o suporte emocional é essencial para o sucesso acadêmico, a Passos Mágicos também disponibiliza acompanhamento psicológico individual e em grupo para alunos e seus familiares, promovendo bem-estar e equilíbrio emocional para enfrentar os desafios da educação. """)
        st.divider()
        st.subheader('**Impacto (indicadores 2023)**')
        st.write(""" Pessoas Impactadas: **4400** (considerando a média de 4 familiares por aluno) """)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(""" Alunos no programa de Aceleração do Conhecimento: **1100 alunos** """)
            st.write(""" - 20% na alfabetização """)
            st.write(""" - 37% nas turmas 1 e 2 """)
            st.write(""" - 24% nas turmas 3 e 4 """)
            st.write(""" - 8% nas turmas 5 e 6 """)
            st.write(""" - 11% nas turmas 7 e 8 """)

        with col2:
            st.write(""" Bolsistas em instituições de ensino particular: **98 alunos** """)
            st.write(""" - Colégio Evolução Arco Íris: 75 alunos """)
            st.write(""" - Albert Einstein: 8 alunos """)
            st.write(""" - Escola João Paulo II: 1 aluno """)
            st.write(""" - Colégio Poliedro: 2 alunos """)
            st.write(""" - FIAP: 12 alunos """)
        
        with col3:
            st.write(""" Universitários em instituições de ensino superior: **103 alunos** """)
            st.write(""" - ESPM: 4 alunos """)
            st.write(""" - Estácio: 5 alunos """)
            st.write(""" - FIAP: 46 alunos """)
            st.write(""" - UNISA: 39 alunos """)

    with tab2:
        st.write(""" O objetivo do projeto é criar uma solução preditiva para monitorar o desempenho escolar dos alunos, identificando aqueles com resultados acima ou abaixo do esperado. A avaliação será baseada em indicadores como Desempenho Acadêmico, Psicopedagógico, Engajamento, Autoavaliação, Adequação de Nível e Ponto da Virada. Para isso, será empregado o modelo de machine learning que apresentou o melhor desempenho segundo as métricas de F1 Score, Acurácia, Precisão e Recall. """)
        st.write(""" Adicionalmente, será conduzida uma análise exploratória para evidenciar os impactos gerados pela Passos Mágicos no desempenho dos estudantes. Essa análise levantará indicadores de performance, detalhando a evolução de cada métrica e explorando o comportamento das Pedras, além de ilustrar graficamente os momentos em que o Ponto de Virada ocorre com maior frequência. """)

    with tab3:
        col1, col2, col3= st.columns(3)

        with col1:
            st.subheader('**IAN**')
            st.write('Indicador de adequação de nível')
            st.write('Originário de resgistro administrativos')
        with col2:
            st.subheader('**IDA**')
            st.write('Indicador de desempenho acadêmico')
            st.write('Notas de provas e média geral universitária')
        with col3:
            st.subheader('**IEG**')
            st.write('Indicador de engajamento')                
            st.write('Registro de entregas de lições de casa e voluntariado')                
        
        col4, col5, col6 = st.columns(3)

        with col4:
            st.subheader('**IAA**')
            st.write('Indicador de autoavaliação')           
            st.write('Questionário de autoavaliação individual')           

        with col5:
            st.subheader('**IPP**')
            st.write('Indicador psicopedagógico')
            st.write('Questionário de avalidação dos pedagogos e professores')
        with col6:
            st.subheader('**IPV**')
            st.write('Indicador do ponto da virada')            
            st.write('Questionário de avalidação dos pedagogos e professores')

def show_analise(df, lano, lIndicadores_1, lpedras):
    tab1, tab2 = st.tabs(['Análise Exploratória', 'Gráficos'])

    with tab1:
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

        num_colunas = len(lIndicadores_1)
        colunas_1 = st.columns(num_colunas, border=True)

        for i, dados in enumerate(lIndicadores_1):
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

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            cbano_grafico = st.selectbox('Selecione o ano:', list(lano.keys()), key = "cbano_grafico")
        with col2:
            cbIndicador = st.selectbox('Selecione o Indicador:', lIndicadores_1[1:], key = "cbIndicador")

        df_ano_grafico = df    
        if(cbano_grafico != 'Todos'):
            df_ano_grafico = df[df['ano'] == lano[cbano_grafico]]       

        st.plotly_chart(scatterChart(df_ano_grafico, 'inde', cbIndicador, 'Relação de Crescimento do inde', 'inde', cbIndicador, color='pedra'), use_container_width=True)

        st.expander(' :bulb: Considerações', expanded=False).markdown("""O gráfico de dispersão ilustra como as outras notas variam em relação ao índice inde, permitindo uma análise visual dessa relação. Além disso, o gráfico inclui uma linha de tendência, que facilita a identificação de um padrão: se o comportamento das notas em relação ao inde apresenta uma tendência de crescimento ou declínio""")
   
def show_modelo(df_model):
    st.header('**Modelo de Machine Learning**')
    st.markdown(""" Preencha os campos abaixo para realizar a previsão""")
    modelo = joblib.load('melhor_modelo_support_vector_machine.pkl')
    tab1, tab2 = st.tabs(['Previsões', 'Relatório'])

    with tab1:
        with st.form(key='form', enter_to_submit=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                iaa = st.number_input('iaa', min_value=0, max_value=10, value=5)
                ipp = st.number_input('ipp', min_value=0, max_value=10, value=5)

            with col2:
                ieg = st.number_input('ieg', min_value=0, max_value=10, value=5)
                ipv = st.number_input('IPV', min_value=0, max_value=10, value=5)

            with col3:
                ips = st.number_input('ips', min_value=0, max_value=10, value=5)                
                ian = st.number_input('ian', min_value=0, max_value=10, value=5)                

            with col4:
                ida = st.number_input('ida', min_value=0, max_value=10, value=5)

            co5,col6,col7 = st.columns([1,1,1], border=False, vertical_alignment='center')

            with col6:
                submit = st.form_submit_button('Realizar previsão', type='primary', use_container_width=True, help='Clique para realizar a previsão de performance do aluno')
            
            if submit:
                dados = {'iaa':iaa, 'ieg':ieg, 'ips':ips, 'ida':ida, 'ipp':ipp, 'ipv':ipv, 'ian':ian}
                data = pd.DataFrame([dados])
                resultado = forecast_performance(data, modelo)
                if resultado == 0:
                    st.subheader('**Aluno com baixa performance**')
                else:
                    st.subheader('**Aluno com alta performance**')

            st.expander(':bulb: Considerações', expanded=False).write(""" Este modelo foi desenvolvido para avaliar o desempenho dos alunos, utilizando como base suas notas e um sistema de classificação chamado "pedras". Entre as categorias de pedras, destaca-se a "Quartzo", que representa alunos com baixo desempenho. Com isso, ao inserir as notas no modelo, ele pode prever se o aluno em questão tem risco de apresentar uma performance insatisfatória. Essa previsão permite que os responsáveis tomem medidas proativas, oferecendo o suporte necessário para melhorar o desempenho do aluno. """)

    with tab2:
        st.write('**Relatório de performance**')
        st.write(""" Para determinar o modelo mais eficiente na previsão do desempenho escolar dos alunos, foi realizada uma análise comparativa envolvendo diversos algoritmos de aprendizado de máquina. Esses modelos foram treinados utilizando as informações fornecidas no dataset, abrangendo variáveis relacionadas ao desempenho escolar. Após o treinamento, os resultados de cada modelo foram avaliados e organizados em um dataframe estruturado. Esse dataframe contém informações detalhadas, incluindo o nome do modelo, os valores obtidos na validação cruzada, bem como as métricas de desempenho mais relevantes: F1 Score, Acurácia, Precision e Recall. Essas métricas foram escolhidas para garantir uma avaliação abrangente, especialmente considerando o equilíbrio entre precisão e sensibilidade nos casos de desbalanceamento de classes. """) 

        st.write(""" Com base na análise das métricas de desempenho, deu-se ênfase ao F1 Score como critério principal de avaliação devido ao desbalanceamento observado no dataset original. Essa escolha foi feita porque o F1 Score equilibra a precisão (precision) e a sensibilidade (recall), sendo ideal para cenários em que há classes desproporcionais. Após a comparação dos resultados entre os modelos testados, o Support Vector Machine (SVM) foi identificado como o mais adequado para resolver o problema proposto, apresentando o melhor desempenho em termos de F1 Score. """)

        st.dataframe(df_model.style.highlight_max(axis=0, color='green'), use_container_width=True)    

        st.write("Os resultados obtidos com o modelo Support Vector Machine (SVM) são apresentados na tabela acima. O SVM obteve o melhor desempenho em termos de F1 Score, Acurácia, Precision e Recall, superando os demais modelos avaliados. Esses resultados reforçam a eficácia do SVM na previsão do desempenho escolar dos alunos, destacando sua capacidade de lidar com classes desbalanceadas e fornecer previsões precisas e confiáveis. Portanto, o SVM foi selecionado como o modelo final para a realização das previsões de desempenho dos alunos neste projeto.")   

def show_power_bi():
    st.header('**Dashboard**')

    iframe_url = "https://app.powerbi.com/view?r=eyJrIjoiMGFmNDAzNTEtMWZkYS00NGFiLWEyN2YtMmRkZjIwNjUyZTA2IiwidCI6IjZkYzg3NGNlLWRkMmItNGFhOS05ZjBkLWFkYjkyNjlhNzU4MCJ9 "

    components.iframe(iframe_url, width=1400, height=650)

def show_conclusao():
    st.title('**Conclusão**')

    st.write(""" O objetivo do projeto foi desenvolver uma solução em machine learning utilizando o modelo Support Vector Machine (SVM) para identificar de forma objetiva os alunos com risco de reprovação. A análise foi baseada em um conjunto de dados composto por notas acadêmicas e indicadores de desempenho, viabilizando o planejamento de intervenções educacionais mais assertivas e direcionadas. """)
    st.write(""" O modelo utilizou técnicas robustas para lidar com dados desbalanceados como a técnica de balanceamento SMOTE (Synthetic Minority Over-sampling Technique), aplicada para lidar com classes desbalanceadas em conjuntos de dados. A quantidade de alunos "em risco" era significativamente menor do que a de alunos "não em risco", o que poderia resultar em um modelo com baixa capacidade de previsão para a classe minoritária. Nesse contexto, o SMOTE foi crucial para gerar novos exemplos sintéticos para a classe minoritária, equilibrando o número de exemplos entre as classes e, assim, melhorando o desempenho do modelo. """)

    st.divider()

    st.subheader("**Benefícios do Modelo**")
    st.write(""" **1. Intervenção Proativa:** Um dos principais benefícios de prever o risco de baixa performance é a capacidade de agir antecipadamente, antes que o aluno alcance um nível crítico de dificuldades acadêmicas. Isso possibilita intervenções mais eficazes e assertivas. """)
    st.write("""**2. Apoio Personalizado:** Com base nas previsões fornecidas pelo modelo, é possível oferecer um suporte personalizado, ajustando as intervenções de acordo com as necessidades individuais de cada aluno, garantindo uma abordagem mais direcionada e eficaz. """)
    st.write(""" **3. Otimização na Alocação de Recursos:** Ao identificar com precisão os alunos que realmente necessitam de apoio, o modelo permite à Passos Mágicos alocar seus recursos de maneira mais estratégica. Isso assegura que a ajuda seja direcionada especificamente aos estudantes em risco, evitando a distribuição indiscriminada de recursos e garantindo um suporte mais eficiente e focado. """)
    st.write(""" **4. Acompanhamento e Monitoramento Contínuo:** O modelo também pode ser utilizado para um acompanhamento constante do desempenho dos alunos ao longo do tempo. À medida que novos dados são coletados, as previsões podem ser atualizadas, ajustando o suporte conforme necessário. Por exemplo, se um aluno inicialmente em risco melhora seu desempenho após a intervenção, o modelo refletirá essa mudança, ajustando a previsão para "não está mais em risco". Esse processo contínuo permite que a instituição acompanhe a eficácia das intervenções e ajuste suas estratégias de forma dinâmica e em tempo real. """)
    st.write(""" Em resumo, o modelo de previsão de risco oferece vantagens significativas, como a intervenção precoce, personalização do suporte, eficiência na alocação de recursos, melhoria da retenção de alunos, e monitoramento contínuo do progresso acadêmico. Essas ações não só ajudam os alunos a alcançarem um melhor desempenho, mas também promovem uma gestão acadêmica mais eficaz e uma instituição mais bem-sucedida no apoio a seus estudantes. """)

    st.divider()

    st.subheader("**Links Relevantes**")
    st.write(""" - [Passos Mágicos](https://passosmagicos.org.br)""")
    st.write(""" - [Repositório no GitHub](https://github.com/Rogeriom49/datathon_fiap)""")
    st.write(""" - [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMGFmNDAzNTEtMWZkYS00NGFiLWEyN2YtMmRkZjIwNjUyZTA2IiwidCI6IjZkYzg3NGNlLWRkMmItNGFhOS05ZjBkLWFkYjkyNjlhNzU4MCJ9)""")

def show_tecnologias():
    st.title('**Tecnologias**')

    with st.container():
        st.write('1. **[Streamlit](https://streamlit.io/)** - Criação do MVP (Produto Mínimo Viável) para aplicações interativas e visuais de ciência de dados.  ')
        st.write('2. **[Pandas](https://pandas.pydata.org/)** - Manipulação e análise de dados com suporte para estruturas de dados como DataFrames.')
        st.write('3. **[Scikit-learn](https://scikit-learn.org/)** - Treinamento e avaliação de modelos de machine learning, com uma ampla gama de algoritmos prontos para uso.')
        st.write("4. **[Matplotlib](https://matplotlib.org/)** e **[Plotly](https://plotly.com/)** - Visualização de dados para gráficos estáticos e interativos, respectivamente.")  
        st.write('5. **[NumPy](https://numpy.org/)** - Funções estatísticas e manipulação de arrays multidimensionais para operações matemáticas eficientes.')
        st.write('6. **[GitHub](https://github.com/)** - Versionamento do projeto.')
        st.write('7. **[Power BI](https://powerbi.microsoft.com/)** - Criação do dashboard final.')

# Executar a aplicação
if __name__ == "__main__":
    main()
    