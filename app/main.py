from fastapi import FastAPI

from app.database import Base, engine
from app.auth import router as auth_router
from app.routes import router as api_router
from app.routes import router as protected_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure AI API Gateway",
    version="1.0.0",
)

app.include_router(auth_router)

app.include_router(api_router)
app.include_router(protected_router)


@app.get("/")
def root():
    return {"message": "Secure AI API Gateway is running successfully!"}


@app.get("/health")
def health():
    return {"status": "healthy"}