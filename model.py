from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class product(Base):
  __tablename__ = 'products'
  id = Column(Integer, primary_key=True)
  Name = Column(String)
  Price = Column(Integer)
  Picture = Column(String)
  Description = Column(String)


class Cart(Base):
   __tablename__ = 'cart'
   id = Column(Integer, primary_key=True)
   cart_id = Column(Integer, primary_key=True)

