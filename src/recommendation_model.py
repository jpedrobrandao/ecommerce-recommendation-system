import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Carregando os dados
ratings = pd.read_csv('/Users/joaopedrobrandao/Projetos/ecommerce-recommendation-system/data/ratings.csv')
movies = pd.read_csv('/Users/joaopedrobrandao/Projetos/ecommerce-recommendation-system/data/movies.csv')

# Criando uma matriz esparsa diretamente
def create_sparse_matrix(ratings):
    # Crie uma matriz esparsa com userId como linha, movieId como coluna e rating como valor
    sparse_matrix = csr_matrix((ratings['rating'], (ratings['userId'], ratings['movieId'])))
    return sparse_matrix

# Criando a matriz esparsa
sparse_matrix = create_sparse_matrix(ratings)

# Treinando o modelo k-NN
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(sparse_matrix)

def recommend_movies(user_id, n_recommendations=5):
    # Verifica se o user_id existe no dataset
    if user_id not in ratings['userId'].unique():
        return {"error": f"User ID {user_id} not found in the dataset."}

    # Encontra os vizinhos mais próximos
    distances, indices = model_knn.kneighbors(sparse_matrix[user_id], n_neighbors=n_recommendations + 1)
    
    recommendations = []
    for i in range(1, len(indices.flatten())):
        similar_user_id = indices.flatten()[i]
        similar_user_ratings = ratings[ratings['userId'] == similar_user_id]
        recommended_movie_ids = similar_user_ratings['movieId'].values
        recommendations.extend(recommended_movie_ids[:n_recommendations])
    
    recommendations = list(set(recommendations))[:n_recommendations]
    recommended_movies = movies[movies['movieId'].isin(recommendations)]
    
    # Converte os tipos do NumPy para tipos nativos do Python
    formatted_recommendations = [
        {"movieId": int(row["movieId"]), "title": str(row["title"])}
        for _, row in recommended_movies.iterrows()
    ]
    
    return formatted_recommendations