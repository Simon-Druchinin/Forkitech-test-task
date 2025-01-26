from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class PaginationQueryParams(BaseModel):
    limit: int = 100
    offset: int = 0


class TronAddressInfoSchema(BaseModel):
    address: str
    balance: int | Decimal
    bandwidth: int | Decimal
    energy: int


class TronAddressInfoHistorySchema(BaseModel):
    id: int
    created_at: datetime
    address: str
    balance: int | Decimal
    bandwidth: int | Decimal
    energy: int
