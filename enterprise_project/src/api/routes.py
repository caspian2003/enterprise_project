from fastapi import APIRouter
from src.services.processor import process_data

router = APIRouter()

@router.get("/process")
async def process():
    data = ["task1", "task2", "task3"]
    result = await process_data(data)
    return {"result": result}