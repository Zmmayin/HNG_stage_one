import time
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def check_response_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration_ms = (time.time() - start) * 1000  # Convert to milliseconds
    response.headers["X-Response-Time"] = f"{duration_ms:.2f}ms"
    if duration_ms > 500:
        print(f"Warning: Slow response time of {duration_ms:.2f}ms for {request.url}")
    return response
    

@app.get("/", status_code=200)
async def root():
    return {"message": "API is running"}

@app.get("/health", status_code=200)
async def health():
    return {"message": "healthy"}

@app.get("/me", status_code=200)
async def me():
    return {
        "name": "Emmanuel Ifelowo",
        "email": "eifelowo@gmail.com",
        "github": "https://github.com/Zmmayin"
    }
