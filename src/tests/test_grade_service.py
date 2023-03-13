import unittest

from src.domain.discipline import Discipline
from src.domain.student import Student
from src.domain.validator_exception import ValidatorException
from src.repository.general_repo import Repository
from src.repository.grade_repo import GradeRepository
from src.services.grade_service import GradeService


class TestGradeService(unittest.TestCase):
    def setUp(self) -> None:
        self.student_repo = Repository()
        self.discipline_repo = Repository()
        self.student_repo.add(Student(1, "Mihai"))
        self.student_repo.add(Student(2, "Laura"))
        self.student_repo.add(Student(3, "Mario"))
        self.discipline_repo.add(Discipline(1, "Maths"))
        self.discipline_repo.add(Discipline(2, "Geography"))
        self.discipline_repo.add(Discipline(3, "Spanish"))
        self.repo = GradeRepository(self.student_repo, self.discipline_repo)
        self.__service = GradeService(self.repo)

    def tearDown(self) -> None:
        pass

    def test_service(self):
        self.__service.add(2, 2, 4)

        try:
            self.__service.add(2, 2, 11)
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "grade must be between 1 and 10")

        self.__service.delete_by_student_id(1)
        self.assertEqual(self.__service.find_by_student_id(1), None)

        self.__service.delete_by_discipline_id(2)
        self.assertEqual(self.__service.find_by_discipline_id(2), None)

        self.__service.delete_by_discipline_id(1)
        self.assertEqual(self.__service.get_all(), [])