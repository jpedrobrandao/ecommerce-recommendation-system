# Sistema de Recomendação para E-commerce

Este projeto implementa um sistema de recomendação baseado em filtragem colaborativa para um cenário de e-commerce. O sistema sugere produtos (filmes, neste caso) com base no histórico de avaliações e comportamento dos usuários.


---

## Como Executar o Projeto

### 1. Configuração Inicial

#### 1.1 Clone o Repositório

Clone este repositório para sua máquina local:
```bash
git clone https://github.com/seu-usuario/ecommerce-recommendation-system.git
cd ecommerce-recommendation-system
```

### 1.2 Crie e Ative um Ambiente Virtual

Crie um ambiente virtual para instalar as dependências do projeto:

#### No Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
````

#### No Windows:
``` bash
python -m venv venv
venv\Scripts\activate
````
### 1.3 Instale as Dependências
Instale as bibliotecas Python necessárias listadas no arquivo requirements.txt:
```bash
pip install -r requirements.txt
```
## 2. Baixe os Dados
### 2.1 Crie a Pasta 
Crie uma pasta chamada **data** na raiz do projeto:
```bash
mkdir data
````

### 2.2 Baixe os Arquivos CSV
Baixe os arquivos ratings.csv e movies.csv do [MovieLens Dataset](https://grouplens.org/datasets/movielens/?spm=5aebb161.5237a6f8.0.0.2318c9218mqh9a) e coloque-os na pasta data. Após baixar o arquivo.zip, extraia os arquivos e mova ratings.csv e movies.csv para a pasta data

### 3. Testar o Modelo de Recomendação
Execute o script de teste para verificar se o modelo está funcionando corretamente:
```bash
python src/test_recommendation.py
Você deve ver as recomendações de filmes no terminal.
````

## 4. Execute a API FastAPI
Inicie o servidor FastAPI:
```bash
uvicorn src.app:app --reload
```
A API estará disponível em http://127.0.0.1:8000. Você pode testar o endpoint /recommend/ usando curl ou Postman:
```bash
curl -X POST "http://127.0.0.1:8000/recommend/" \
     -H "Content-Type: application/json" \
     -d '{"user_id": 1, "n_recommendations": 5}'
```
Exemplo de resposta:
```json
{
    "recommendations": [
        {"movieId": 3186, "title": "Shawshank Redemption, The (1994)"},
        {"movieId": 2968, "title": "Pulp Fiction (1994)"},
        {"movieId": 2028, "title": "Forrest Gump (1994)"},
        {"movieId": 1198, "title": "Star Wars: Episode V - The Empire Strikes Back (1980)"},
        {"movieId": 589, "title": "Terminator 2: Judgment Day (1991)"}
    ]
}
```

## 5. Execute o Dashboard Interativo
Inicie o dashboard interativo usando Streamlit:
```bash
streamlit run src/dashboard.py
```

O dashboard estará disponível em http://localhost:8501. Nele, você pode inserir o ID do usuário e o número de recomendações desejadas para visualizar os resultados em uma interface gráfica.

## Funcionalidades do Projeto
- ####	Modelo de Recomendação :

  - Usa filtragem colaborativa baseada em k-NN para sugerir filmes.
  - Retorna as recomendações em formato JSON ou gráfico.
- #### API FastAPI :
  - Fornece um endpoint /recommend/ para obter recomendações via requisições HTTP.
- #### Dashboard Interativo :
  - Interface visual criada com Streamlit para explorar as recomendações de forma intuitiva.

## Contribuições
Contribuições são bem-vindas! Se você encontrar bugs ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a [MIT License](https://choosealicense.com/licenses/mit/).
