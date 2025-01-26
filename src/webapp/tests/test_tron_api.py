from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient


def test_get_address_info(client: TestClient) -> None:
    test_address = "TE2RzoSV3wFK99w6J9UnnZ4vLfXYoxvRwP"

    mock_tron_service = AsyncMock()
    mock_tron_service.get_address_info.return_value = {
        "address": test_address,
        "balance": 1000,
        "bandwidth": 500,
        "energy": 300,
    }

    mock_session = AsyncMock()

    with (
        patch("tron_api.services.get_tron_service", return_value=mock_tron_service),
        patch("main.get_async_session", return_value=mock_session),
    ):
        response = client.get("/tron_api/address_info", params={"address": test_address})

    assert response.status_code == 200

    data = response.json()
    assert data["address"] == test_address
    assert data["balance"] == 1000
    assert data["bandwidth"] == 500
    assert data["energy"] == 300
