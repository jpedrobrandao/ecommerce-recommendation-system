# Sistema de Recomendação para E-commerce

Este projeto implementa um sistema de recomendação baseado em filtragem colaborativa para um cenário de e-commerce. O sistema sugere produtos (filmes, neste caso) com base no histórico de compras e comportamento de navegação dos usuários.

**Estrutura do Projeto**
ecommerce-recommendation-system/
│
├── data/                     # Pasta para armazenar os dados brutos
│   ├── ratings.csv           # Avaliações dos usuários
│   └── movies.csv            # Informações sobre os filmes
│
├── src/                      # Código-fonte do projeto
│   ├── recommendation_model.py  # Modelo de recomendação
│   ├── app.py                # API FastAPI para servir as recomendações
│   ├── dashboard.py          # Dashboard interativo usando Streamlit
│   └── test_recommendation.py # Script para testar o modelo
│
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto

**Como Executar o Projeto**

**1. Configuração Inicial**
**1.1. Clone o Repositório**
Clone este repositório para sua máquina local:

