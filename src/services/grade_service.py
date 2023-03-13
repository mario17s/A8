from src.domain.grade import Grade
from src.domain.validator_exception import ValidatorException
MINIMUM_GRADE = 1
MAXIMUM_GRADE = 10

class GradeService():
    def __init__(self, repository):
        self.__repository = repository
        self.__repository.add(Grade(1, 1, 2))
        self.__repository.add(Grade(1, 1, 5))
        self.__repository.add(Grade(1, 2, 10))
        self.__repository.add(Grade(1, 2, 8))
        self.__repository.add(Grade(2, 2, 1))
        self.__repository.add(Grade(2, 2, 5))
        self.__repository.add(Grade(1, 3, 10))
        self.__repository.add(Grade(1, 3, 8))
        self.__repository.add(Grade(2, 3, 3))
        self.__repository.add(Grade(2, 3, 5))

    def add(self, discipline_id, student_id, grade):
        if grade < MINIMUM_GRADE or grade > MAXIMUM_GRADE:
            raise ValidatorException("grade must be between 1 and 10")
        new_grade = Grade(discipline_id, student_id, grade)
        self.__repository.add(new_grade)

    def delete_by_student_id(self, student_id):
        self.__repository.delete_by_student_id(student_id)

    def delete_by_discipline_id(self, discipline_id):
        self.__repository.delete_by_discipline_id(discipline_id)

    def find_by_student_id(self, student_id):
        return self.__repository.find_by_student_id(student_id)

    def find_by_discipline_id(self, discipline_id):
        return self.__repository.find_by_discipline_id(discipline_id)

    def get_all(self):
        return self.__repository.get_all()

    