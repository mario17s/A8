from src.domain.student import Student
from src.domain.validator_exception import ValidatorException
MINIMUM_ID = 0
MINIMUM_LENGTH = 1

class StudentService:
    def __init__(self, repository):
        self.__repository = repository
        self.__repository.add(Student(1, "Mihai"))
        self.__repository.add(Student(2, "Laura"))
        self.__repository.add(Student(3, "Mario"))

    def add_student(self, id, name):
        if id < MINIMUM_ID or len(name) < MINIMUM_LENGTH:
            raise ValidatorException("Validation failed")
        new_student = Student(id, name)
        self.__repository.add(new_student)



    def delete_student(self, student_id):
        if student_id < MINIMUM_ID:
            raise ValidatorException("Validation failed")
        self.__repository.remove(student_id)

    def update_student(self, student_id, new_name):
        if student_id < MINIMUM_ID:
            raise ValidatorException("Validation failed")
        if len(new_name) < MINIMUM_LENGTH:
            raise ValidatorException("Validation failed")
        self.__repository.update(student_id, new_name)

    def find_by_id(self, student_id):
        if student_id < MINIMUM_ID:
            raise ValidatorException("Validation failed")
        return self.__repository.find_by_id(student_id)

    def get_all(self):
        return self.__repository.get_all()