from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, Float, DateTime, create_engine

Base = declarative_base
engine = create_engine("sqlite:///db/budget_tracker.db")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer(), primary_key = True)
    amount = Column(Float(), nullable = False)
    description = (String())
    timestamp = Column(DateTime, default = DateTime.now())
    category_id = Column(Integer(), ForeignKet(''))

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    

