import unittest

from src.domain.fail_dto import FailDTO


class TestFailDTO(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_fail_dto(self):
        failing_student = FailDTO("Mary", "Maths")
        self.assertEqual(failing_student.__str__(), "Mary,Maths")