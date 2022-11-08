import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    lastname = Column(String(100))
    age = Column(Integer)
    email = Column(String(200))
    favorite = relationship("Characters", backref="user")

class Favorite (Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    lastname = Column(String(100))
    gender = Column(String(100))
    homeworld = Column(String(100))
    vehicle = Column(String(100))
    planet = relationship("Planet")
    vehicle = relationship("Vehicle")
    favorites = Column(Integer, ForeignKey("favorites"), nullable=False)
         
class Planet (Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    population = Column(Integer)
    character_id = Column (Integer, ForeignKey("characters.id"))
    users_id_favorites = Column(Integer, ForeignKey("favorites"), nullable=False)
 

class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    model = Column(String(100))
    passengers = Column(Integer)
    description = Column(String(250))
    cargo_capacity = Column(Integer)
    character_id = Column (Integer, ForeignKey("characters.id"))
    favorites = Column(Integer, ForeignKey("favorites"), nullable=False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')