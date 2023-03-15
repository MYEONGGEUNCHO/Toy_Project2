from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from typing import List, Dict, Any, Optional

from domain.engine.leverage import leverage_crud, leverage_schema
from domain.user.user_router import get_current_user

router = APIRouter(
    prefix="/api/engine/leverage"
)

@router.post("/calculater")
def laverage_calculater(
    form: leverage_schema.Calculater
) -> Dict[Any, Dict[str, Any]]:
    """님들의 빚투 계산기

    Args:
        form (leverage_schema.Calculater): 입력값

    Returns:
        Dict[Any, Dict[str, Any]]: 결과값
    """
    result = leverage_crud.leverage(
        form.capital, form.debt, form.interest_rate
    )
    return result