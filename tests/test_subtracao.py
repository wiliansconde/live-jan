def test_soma_cenario_1(client):
    response = client.get("/subtracao", params={"a": 10, "b": 3})
    assert response.status_code == 200
    assert response.json()["resultado"] == 7
