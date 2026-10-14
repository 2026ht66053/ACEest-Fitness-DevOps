import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to ACEest Fitness & Gym" in response.get_json()["message"]


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_programs(client):
    response = client.get("/programs")
    assert response.status_code == 200
    assert len(response.get_json()["programs"]) == 3


def test_calculate_calories(client):
    response = client.post(
        "/calculate-calories",
        json={"weight_kg": 70, "duration_minutes": 30, "met": 5},
    )
    assert response.status_code == 200
    assert response.get_json()["calories_burned"] == 183.75


def test_calculate_calories_invalid_data(client):
    response = client.post("/calculate-calories", json={})
    assert response.status_code == 400


def test_calculate_calories_zero_values(client):
    response = client.post(
        "/calculate-calories",
        json={"weight_kg": 70, "duration_minutes": 0, "met": 5},
    )
    assert response.status_code == 400


def test_unknown_route(client):
    response = client.get("/unknown")
    assert response.status_code == 404
