from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.dependencies import get_student_repository
from app.models import Student, StudentCreate
from app.repositories import StudentRepository

router = APIRouter(prefix="/students", tags=["students"])

StudentRepositoryDependency = Annotated[
    StudentRepository, Depends(get_student_repository)
]


@router.post(
    "",
    response_model=Student,
    status_code=status.HTTP_201_CREATED,
    summary="Add a student",
)
def add_student(
    student_data: StudentCreate,
    repository: StudentRepositoryDependency,
) -> Student:
    return repository.add(student_data)


@router.get("", response_model=list[Student], summary="View all students")
def view_students(repository: StudentRepositoryDependency) -> list[Student]:
    return repository.get_all()


@router.get(
    "/{student_id}",
    response_model=Student,
    summary="View a student by ID",
)
def view_student(
    student_id: int,
    repository: StudentRepositoryDependency,
) -> Student:
    student = repository.get_by_id(student_id)
    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    return student


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a student",
)
def delete_student(
    student_id: int,
    repository: StudentRepositoryDependency,
) -> Response:
    if not repository.delete(student_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
