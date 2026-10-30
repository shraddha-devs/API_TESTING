# Student API

A backend-only REST API for adding, viewing, and deleting students. Student data
is held in memory and is cleared whenever the application restarts.

## Requirements

- Python 3.10 or newer
- pip

The Python packages required by the application and its tests are listed in
[`requirements.txt`](requirements.txt).

## Setup and run

Run these commands from the project root (`D:\TEST_API`):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

If PowerShell prevents virtual environment activation, run the commands below
in Command Prompt instead:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

The server runs at `http://127.0.0.1:8000`.

## API endpoints

Interactive API documentation is available in a web browser at
[`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs). The OpenAPI schema
is at [`http://127.0.0.1:8000/openapi.json`](http://127.0.0.1:8000/openapi.json).
The root URL [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) provides a
simple health response; use `/docs` to try the student endpoints in a browser.

| Method | URL | Purpose |
| --- | --- | --- |
| `POST` | `http://127.0.0.1:8000/students` | Add a student |
| `GET` | `http://127.0.0.1:8000/students` | View all students |
| `GET` | `http://127.0.0.1:8000/students/{student_id}` | View a student by ID |
| `DELETE` | `http://127.0.0.1:8000/students/{student_id}` | Delete a student |

Students have a `name` (1–100 characters) and a positive integer `age`. IDs
are assigned by the API. For example, in Postman select **POST**, enter
`http://127.0.0.1:8000/students`, choose **Body → raw → JSON**, and send:

```json
{
  "name": "Asha",
  "age": 20
}
```

The API responds with HTTP `201 Created` and the assigned ID:

```json
{
  "id": 1,
  "name": "Asha",
  "age": 20
}
```

Use the other URLs in the table with the corresponding HTTP method in Postman.
Missing student IDs return HTTP `404 Not Found`; invalid request data returns
HTTP `422 Unprocessable Entity`. A successful deletion returns HTTP `204 No
Content`.

## Run tests

From the project root, install the requirements if you have not already, then
run:

```powershell
python -m pytest
```
