import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    email = Column(String(250))
    password = Column(String(10))
    favorites = relationship("Favorite")

class Favorite (Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))

class Character (Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    homeworld = Column(String(100))
    vehicle = Column(String(100))
    planet = relationship("Planet")
    vehicle = relationship("Vehicle")

class Planet (Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    population = Column(Integer)
    character_id = Column (Integer, ForeignKey("characters.id"))

class Vehicle (Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    crew = Column(Integer)
    character_id = Column (Integer, ForeignKey("characters.id"))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')