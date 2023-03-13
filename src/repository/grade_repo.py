from src.repository.repository_exception import RepositoryException


class GradeRepository:
    def __init__(self, student_repo, discipline_repo):
        self._grades = []
        self.__student_repo = student_repo
        self.__discipline_repo = discipline_repo

    def add(self, new_grade):
        if self.__discipline_repo.find_by_id(new_grade.discipline_id) is None:
            raise RepositoryException("Discipline id not found in repo")
        if self.__student_repo.find_by_id(new_grade.student_id) is None:
            raise RepositoryException("Student id not found in repo")
        self._grades.append(new_grade)

    def delete_by_student_id(self, student_id):
        new_list = []
        for grade in self._grades:
            if grade.student_id != student_id:
                new_list.append(grade)
        self._grades.clear()
        self._grades.extend(new_list)

    def delete_by_discipline_id(self, discipline_id):
        new_list = []
        for grade in self._grades:
            if grade.discipline_id != discipline_id:
                new_list.append(grade)
        self._grades.clear()
        self._grades.extend(new_list)

    def find_by_student_id(self, student_id):
        for grade in self._grades:
            if grade.student_id == student_id:
                return grade
        return None

    def find_by_discipline_id(self, discipline_id):
        for grade in self._grades:
            if grade.discipline_id == discipline_id:
                return grade
        return None

    def get_all(self):
        return self._grades