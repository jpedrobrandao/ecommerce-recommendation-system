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

Como Executar o Projeto
1. Configuração Inicial
1.1. Clone o Repositório
Clone este repositório para sua máquina local:
bash
Copy
1
2
git clone https://github.com/seu-usuario/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
1.2. Crie e Ative um Ambiente Virtual
Crie um ambiente virtual para instalar as dependências do projeto:
No Linux/Mac:
bash
Copy
1
2
python -m venv venv
source venv/bin/activate
No Windows:
bash
Copy
1
2
python -m venv venv
venv\Scripts\activate
 1.3. Instale as Dependências
Instale as bibliotecas Python necessárias listadas no arquivo requirements.txt:
bash
Copy
1
pip install -r requirements.txt
2. Baixe os Dados
2.1. Crie a Pasta data/
Crie uma pasta chamada data/ na raiz do projeto:
bash
Copy
1
mkdir data
2.2. Baixe os Arquivos CSV
Baixe os arquivos ratings.csv e movies.csv do MovieLens Dataset e coloque-os na pasta data/.
Link direto para o dataset: MovieLens Latest Small Dataset
Após baixar o arquivo .zip, extraia os arquivos e mova ratings.csv e movies.csv para a pasta data/.
 3. Testar o Modelo de Recomendação
Execute o script de teste para verificar se o modelo está funcionando corretamente:
bash
Copy
1
python src/test_recommendation.py
Você deve ver as recomendações de filmes no terminal.
4. Executar a API FastAPI
Inicie o servidor FastAPI:
bash
Copy
1
uvicorn src.app:app --reload
A API estará disponível em http://127.0.0.1:8000. Você pode testar o endpoint /recommend/ usando curl ou Postman:
bash
Copy
1
2
3
curl -X POST "http://127.0.0.1:8000/recommend/" \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1, "n_recommendations": 5}'
Exemplo de resposta:
json
Copy
1
2
3
4
5
6
7
8
9
⌄
⌄
{
    "recommendations": [
        {"movieId": 3186, "title": "Shawshank Redemption, The (1994)"},
        {"movieId": 2968, "title": "Pulp Fiction (1994)"},
        {"movieId": 2028, "title": "Forrest Gump (1994)"},
        {"movieId": 1198, "title": "Star Wars: Episode V - The Empire Strikes Back (1980)"},
        {"movieId": 589, "title": "Terminator 2: Judgment Day (1991)"}
    ]
}
5. Executar o Dashboard Interativo
Inicie o dashboard interativo usando Streamlit:
bash
Copy
1
streamlit run src/dashboard.py
O dashboard estará disponível em http://localhost:8501. Nele, você pode inserir o ID do usuário e o número de recomendações desejadas para visualizar os resultados em uma interface gráfica.
Funcionalidades do Projeto
Modelo de Recomendação :
Usa filtragem colaborativa baseada em k-NN para sugerir filmes.
Retorna as recomendações em formato JSON ou gráfico.
 API FastAPI :
Fornece um endpoint /recommend/ para obter recomendações via requisições HTTP.
 Dashboard Interativo :
Interface visual criada com Streamlit para explorar as recomendações de forma intuitiva.
