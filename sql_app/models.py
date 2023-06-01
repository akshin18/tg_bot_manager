from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Bots(Base):
    __tablename__ = "bots"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True)
    name = Column(String,default="Name")


    # items = relationship("Item", back_populates="owner")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    bot = Column(Integer, ForeignKey("bots.id"))

    # owner = relationship("User", back_populates="items")
