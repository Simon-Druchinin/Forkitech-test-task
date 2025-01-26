from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_async_session

from .schemas import TronAddressInfo
from .services import TronService, get_tron_service

router = APIRouter(prefix="/tron_api", tags=["Tron API"])


@router.get("/address_info")
async def get_address_info(
    address: str,
    tron_service: Annotated[TronService, Depends(get_tron_service)],
    session: AsyncSession = Depends(get_async_session),
) -> TronAddressInfo:
    return tron_service.get_address_info(address)


@router.get("/history")
async def get_requests_history():
    return {}
