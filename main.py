from fastapi import FastAPI
import uvicorn

from app.endpoints.login import loginrouter
from app.endpoints.tradings import tradesrouter
from config import API_URL


app = FastAPI()


app.include_router(loginrouter, prefix=f"{API_URL}/auth")
app.include_router(tradesrouter, prefix=f"{API_URL}/trades")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
