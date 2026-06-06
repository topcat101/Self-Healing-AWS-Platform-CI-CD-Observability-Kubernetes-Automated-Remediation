from django.test import TestCase
from django.urls import reverse


class StatusEndpointTests(TestCase):
    def test_home_endpoint_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "running")

    def test_health_endpoint_returns_200(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    def test_version_endpoint_returns_200(self):
        response = self.client.get("/version/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("version", response.json())