from app.repositories import StudentRepository

student_repository = StudentRepository()


def get_student_repository() -> StudentRepository:
    return student_repository
