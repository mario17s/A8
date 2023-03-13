import unittest

from src.domain.best_dto import BestDTO


class TestBestDTO(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_best_dto(self):
        failing_student = BestDTO("Mary", 9.5)
        self.assertEqual(failing_student.__str__(), "Mary,9.5")