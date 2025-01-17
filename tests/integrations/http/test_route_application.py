from httpx import AsyncClient
from starlette import status


async def test_get_applications(client: AsyncClient) -> None:
    response = await client.get("/applications")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"total": 0, "applications": []}


async def test_scenarios_application(client: AsyncClient) -> None:
    new_application = {
        "user_name": "Maclovi",
        "description": "Some Description",
    }
    response = await client.post("/applications", json=new_application)
    assert response.status_code == status.HTTP_200_OK
    assert response.read() == b"1"

    response = await client.get("/applications")
    assert response.status_code == status.HTTP_200_OK
    expected_application = {"id": 1, **new_application}
    resp_json = response.json()
    del resp_json["applications"][-1]["created_at"]
    assert resp_json == {"total": 1, "applications": [expected_application]}

    response = await client.get("/applications", params={"size": 1001})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    wrong_new_application = {
        "user_name": "_Maclovi",
        "description": "Some Description",
    }
    response = await client.post("/applications", json=wrong_new_application)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
