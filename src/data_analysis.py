import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
ratings = pd.read_csv('/Users/joaopedrobrandao/Projetos/ecommerce-recommendation-system/data/ratings.csv')
movies = pd.read_csv('/Users/joaopedrobrandao/Projetos/ecommerce-recommendation-system/data/movies.csv')

# Visualizando as primeiras linhas
print("Primeiras linhas de 'ratings':")
print(ratings.head())

print("\nPrimeiras linhas de 'movies':")
print(movies.head())

# Estatísticas básicas
print("\nEstatísticas de 'ratings':")
print(ratings.describe())

print("\nDistribuição das avaliações:")
plt.hist(ratings['rating'], bins=10)
plt.title('Distribuição das Avaliações')
plt.xlabel('Avaliação')
plt.ylabel('Frequência')
plt.show()