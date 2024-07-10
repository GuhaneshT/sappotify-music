from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import  Session


from pydantic import BaseModel
from database import sessionLocal,engine 
import models
from fastapi.middleware.cors import CORSMiddleware



from datetime import datetime, timedelta
from typing import Annotated, List


app=FastAPI()

origins=[
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)


class UserBase(BaseModel):
    
    user_name : str
    username : str
    password : str
class UserModel(UserBase):
    user_id:int
    class Config:
        orm_mode=True
        
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependancy=Annotated[Session, Depends(get_db)]
models.base.metadata.create_all(bind=engine)
@app.post("/users/",response_model=UserModel)

async def create_user(user:UserBase,db:db_dependancy):
    db_user=models.Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
@app.get("/users/",response_model=List[UserModel])

async def get_user(db:db_dependancy,skip:int=0,limit:int=100):
    user=db.query(models.Users).offset(skip).limit(limit).all()
    return user
    
# class SongBase(BaseModel):
    
#     song_name = str
#     artist_name = str
#     album_cover = str
# class LikesBase(BaseModel):
    
#     user_id = int
#     song_id = int
    