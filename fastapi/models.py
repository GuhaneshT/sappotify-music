from database import base
from sqlalchemy import Column,Integer,String,Float,Boolean


class Users(base):
    __tablename__='users'
    
    user_id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String)
    username = Column(String,unique=True)
    password = Column(String)
class Songs(base):
    __tablename__='songs'
    
    song_id = Column(Integer,primary_key=True,index=True)
    song_name = Column(String)
    artist_name = Column(String)
    album_cover = Column(String)
    
    
class Likes(base):
    __tablename__='likes'
    
    like_id=Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer)
    song_id = Column(Integer)
    