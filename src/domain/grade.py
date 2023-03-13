from src.domain.validator_exception import ValidatorException


class Grade:
    def __init__(self, discipline_id, student_id, value):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__value = value

    @property
    def discipline_id(self):
        return self.__discipline_id

    @discipline_id.setter
    def discipline_id(self, value):
        self.__discipline_id = value

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return str(self.__discipline_id) + "," + str(self.__student_id) + "->" + str(self.__value)
