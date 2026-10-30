from fastapi.testclient import TestClient


def test_add_student(client: TestClient) -> None:
    response = client.post("/students", json={"name": "Asha", "age": 20})

    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Asha", "age": 20}


def test_view_all_students(client: TestClient) -> None:
    client.post("/students", json={"name": "Asha", "age": 20})
    client.post("/students", json={"name": "Ravi", "age": 21})

    response = client.get("/students")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Asha", "age": 20},
        {"id": 2, "name": "Ravi", "age": 21},
    ]


def test_view_student_by_id(client: TestClient) -> None:
    client.post("/students", json={"name": "Asha", "age": 20})

    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Asha", "age": 20}


def test_view_missing_student_returns_404(client: TestClient) -> None:
    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_delete_student(client: TestClient) -> None:
    client.post("/students", json={"name": "Asha", "age": 20})

    response = client.delete("/students/1")

    assert response.status_code == 204
    assert client.get("/students/1").status_code == 404


def test_delete_missing_student_returns_404(client: TestClient) -> None:
    response = client.delete("/students/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student not found"}


def test_add_student_validates_input(client: TestClient) -> None:
    response = client.post("/students", json={"name": "", "age": 0})

    assert response.status_code == 422
