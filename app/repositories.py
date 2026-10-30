from app.models import Student, StudentCreate


class StudentRepository:
    """Stores students in memory for the lifetime of the application process."""

    def __init__(self) -> None:
        self._students: dict[int, Student] = {}
        self._next_id = 1

    def add(self, student_data: StudentCreate) -> Student:
        student = Student(id=self._next_id, **student_data.model_dump())
        self._students[student.id] = student
        self._next_id += 1
        return student

    def get_all(self) -> list[Student]:
        return list(self._students.values())

    def get_by_id(self, student_id: int) -> Student | None:
        return self._students.get(student_id)

    def delete(self, student_id: int) -> bool:
        return self._students.pop(student_id, None) is not None
