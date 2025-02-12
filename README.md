# Análise de Indicadores Educacionais e Desempenho Acadêmico

## Visão Geral
Este repositório contém a análise de indicadores educacionais, com foco no desempenho acadêmico, engajamento dos alunos e análise preditiva de tendências de desempenho, utilizando dados de 2020 a 2022. O projeto inclui visualizações interativas, modelos preditivos e recomendações baseadas nos dados disponíveis.

## Funcionalidades Principais
- **Dashboard Interativo**: Visualizações dinâmicas dos indicadores acadêmicos.
- **Modelo Preditivo - FORECAST**: Previsão do desempenho futuro dos alunos com base em modelos estatísticos.

# Tecnologias Utilizadas

Para o desenvolvimento deste projeto, diversas **ferramentas e tecnologias** foram empregadas, garantindo a qualidade da análise de dados, modelagem preditiva e apresentação dos resultados. Abaixo, destacamos as principais tecnologias utilizadas:

## **Bibliotecas de Machine Learning e Estatística**
O projeto faz uso de bibliotecas amplamente utilizadas para **treinamento, validação e avaliação de modelos preditivos**:

- **`scikit-learn`**: Biblioteca essencial para **aprendizado de máquina**, utilizada para dividir os dados (`train_test_split`), avaliar modelos (`cross_val_score`) e calcular métricas como **acurácia, F1-score, precisão e recall**.
- **`imblearn (imbalanced-learn)`**: Utilizada para lidar com o **desbalanceamento dos dados** por meio da técnica **SMOTE (Synthetic Minority Over-sampling Technique)**, garantindo um melhor equilíbrio entre classes na modelagem preditiva.
- **`xgboost`**: Implementação eficiente do **gradiente boosting**, usada para treinar modelos altamente performáticos.
- **`joblib`**: Utilizado para **salvar e carregar modelos de machine learning** de forma otimizada.

## **Modelos de Machine Learning Implementados**
Diferentes **modelos supervisionados** foram testados e comparados para obter a melhor performance:

- **Random Forest (`RandomForestClassifier`)** → Algoritmo baseado em árvores de decisão que melhora a precisão ao combinar várias árvores.
- **Suporte a Vetores de Máquinas (`SVC`)** → Modelo poderoso para classificação de dados não lineares.
- **Regressão Logística (`LogisticRegression`)** → Modelo estatístico utilizado para prever a probabilidade de uma classe.
- **Árvores de Decisão (`DecisionTreeClassifier`)** → Algoritmo interpretável para tomada de decisões com base em regras.
- **K-Nearest Neighbors (`KNeighborsClassifier`)** → Modelo baseado na proximidade dos dados para realizar classificações.
- **XGBoost (`XGBClassifier`)** → Algoritmo baseado em boosting, utilizado para melhorar a performance e lidar com grandes volumes de dados.

## **Infraestrutura de Banco de Dados**
O projeto utilizou um **banco de dados relacional na nuvem** para armazenar e processar grandes volumes de dados educacionais:

- **Amazon RDS (Relational Database Service)**  
  - O banco de dados escolhido foi o **PostgreSQL**, devido à sua robustez, escalabilidade e compatibilidade com análises avançadas.
  - Utilizado para armazenar e consultar informações sobre os alunos, permitindo análises aprofundadas.

- **Processamento de Dados**:
  - Apache Spark: Manipulação de grandes volumes de dados.

## **Visualização e Storytelling dos Dados**
A apresentação dos insights e resultados do projeto foi feita utilizando **ferramentas de visualização de dados**:

- **Power BI** → Criamos **dashboards interativos** para explorar os impactos da ONG Passos Mágicos nos alunos.
- **Matplotlib & Seaborn** → Utilizados para a **análise exploratória de dados (EDA)**, gerando gráficos e matrizes de correlação para identificar padrões nos dados.

## **Hospedagem e Desenvolvimento**
- **Streamlit** → Utilizado para desenvolver uma interface interativa e acessível para análise e previsão de risco acadêmico.
- **AWS (Amazon Web Services)** → Além do **banco de dados RDS**, a AWS foi utilizada para armazenar e processar os dados de forma segura e escalável.


## Acesso às Ferramentas
- **Dashboard Interativo**: Disponível em Streamlit para visualização dinâmica.
- **Dashboard Complementar**: Disponível em Power BI para análises complementares.

## Análise dos Indicadores Acadêmicos

### 1. Evolução da Classificação dos Alunos por Ano
- **2020**: Maioria classificada como Ametista.
- **2021**: Redução em Ametista, aumento de Ágata.
- **2022**: Predominância de Topázio.

Essa evolução reflete mudanças no critério de avaliação ou melhora no desempenho.

### 2. Análise dos Indicadores Educacionais (2020-2022)
- **INDE (Desempenho Acadêmico)**: Queda em 2021 devido ao ensino remoto, com recuperação em 2022.
- **IDA (Indicador de Aprendizagem)**: Queda em 2021, seguido por recuperação.
- **IEG (Engajamento)**: Queda acentuada em 2021, mas com recuperação em 2022.
- **IPS (Bem-estar Psicossocial)**: Aumento durante a crise, refletindo esforços de suporte emocional.
- **IPP (Suporte Pedagógico)**: Estabilidade em 2020/2021 e aumento significativo em 2022.

### 3. Matriz de Correlação entre Indicadores Acadêmicos
- Correlação forte entre INDE, IEG e IPV.
- Correlação moderada entre IPS e IPV, sugerindo a importância do suporte psicossocial para momentos críticos de mudança.

## Conclusões

- **Impacto da Pandemia**: O ano de 2021 foi marcado por quedas nos indicadores de desempenho e engajamento devido ao impacto da pandemia. Contudo, 2022 mostrou uma recuperação substancial.
  
- **Engajamento e Desempenho**: A relação forte entre engajamento e desempenho destaca a importância de estratégias que promovam a participação ativa dos alunos.

- **Mudanças nas Classificações**: A diversificação nas classificações ao longo dos anos sugere uma reavaliação dos critérios de avaliação, refletindo a evolução do sistema educacional.

## Recomendações

- **Focar em Subconjuntos de Dados Completos**: Priorizar dados completos para análises mais precisas.
- **Documentar Limitações**: Registrar as limitações devido à falta de dados ausentes, garantindo uma interpretação mais cautelosa.
- **Melhorar a Coleta de Dados**: Reforçar a coleta de dados sobre desempenho acadêmico, frequência e aspectos socioeconômicos.

## Limitações

- A falta de dados em variáveis essenciais comprometeu a análise de certas áreas, como o desempenho detalhado e a frequência escolar.
- A predominância de valores "Não Informado" em algumas colunas sugere que os dados coletados são incompletos e podem afetar a precisão das conclusões.
