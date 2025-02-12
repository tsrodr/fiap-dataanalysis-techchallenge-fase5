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
1. **Dashboard Interativo**:
   - Disponível em [Streamlit](https://fiap-dataanalysis-techchallenge-fase5-whbkrxfjy7xfhvappzq3bk2.streamlit.app).
2. **Dashboard Complementar**:
   - Disponível em [Power BI](https://app.powerbi.com/view?r=eyJrIjoiNGNlYjNjMzYtODNkNC00ZDk4LTkwYzItZGJiODZiMTAwNzVhIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9).

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


## 📌 Conclusão Final do Projeto  

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

