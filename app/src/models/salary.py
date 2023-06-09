from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from src.db.base_class import Base


class SalaryInfo(Base):
    id = Column(Integer, primary_key=True, unique=True)
    amount = Column(Integer)
    update = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="salary")
