import streamlit as st
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
    lAno = {'Todos': 'Todos','2020': 2020, '2021': 2021, '2022':2022}
    lIndicadores_1 = ['inde', 'iaa', 'ieg','ips','ida', 'ipp', 'ipv','ian']
    lPedras = ['Topázio', 'Ametista', 'Ágata', 'Quartzo']
    st.sidebar.title("Menu de Navegação")

    pages = [
        "Início",
        "Análise",
        "Modelo de Machine Learning",
        "Análise com Power BI"
    ]

    page = st.sidebar.radio("Navegue pelo Projeto", pages)

    if page == "Início":
        show_home()
    elif page == "Análise":
        show_analise(df, lAno, lIndicadores_1, lPedras)
    elif page == "Modelo de Machine Learning":
        show_modelo(df_model)



def show_home():
    st.title("O Projeto")

def show_analise(df, lAno, lIndicadores_1, lPedras):
    tab1, tab2 = st.tabs(['Análise Exploratória', 'Gráficos'])

    with tab1:
        cbAno = st.selectbox('Selecione o Ano:', list(lAno.keys()), key = "cbAno")

        df_ano = df    
        if(cbAno != 'Todos'):
            df_ano = df[df['ANO'] == lAno[cbAno]]
            if(lAno[cbAno] > 2020):
                df_ano_anterior = df[df['ANO'] == lAno[cbAno]-1]

        num_colunas_pedras = len(lPedras)
        colunas_2 = st.columns(num_colunas_pedras, border=True)
        for i, dados in enumerate(lPedras):
            coluna_atual = colunas_2[i % num_colunas_pedras]
            with coluna_atual:
                if(cbAno != 'Todos' and lAno[cbAno] > 2020):
                    st.metric(dados, label_visibility='visible', help='Comparativo em relação ao ano anterior', value=np.sum(df_ano['PEDRA'] == dados), delta= int(np.sum(df_ano['PEDRA'] == dados) - np.sum(df_ano_anterior['PEDRA'] == dados)))
                else:
                    st.metric(dados, np.sum(df_ano['PEDRA'] == dados), delta=None)            

        num_colunas = len(lIndicadores_1)
        colunas_1 = st.columns(num_colunas, border=True)

        for i, dados in enumerate(lIndicadores_1):
            coluna_atual = colunas_1[i % num_colunas]
            with coluna_atual:
                st.subheader(dados, help='Comparativo em relação ao ano anterior')
                if(cbAno != 'Todos' and lAno[cbAno] > 2020):
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
            cbAno_grafico = st.selectbox('Selecione o Ano:', list(lAno.keys()), key = "cbAno_grafico")
        with col2:
            cbIndicador = st.selectbox('Selecione o Indicador:', lIndicadores_1[1:], key = "cbIndicador")

        df_ano_grafico = df    
        if(cbAno_grafico != 'Todos'):
            df_ano_grafico = df[df['ANO'] == lAno[cbAno_grafico]]       

        st.plotly_chart(scatterChart(df_ano_grafico, 'INDE', cbIndicador, 'Relação de Crescimento do INDE', 'INDE', cbIndicador, color='PEDRA'), use_container_width=True)

        st.expander(' :bulb: Considerações', expanded=False).markdown("""O gráfico de dispersão ilustra como as outras notas variam em relação ao índice INDE, permitindo uma análise visual dessa relação. Além disso, o gráfico inclui uma linha de tendência, que facilita a identificação de um padrão: se o comportamento das notas em relação ao INDE apresenta uma tendência de crescimento ou declínio""")
        

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


# Executar a aplicação
if __name__ == "__main__":
    main()
    