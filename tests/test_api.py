import unittest

from fastapi.testclient import TestClient

from database import SessionLocal
from main import app
from models import Task


class TaskApiTests(unittest.TestCase):
    def test_create_task_success(self):
        db = SessionLocal()
        db.query(Task).delete()
        db.commit()
        db.close()

        client = TestClient(app)
        response = client.post("/tasks", json={"title": "Test task"})

        self.assertEqual(response.status_code, 201)
        body = response.json()
        self.assertEqual(body["title"], "Test task")
        self.assertIsNotNone(body["id"])


if __name__ == "__main__":
    unittest.main()
