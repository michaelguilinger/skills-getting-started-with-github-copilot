from src.app import activities


def test_get_activities_returns_seeded_activities(client):
    # Arrange
    expected_activity_name = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert expected_activity_name in payload
    assert payload[expected_activity_name]["participants"] == activities[expected_activity_name]["participants"]


def test_get_activities_returns_activity_details(client):
    # Arrange
    activity_name = "Programming Class"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert payload[activity_name]["description"] == activities[activity_name]["description"]
    assert payload[activity_name]["schedule"] == activities[activity_name]["schedule"]
    assert payload[activity_name]["max_participants"] == activities[activity_name]["max_participants"]