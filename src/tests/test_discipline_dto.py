import unittest

from src.domain.discipline_dto import DisciplineDTO


class TestDisciplineDTO(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_best_dto(self):
        failing_student = DisciplineDTO("Maths", 9.5)
        self.assertEqual(failing_student.__str__(), "Maths,9.5")