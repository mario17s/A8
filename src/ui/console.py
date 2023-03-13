from src.domain.best_dto import BestDTO
from src.domain.discipline_dto import DisciplineDTO
from src.domain.fail_dto import FailDTO
from src.domain.validator_exception import ValidatorException
from src.repository.repository_exception import RepositoryException


class Console:
    def __init__(self, student_service, discipline_service, grade_service):
        self.__student_service = student_service
        self.__discipline_service = discipline_service
        self.__grade_servive = grade_service

    def add_student(self):
        id = input("give the id ")
        name = input("give the name ")
        try:
            id = int(id)
            self.__student_service.add_student(id, name)
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def remove_student(self):
        id = input("give the id ")
        try:
            id = int(id)
            self.__student_service.delete_student(id)
            if self.__grade_servive.find_by_student_id(id) is not None:
                self.__grade_servive.delete_by_student_id(id)
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def update_student(self):
        id = input("give the id ")
        new_name = input("give the new name ")
        try:
            id = int(id)
            self.__student_service.update_student(id, new_name)
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def display_students(self):
        all_students = self.__student_service.get_all()
        for student in all_students:
            print(student)

    def add_discipline(self):
        id = input("give the id ")
        name = input("give the name ")
        try:
            id = int(id)
            self.__discipline_service.add_discipline(id, name)
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def remove_discipline(self):
        id = input("give the id ")
        try:
            id = int(id)
            self.__discipline_service.delete_discipline(id)
            if self.__grade_servive.find_by_discipline_id(id) is not None:
                self.__grade_servive.delete_by_discipline_id(id)
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def update_discipline(self):
        id = input("give the id ")
        new_name = input("give the new name ")
        try:
            id = int(id)
            self.__discipline_service.update_discipline(id, new_name)
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def display_disciplines(self):
        all_disciplines = self.__discipline_service.get_all()
        for discipline in all_disciplines:
            print(discipline)

    def add_grade(self):
        discipline_id = input("give the discipline id ")
        student_id = input("give the student id ")
        value = input("enter the grade ")
        try:
            discipline_id = int(discipline_id)
            student_id = int(student_id)
            value = int(value)
            self.__grade_servive.add(discipline_id, student_id, value)
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def display_grades(self):
        all_grades = self.__grade_servive.get_all()
        for grade in all_grades:
            print(grade)

    def search_by_student_id(self):
        id = input("give the id ")
        try:
            id = int(id)
            print(self.__student_service.find_by_id(id))
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def search_by_discipline_id(self):
        id = input("give the id ")
        try:
            id = int(id)
            print(self.__discipline_service.find_by_id(id))
        except ValueError as ve:
            print(ve)
        except ValidatorException as v:
            print(v)
        except RepositoryException as re:
            print(re)

    def print_failing_students(self):
        new_list = []
        for student in self.__student_service.get_all():
            for discipline in self.__discipline_service.get_all():
                sum = 0
                number_of_grades = 0
                for grade in self.__grade_servive.get_all():
                    if grade.student_id == student.id and grade.discipline_id == discipline.id:
                        sum += grade.value
                        number_of_grades += 1
                if number_of_grades > 0:
                    if float(sum / number_of_grades) < 4.5:
                        failing_student = FailDTO(student.name, discipline.name)
                        new_list.append(failing_student)
        for data_transfer_object in new_list:
            print(data_transfer_object)

    def print_best_students(self):
        new_list = []
        for student in self.__student_service.get_all():
            average = 0
            number_of_disciplines = 0
            for discipline in self.__discipline_service.get_all():
                sum = 0
                number_of_grades = 0
                for grade in self.__grade_servive.get_all():
                    if grade.student_id == student.id and grade.discipline_id == discipline.id:
                        sum += grade.value
                        number_of_grades += 1
                if number_of_grades > 0:
                    average += (float)(sum / number_of_grades)
                    number_of_disciplines += 1
            average = (float)(average / number_of_disciplines)
            best_student = BestDTO(student.name, average)
            new_list.append(best_student)
        new_list = sorted(new_list, key= lambda a: a.average, reverse = True)
        for data_transfer_object in new_list:
            print(data_transfer_object)


    def print_disciplines_with_at_least_one_grade(self):
        new_list = []
        for discipline in self.__discipline_service.get_all():
            sum = 0
            number_of_grades = 0
            for grade in self.__grade_servive.get_all():
                if grade.discipline_id == discipline.id:
                    sum += grade.value
                    number_of_grades += 1
            if number_of_grades > 0:
                average = (float)(sum / number_of_grades)
                new_discipline = DisciplineDTO(discipline.name, average)
                new_list.append(new_discipline)
        new_list = sorted(new_list, key= lambda a: a.average, reverse = True)
        for data_transfer_object in new_list:
            print(data_transfer_object)


    def print_options(self):
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Update a student")
        print("4. Display students")
        print("5. Add a discipline")
        print("6. Remove a discipline")
        print("7. Update a discipline")
        print("8. Display disciplines")
        print("9. Grade student at a discipline")
        print("10. Display grades")
        print("11. Search by student id")
        print("12. Search by discipline id")
        print("13. Print failing students")
        print("14. Print best students")
        print("15. Print disciplines' averages")
        print("16. Exit")

    def run_console(self):
        while True:
            self.print_options()
            option = int(input("enter an option "))
            if option == 1: #1. Add a student
                self.add_student()
            if option == 2: #2. Remove a student
                self.remove_student()
            if option == 3: #3. Update a student
                self.update_student()
            if option == 4: #4. Display students
                self.display_students()
            if option == 5: #5. Add a discipline
                self.add_discipline()
            if option == 6: #6. Remove a discipline
                self.remove_discipline()
            if option == 7: #7. Update a discipline
                self.update_discipline()
            if option == 8: #8. Display disciplines
                self.display_disciplines()
            if option == 9: #9. Grade student at a discipline
                self.add_grade()
            if option == 10: #10. Display grades
                self.display_grades()
            if option == 11: #11. Search by student id
                self.search_by_student_id()
            if option == 12: #12. Search by discipline id
                self.search_by_discipline_id()
            if option == 13: #13. Print failing students
                self.print_failing_students()
            if option == 14: #14. Print best students
                self.print_best_students()
            if option == 15: #15. Print disciplines' averages
                self.print_disciplines_with_at_least_one_grade()
            if option == 16: #16. Exit
                break