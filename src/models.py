import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url_img = Column(String(250))
    alive = Column(Boolean)

class Episodes(Base):
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lenght = Column(Integer)

class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(250))

class Characters_episodes(Base):
    __tablename__ = 'characters_episodes'
    id = Column(Integer, primary_key=True)
    id_character = Column(Integer, ForeignKey('characters.id'))
    id_episode = Column(Integer, ForeignKey('episodes.id'))
    character = relationship(Characters)
    episode = relationship(Episodes)

class Episodes_locations(Base):
    __tablename__ = 'episodes_locations'
    id = Column(Integer, primary_key=True)    
    id_episode = Column(Integer, ForeignKey('episodes.id'))
    id_location = Column(Integer, ForeignKey('locations.id'))
    episode = relationship(Episodes)
    location = relationship(Locations)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_character = Column(Integer,ForeignKey('characters.id'))
    id_episode = Column(Integer, ForeignKey('episodes.id'))
    id_location = Column(Integer, ForeignKey('locations.id'))
    user = relationship(User)
    character = relationship(Characters)
    episode = relationship(Episodes)
    location = relationship(Locations)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
