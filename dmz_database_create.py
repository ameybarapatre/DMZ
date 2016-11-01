import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class services_dmz(Base):
    __tablename__ = 'services_dmz'
    service_id = Column(Integer, primary_key=True)
    service_name = Column(String(250))
    service_port = Column(Integer,nullable=False)
    service_protocol = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users_dmz.user_id'))
    users=relationship("users_dmz",back_populates="services")

class users_dmz(Base):
    __tablename__ = 'users_dmz'
    user_grp = Column(Integer ,nullable=True)
    user_pass = Column(String(250) , nullable=False)
    user_name = Column(String(250), nullable=False)
    user_id = Column(Integer , nullable=False , primary_key=True)
    services  = relationship("services_dmz ",back_populates="users" )


engine = create_engine('sqlite:///dmz_database_version-1.0.db')


Base.metadata.create_all(engine)