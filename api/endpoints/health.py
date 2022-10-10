from typing import Any

import schemas
from fastapi import APIRouter

router = APIRouter()


GET_HEALTH = {
    200: {
        "description": "API response successfully",
        "content": {"json": {"detail": "Service healthy"}},
    }
}


@router.get("/", response_model=schemas.Msg, status_code=200, responses=GET_HEALTH)
def get_health() -> Any:
    return schemas.Msg(detail="Service healthy")
