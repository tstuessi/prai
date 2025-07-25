from fastapi.testclient import TestClient

from prai.app import app

client = TestClient(app)


class TestRootEndpoint:
    """Tests for the root endpoint (/)."""

    def test_read_root(self):
        """Test the root endpoint returns welcome message."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello from PRAI!"}


class TestHealthEndpoint:
    """Tests for the health check endpoint (/health)."""

    def test_health_check(self):
        """Test the health check endpoint returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


class TestItemsEndpoint:
    """Tests for the items endpoint (/items/{item_id})."""

    def test_read_item(self):
        """Test the item endpoint with ID only."""
        response = client.get("/items/42")
        assert response.status_code == 200
        assert response.json() == {"item_id": 42, "q": None}

    def test_read_item_with_query(self):
        """Test the item endpoint with ID and query parameter."""
        response = client.get("/items/42?q=test")
        assert response.status_code == 200
        assert response.json() == {"item_id": 42, "q": "test"}

    def test_read_item_invalid_id(self):
        """Test the item endpoint with invalid ID type."""
        response = client.get("/items/not-a-number")
        assert response.status_code == 422  # Validation error
