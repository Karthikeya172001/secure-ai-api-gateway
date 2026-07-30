from fastapi import FastAPI

from app.database import Base, engine
from app.auth import router as auth_router
from app.routes import router as api_router
from app import admin
from app.limiter import limiter

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure AI API Gateway",
    version="1.0.0",
)



app.state.limiter = limiter
from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded

@app.exception_handler(RateLimitExceeded)
async def custom_rate_limit_handler(
    request: Request,
    exc: RateLimitExceeded,
):
    return JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded. Try again later."
        },
    )
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler,
)

app.add_middleware(SlowAPIMiddleware)

app.include_router(auth_router)
app.include_router(admin.router)
app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Secure AI API Gateway is running successfully!"}


@app.get("/health")
def health():
    return {"status": "healthy"}