from .base import CRUDBase
from src.models.salary import SalaryInfo
from src.schemas.salary import SalaryCreate, SalaryUpdate

salary = CRUDBase[SalaryInfo, SalaryCreate, SalaryUpdate](SalaryInfo)
