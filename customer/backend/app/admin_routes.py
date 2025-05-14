from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, crud, auth, models
from .database import get_db
from typing import List

router = APIRouter(prefix="/admin", tags=["admin"])

# Admin: Get all users
@router.get("/users", response_model=List[schemas.UserOut])
def read_users(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_admin_user)):
    users = db.query(models.User).all()
    return users

# Admin: Get all products
@router.get("/products", response_model=List[schemas.ProductOut])
def read_products(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_admin_user)):
    return crud.get_products(db)

# Admin: Create product
@router.post("/products", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_admin_user)):
    return crud.create_product(db, product, owner_id=current_user.id)

# Admin: Update product
@router.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_admin_user)):
    return crud.update_product(db, product_id, product)

# Admin: Delete product
@router.delete("/products/{product_id}", response_model=schemas.ProductOut)
def delete_product(product_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_admin_user)):
    return crud.delete_product(db, product_id)

# Admin: Get all orders
@router.get("/orders", response_model=List[schemas.OrderOut])
def read_orders(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_admin_user)):
    return crud.get_all_orders(db)
