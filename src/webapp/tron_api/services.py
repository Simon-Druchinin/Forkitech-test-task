from tronpy import Tron

from .schemas import TronAddressInfo


class TronService:
    def __init__(self, client: Tron | None = None) -> None:
        self._client = client or Tron()

    def get_address_info(self, address: str) -> TronAddressInfo:
        return TronAddressInfo(
            balance=self._client.get_bandwidth(address),
            bandwidth=self._client.get_account_balance(address),
            energy=self.get_energy(address),
        )

    def get_energy(self, address: str) -> int:
        return self._client.get_account(address)["account_resource"]["energy_window_size"]


def get_tron_service() -> TronService:
    return TronService()
