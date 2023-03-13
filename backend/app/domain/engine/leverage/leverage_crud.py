from typing import List, Dict, Any, Optional, Union

return_rate = [
    -2, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1
    , -1, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1
    , 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1
    , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2
]

def leverage(
    capital: int
    , debt: int
    , interest_rate: float
) -> Dict[int, Dict[str, Any]]:
    asset = capital + debt
    leverage_ratio = debt/capital
    finance_leverage_ratio = asset/capital
    
    result = dict()
    for i in return_rate:
        unit = dict()
        profit = i *asset
        interest = debt * interest_rate
        total_profit = profit - interest
        total_profit_rate = ((i*finance_leverage_ratio)-(interest_rate*leverage_ratio))
        
        unit = {
            'profit': profit
            , 'interest': interest
            , 'total_profit': total_profit
            , 'total_profit_rate': total_profit_rate
        }
        
        result[i] = unit
        
    return result