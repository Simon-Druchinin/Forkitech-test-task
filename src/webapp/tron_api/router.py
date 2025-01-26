from asyncio import to_thread
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database import get_async_session

from .schemas import PaginationQueryParams, TronAddressInfoHistorySchema, TronAddressInfoSchema
from .services import TronService, add_address_info_to_history, get_paginated_history, get_tron_service

router = APIRouter(prefix="/tron_api", tags=["Tron API"])


@router.get("/address_info")
async def get_address_info(
    address: str,
    tron_service: Annotated[TronService, Depends(get_tron_service)],
    session: AsyncSession = Depends(get_async_session),
) -> TronAddressInfoSchema:
    address_info = await to_thread(tron_service.get_address_info(address))
    await add_address_info_to_history(address_info, session)
    return address_info


@router.get("/history")
async def get_requests_history(
    pagination_query_params: PaginationQueryParams = Depends(),
    session: AsyncSession = Depends(get_async_session),
) -> list[TronAddressInfoHistorySchema]:
    return await get_paginated_history(pagination_query_params, session)
