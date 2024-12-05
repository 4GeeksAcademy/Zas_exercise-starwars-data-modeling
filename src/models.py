import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50),nullable=False)
    password = Column (String (50), nullable = False)
    subscription_date = Column (Date)
    favorites = relationship('Favorite',back_populates='users') 


class Planet (Base):
    __tablename__ = 'planets'

    id = Column (Integer, primary_key = True)
    planet_name = Column (String)
    population = Column (Integer)
    rotation = Column (String)
    orbital_period = Column (String)
    diameter = Column (String)
    gravity = Column (String)
    terrain = Column (String)
    surface = Column (String)
    climate = Column (String)
    favorites = relationship('Favorite',back_populates='planets')


class Character(Base):
    __tablename__ = 'characters'
    id = Column (Integer, primary_key = True)
    character_name = Column (String)
    birth_year = Column (Date) 
    species = Column (String)
    height = Column (String)
    mass = Column (String)
    gender = Column (String)
    hair_color = Column (String)
    skin_color = Column (String) 
    homeworld = Column (Integer, ForeignKey(Planet.id)) 
    favorites = relationship('favorites',back_populates='characters')
    planet = relationship ('planets', back_populates='characters')


class Vehicle (Base):
    __tablename__ = 'vehicles'    
    id = Column (Integer, primary_key = True)
    model = Column (String)
    vehicle_class = Column (String)
    manufacturer = Column (String)
    cost_in_credits = Column (String)
    cargo_capacity = Column (String)
    max_atmosphering_speed = Column (String)
    owner = Column (String, ForeignKey(Character.id))
    favorites = relationship('favorites',back_populates='vehicles')

    
    



class Favorite(Base):
    __tablename__ = 'favorites'
    favorite_id = Column (Integer, primary_key = True) 
    user_id = Column(Integer, ForeignKey(User.id))
    character_id = Column(Integer, ForeignKey(Character.id))
    planet_id = Column(Integer,ForeignKey(Planet.id))

    user = relationship("users", back_populates="favorites")
    character = relationship("characters", back_populates="favorites")
    planet = relationship("planets", back_populates="favorites")
    vehicle = relationship("vehicles", back_populates="favorites")
    

    def to_dict(self):
        return {}

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
