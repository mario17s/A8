import unittest

from src.domain.discipline import Discipline
from src.domain.grade import Grade
from src.domain.student import Student
from src.repository.general_repo import Repository
from src.repository.grade_repo import GradeRepository
from src.repository.repository_exception import RepositoryException


class TestGradeRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.student_repo = Repository()
        self.discipline_repo = Repository()
        self.__repository = GradeRepository(self.student_repo, self.discipline_repo)

    def tearDown(self) -> None:
        pass

    def test_repo(self):
        new_grade = Grade(1,1,7)
        try:
            self.__repository.add(new_grade)
        except RepositoryException as re:
            self.assertEqual(re.get_message(), "Discipline id not found in repo")
        self.student_repo.add(Student(1, "Mirel"))
        self.discipline_repo.add(Discipline(1, "Spanish"))
        self.__repository.add(Grade(1, 1, 4))

        try:
            self.__repository.add(Grade(1, 2, 3))
        except RepositoryException as re:
            self.assertEqual(re.get_message(), "Student id not found in repo")

        self.student_repo.add(Student(2, "Gigel"))
        self.discipline_repo.add(Discipline(2, "Maths"))
        self.__repository.add(Grade(2, 2, 4))

        self.__repository.delete_by_student_id(1)
        self.assertEqual(self.__repository.find_by_student_id(1), None)

        self.__repository.add(Grade(1, 2, 4))
        self.__repository.delete_by_discipline_id(2)
        self.assertEqual(self.__repository.find_by_discipline_id(2), None)

        self.assertEqual(self.__repository.find_by_student_id(2).value, 4)
        self.assertEqual(self.__repository.find_by_discipline_id(1).value, 4)
        self.__repository.delete_by_discipline_id(1)
        self.assertEqual(self.__repository.get_all(), [])
