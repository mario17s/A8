import unittest

from src.domain.validator_exception import ValidatorException
from src.repository.general_repo import Repository
from src.services.discipline_service import DisciplineService


class TestDisciplineService(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repository()
        self.__service = DisciplineService(self.repo)

    def tearDown(self) -> None:
        pass

    def test_service(self):
        self.__service.add_discipline(4, "Spanish")
        self.assertEqual(self.repo.find_by_id(4).name, "Spanish")

        try:
            self.__service.add_discipline(-3, "Maths")
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        self.__service.delete_discipline(4)
        self.assertEqual(self.repo.find_by_id(4), None)

        try:
            self.__service.delete_discipline(-3)
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        self.__service.update_discipline(3, "French")
        self.assertEqual(self.repo.find_by_id(3).name, "French")

        try:
            self.__service.update_discipline(-3, "French")
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        try:
            self.__service.update_discipline(4, "")
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")


        self.assertEqual(self.__service.find_by_id(3).name, "French")
        try:
            el = self.__service.find_by_id(-3)
        except ValidatorException as ve:
            self.assertEqual(ve.get_message(), "Validation failed")

        self.__service.delete_discipline(3)
        self.__service.delete_discipline(2)
        self.__service.delete_discipline(1)
        self.assertEqual(self.__service.get_all(), [])
