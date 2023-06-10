from typing import Optional

from datetime import date
from pydantic import BaseModel


class SalaryBase(BaseModel):
    amount: Optional[int] = None
    update: Optional[date] = None


class SalaryCreate(SalaryBase):
    amount: int
    update: date
    user_id: int


class SalaryUpdate(SalaryBase):
    user_id: int


class SalaryInDBBase(SalaryBase):
    user_id: int = None

    class Config:
        orm_mode = True


class Salary(SalaryInDBBase):
    pass
