class FailDTO:
    def __init__(self, student_name, discipline_name):
        self.__student_name = student_name
        self.__discipline_name = discipline_name

    def __str__(self):
        return self.__student_name + "," + self.__discipline_name

