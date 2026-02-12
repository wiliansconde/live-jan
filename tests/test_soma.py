
def test_soma_cenario_1(client):
    response = client.get("/soma", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["resultado"] == 5

def test_soma_cenario_2(client):
    response = client.get("/soma", params={"a": 10, "b": 3})
    assert response.status_code == 200
    assert response.json()["resultado"] == 13
