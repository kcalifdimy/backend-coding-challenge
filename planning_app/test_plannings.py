from pickle import FALSE
from fastapi.testclient import TestClient
from fastapi import FastAPI
#from planning_app.main import app

#client = TestClient(app)




def test_get_single_planning(client):
    response = client.get("http://127.0.0.1:8000/planning/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
 



def test_get_all_plannings(client):
    response = client.get("http://127.0.0.1:8000/plannings?page=1&size=50")
    assert response.status_code == 200
    assert response.json()["size"] == 50

def test_get_search(client):
    pass