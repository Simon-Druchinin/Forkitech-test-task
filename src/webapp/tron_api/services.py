from pydantic import TypeAdapter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import Tron

from .models import TronAddressInfo
from .schemas import PaginationQueryParams, TronAddressInfoHistorySchema, TronAddressInfoSchema


class TronService:
    def __init__(self, client: Tron | None = None) -> None:
        self._client = client or Tron()

    def get_address_info(self, address: str) -> TronAddressInfoSchema:
        return TronAddressInfoSchema(
            address=address,
            balance=self._client.get_bandwidth(address),
            bandwidth=self._client.get_account_balance(address),
            energy=self.get_energy(address),
        )

    def get_energy(self, address: str) -> int:
        return self._client.get_account(address)["account_resource"]["energy_window_size"]


def get_tron_service() -> TronService:
    return TronService()


async def add_address_info_to_history(address_info: TronAddressInfoSchema, session: AsyncSession) -> None:
    new_address_info = TronAddressInfo(**address_info.model_dump())
    session.add(new_address_info)
    await session.commit()


async def get_paginated_history(
    pagination: PaginationQueryParams,
    session: AsyncSession,
) -> list[TronAddressInfoHistorySchema]:
    query = select(TronAddressInfo).limit(pagination.limit).offset(pagination.offset)
    result = await session.execute(query)
    return TypeAdapter(list[TronAddressInfoHistorySchema]).validate_python(result.scalars().all(), from_attributes=True)
