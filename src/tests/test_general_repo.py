import unittest

from src.domain.student import Student
from src.repository.general_repo import Repository
from src.repository.repository_exception import RepositoryException


class TestGeneralRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repository = Repository()

    def tearDown(self) -> None:
        pass

    def test_repo(self):
        new_student = Student(1, "Mihai")
        self.__repository.add(new_student)
        self.assertEqual(self.__repository.get_all(), [new_student])
        new_student = Student(1, "Maria")
        try:
            self.__repository.add(new_student)
        except RepositoryException as re:
            self.assertEqual(re.get_message(), "Duplicate id")
        new_student = Student(2, "Laura")
        self.__repository.add(new_student)
        self.__repository.remove(1)
        self.assertEqual(self.__repository.find_by_id(1), None)
        try:
            self.__repository.remove(1)
        except RepositoryException as re:
            self.assertEqual(re.get_message(), "Object not in Repository")

        self.__repository.update(2, "Lala")
        self.assertEqual(self.__repository.find_by_id(2).name, "Lala")

        try:
            self.__repository.update(3, "Magdalena")
        except RepositoryException as re:
            self.assertEqual(re.get_message(), "Object not in repository")

        self.assertEqual(self.__repository.__len__(), 1)