import datetime
from typing import List, Dict, Any, Optional, Union
from pydantic import BaseModel, validator

class Calculater(BaseModel):
    capital: Union[int, float]
    debt: Union[int, float]
    interest_rate: Union[int, float]
    
class Leverage(BaseModel):
    profit_rate: Union[int, float]
    profit: Union[int, float]
    interest: Union[int, float]
    total_profit: Union[int, float]
    total_profit_rate: Union[int, float]