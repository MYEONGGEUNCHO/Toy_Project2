import datetime
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel, validator

class Calculater(BaseModel):
    capital: Union[int, float]
    debt: Union[int, float]
    interest_rate: float
    
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