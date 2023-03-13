from src.domain.discipline import Discipline
from src.domain.validator_exception import ValidatorException
import nbformat
MINIMUM_ID = 0
MINIMUM_LENGTH = 1
class DisciplineService:
    def __init__(self, repository):
        self.__repository = repository
        self.__repository.add(Discipline(1, "Maths"))
        self.__repository.add(Discipline(2, "Geography"))
        self.__repository.add(Discipline(3, "Spanish"))

    def add_discipline(self, id, name):
        if id < MINIMUM_ID or len(name) < MINIMUM_LENGTH:
            raise ValidatorException("Validation failed")
        new_discipline = Discipline(id, name)
        self.__repository.add(new_discipline)

    def delete_discipline(self, discipline_id):
        if discipline_id < MINIMUM_ID:
            raise ValidatorException("Validation failed")
        self.__repository.remove(discipline_id)

    def update_discipline(self, discipline_id, new_name):
        if discipline_id < MINIMUM_ID:
            raise ValidatorException("Validation failed")
        if len(new_name) < MINIMUM_LENGTH:
            raise ValidatorException("Validation failed")
        self.__repository.update(discipline_id, new_name)

    def find_by_id(self, discipline_id):
        if discipline_id < MINIMUM_ID:
            raise ValidatorException("Validation failed")
        return self.__repository.find_by_id(discipline_id)

    def get_all(self):
        return self.__repository.get_all()