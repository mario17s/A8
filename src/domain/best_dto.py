class BestDTO:
    def __init__(self, student_name, average):
        self.__student_name = student_name
        self.average = average

    def __str__(self):
        return self.__student_name + "," + str(self.average)

