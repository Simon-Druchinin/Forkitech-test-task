from pydantic import BaseModel


class TronAddressInfo(BaseModel):
    balance: int
    bandwidth: int
    energy: int
