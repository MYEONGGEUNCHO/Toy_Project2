from typing import List, Dict, Any, Optional, Union
from domain.engine.leverage.leverage_schema import Leverage

return_rate: List[Union[int, float]] = [
    -2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1
    , -1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1
    , 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1
    , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2
]

def leverage(
    capital: Union[int, float]
    , debt: Union[int, float]
    , interest_rate: Union[int, float]
) -> Dict[Union[int, float], Leverage]:
    asset = capital + debt
    leverage_ratio = debt/capital
    finance_leverage_ratio = asset/capital
    
    result = dict()
    for i in return_rate:
        unit = dict()
        revenue = i * asset
        cost = debt * interest_rate
        profit = revenue - cost
        profit_rate = ((i*finance_leverage_ratio)-(interest_rate*leverage_ratio))
        
        unit = {
            'revenue_rate': i
            , 'revenue': revenue
            , 'cost': cost
            , 'profit': profit
            , 'profit_rate': profit_rate
        }
        
        result[i] = unit
        
    return result