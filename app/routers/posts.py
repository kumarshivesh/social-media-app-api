from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas, database

router = APIRouter()

@router.post("/users/{user_id}/posts/", response_model=schemas.Post)
def create_post_for_user(user_id: int, post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    return crud.create_post(db=db, post=post, user_id=user_id)

@router.get("/users/{user_id}/posts/", response_model=List[schemas.Post])
def read_user_posts(user_id: int, db: Session = Depends(database.get_db)):
    posts = crud.get_posts_by_user(db, user_id=user_id)
    if posts is None:
        raise HTTPException(status_code=404, detail="Posts not found")
    return posts


