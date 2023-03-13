import unittest

from src.domain.validator_exception import ValidatorException
from src.repository.general_repo import Repository
from src.services.student_service import StudentService


class TestStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repository()
        self.__service = StudentService(self.repo)

    def tearDown(self) -> None:
        pass

    def test_service(self):
        self.__service.add_student(4, "Mihai")
        self.assertEqual(self.repo.find_by_id(4).name, "Mihai")

        try:
            self.__service.add_student(-3, "Gicu")
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        self.__service.delete_student(4)
        self.assertEqual(self.repo.find_by_id(4), None)

        try:
            self.__service.delete_student(-3)
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        self.__service.update_student(3, "Jery")
        self.assertEqual(self.repo.find_by_id(3).name, "Jery")

        try:
            self.__service.update_student(-3, "Jery")
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        try:
            self.__service.update_student(3, "")
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")


        self.assertEqual(self.__service.find_by_id(3).name, "Jery")
        try:
            el = self.__service.find_by_id(-3)
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        self.__service.delete_student(3)
        self.__service.delete_student(2)
        self.__service.delete_student(1)
        self.assertEqual(self.__service.get_all(), [])
