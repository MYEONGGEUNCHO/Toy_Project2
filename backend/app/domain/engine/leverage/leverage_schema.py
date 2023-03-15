import datetime
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel, validator

class Calculater(BaseModel):
    capital: Union[int, float] = 600
    debt: Union[int, float] = 1000
    interest_rate: float = 0.06
    
    @validator('capital', 'debt', 'interest_rate')
    def not_empty(cls, v):
        if not v:
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class Leverage(BaseModel):
    revenue_rate: Union[int, float]
    revenue: Union[int, float]
    cost: Union[int, float]
    profit: Union[int, float]
    profit_rate: Union[int, float]
