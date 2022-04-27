import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    post_author_id = Column(Integer, ForeignKey("user.id"))
    post_author = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    comment_author_id = Column(Integer, ForeignKey("user.id"))
    comment_author = relationship(User)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'
    
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey("user.id"))
    following_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

# ¿que es el BASE?
# nullable=false -> es que es un campo que no puede dejarse vacio
# Relationship hace referencia a la tabla a la que nos vamos a conectar

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
