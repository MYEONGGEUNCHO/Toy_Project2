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
):
    result = leverage_crud.leverage(
        form.capital, form.debt, form.interest_rate
    )
    return result