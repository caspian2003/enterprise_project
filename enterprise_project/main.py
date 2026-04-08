from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Enterprise App")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Enterprise App Running"}