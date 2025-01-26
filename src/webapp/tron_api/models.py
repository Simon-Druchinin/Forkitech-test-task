from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from config.database import Base

app_name = "tron_api"


class TronAddressInfo(Base):
    __tablename__ = f"{app_name}_tron_address_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    address: Mapped[str] = mapped_column(String)
    balance: Mapped[int] = mapped_column(Integer)
    bandwidth: Mapped[int] = mapped_column(Integer)
    energy: Mapped[int] = mapped_column(Integer)

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}> id={self.id}"
