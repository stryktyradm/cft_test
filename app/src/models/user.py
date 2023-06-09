from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True, unique=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    salary = relationship("SalaryInfo", uselist=False, back_populates="user")
