from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, crud, auth, models
from .database import get_db
from typing import List

router = APIRouter(tags=["customer"])

# Register new user
@router.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_email = crud.get_user_by_email(db, user.email)
    if db_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

# List products
@router.get("/products", response_model=List[schemas.ProductOut])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

# Get product detail
@router.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Place order
@router.post("/orders", response_model=schemas.OrderOut)
def place_order(order: schemas.OrderCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_order(db, customer_id=current_user.id, order=order)

# List my orders
@router.get("/orders", response_model=List[schemas.OrderOut])
def list_my_orders(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.get_orders_by_customer(db, customer_id=current_user.id)
