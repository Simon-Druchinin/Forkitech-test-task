from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from config.database import Base

app_name = "tron_api"


class TronAddressInfo(Base):
    __tablename__ = f"{app_name}_tron_address_info"

    address: Mapped[str] = mapped_column(String)
    balance: Mapped[int] = mapped_column(Integer)
    bandwidth: Mapped[int] = mapped_column(Integer)
    energy: Mapped[int] = mapped_column(Integer)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}> id={self.id}"
