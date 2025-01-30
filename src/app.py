from fastapi import FastAPI
from pydantic import BaseModel
from src.recommendation_model import recommend_movies

# Cria a instância do FastAPI
app = FastAPI()

class UserRequest(BaseModel):
    user_id: int
    n_recommendations: int = 5

@app.post("/recommend/")
def recommend(request: UserRequest):
    recommendations = recommend_movies(request.user_id, request.n_recommendations)
    return {"recommendations": recommendations}