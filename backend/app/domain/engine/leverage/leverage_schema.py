import datetime
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, validator

class Calculater(BaseModel):
    capital: int
    debt: int
    interest_rate: float
    
class Leverage(BaseModel):
    profit_rate: float
    profit: int
    interest: int
    total_profit: int
    total_profit_rate: float
    
# class LeverageDict(BaseModel):
#     leverage_Dict: Dict[int, Dict[str, Leverage]] = None