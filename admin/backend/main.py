import os
import sys

# Update sys.path to point to customer/backend/app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../customer/backend/app')))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from admin_routes import router as admin_router
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Marketplace Admin API")

origins = [
    "http://localhost:3001",  # admin frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_router)

@app.get("/")
def root():
    return {"message": "Marketplace Admin API running"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")