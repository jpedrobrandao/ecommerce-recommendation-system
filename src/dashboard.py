import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from recommendation_model import recommend_movies

# Carregue os dados de filmes
movies = pd.read_csv('/Users/joaopedrobrandao/Projetos/ecommerce-recommendation-system/data/movies.csv')

# Título do dashboard
st.title("Sistema de Recomendação de Filmes")

# Entradas do usuário
user_id = st.number_input("ID do Usuário:", min_value=1, value=1)
n_recommendations = st.number_input("Número de Recomendações:", min_value=1, value=5)

# Botão para gerar recomendações
if st.button("Gerar Recomendações"):
    # Obtenha as recomendações para o usuário
    recommendations = recommend_movies(user_id, n_recommendations)
    
    if "error" in recommendations:
        st.error(recommendations["error"])
    else:
        # Converta as recomendações em um DataFrame
        df_recommendations = pd.DataFrame(recommendations)
        
        # Exiba as recomendações em uma tabela
        st.subheader("Recomendações de Filmes")
        st.table(df_recommendations)
        
        # Crie um gráfico de barras
        st.subheader("Gráfico de Recomendações")
        fig, ax = plt.subplots()
        ax.barh(df_recommendations['title'], range(1, len(df_recommendations) + 1), color='skyblue')
        ax.set_xlabel('Ranking')
        ax.set_ylabel('Filme')
        ax.invert_yaxis()  # Inverte o eixo Y para exibir o ranking do maior para o menor
        st.pyplot(fig)