"""Unit tests for counter API routes."""
from unittest import TestCase
from service import app
from service.routes import reset_counters


class TestCounterAPI(TestCase):
    """Test the API's main success and error paths."""

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        reset_counters()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Counter REST API")

    def test_health(self):
        self.assertEqual(self.client.get("/health").status_code, 200)

    def test_create_list_read_update_delete(self):
        response = self.client.post("/counters/demo")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"name": "demo", "counter": 0})
        self.assertEqual(self.client.get("/counters").get_json(), [{"name": "demo", "counter": 0}])
        self.assertEqual(self.client.get("/counters/demo").get_json()["counter"], 0)
        self.assertEqual(self.client.put("/counters/demo").get_json()["counter"], 1)
        self.assertEqual(self.client.delete("/counters/demo").status_code, 204)
        self.assertEqual(self.client.get("/counters/demo").status_code, 404)

    def test_duplicate_create_conflicts(self):
        self.assertEqual(self.client.post("/counters/demo").status_code, 201)
        self.assertEqual(self.client.post("/counters/demo").status_code, 409)

    def test_update_missing_counter_is_not_found(self):
        self.assertEqual(self.client.put("/counters/missing").status_code, 404)

    def test_delete_missing_counter_is_idempotent(self):
        self.assertEqual(self.client.delete("/counters/missing").status_code, 204)
