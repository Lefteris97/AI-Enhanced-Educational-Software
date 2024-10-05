from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

class PerformanceScore(Base):
    __tablename__ = 'performance'
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    score = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    # Establish relationship with User model
    user = relationship('User', back_populates='performance_scores')

# Relationship setup in User
User.performance_scores = relationship('PerformanceScore', order_by=PerformanceScore.date, back_populates='user')