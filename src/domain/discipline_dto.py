class DisciplineDTO:
    def __init__(self, discipline_name, average):
        self.__discipline_name = discipline_name
        self.average = average

    def __str__(self):
        return self.__discipline_name + "," + str(self.average)