# /app/main.py
from fastapi import FastAPI
from .routers.status import router as status
from .routers.predict_routes import router as predict_router
from .routers.upload_routes import router as upload_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(status)
app.include_router(predict_router)
app.include_router(upload_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
