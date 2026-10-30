import pytest
from fastapi.testclient import TestClient

from app.dependencies import get_student_repository
from app.main import app
from app.repositories import StudentRepository


@pytest.fixture
def client():
    repository = StudentRepository()
    app.dependency_overrides[get_student_repository] = lambda: repository
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
