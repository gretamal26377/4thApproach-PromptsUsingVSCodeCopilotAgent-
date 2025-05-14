from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from . import models, schemas, crud, auth, customer_routes
from .database import engine, get_db
from .auth import create_access_token
from .config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Marketplace API")

# CORS for customer frontend only
origins = [
    "http://localhost:3000",  # customer frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include only customer router
app.include_router(customer_routes.router)

# Token endpoint (for customer login)
@app.post("/token", response_model=schemas.UserOut)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user": schemas.UserOut.from_orm(user)}
