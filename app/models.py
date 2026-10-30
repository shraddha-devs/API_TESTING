from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0)


class Student(StudentCreate):
    id: int
