from src.recommendation_model import recommend_movies

if __name__ == "__main__":
    print("Testando a função recommend_movies:")
    recommendations = recommend_movies(user_id=1, n_recommendations=5)
    print(recommendations)