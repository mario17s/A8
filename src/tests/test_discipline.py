import unittest

from src.domain.discipline import Discipline


class TestDiscipline(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_discipline(self):
        discipline = Discipline(1, "Maths")
        self.assertEqual(discipline.id, 1)
        self.assertEqual(discipline.name, "Maths")
        discipline.id = 2
        self.assertEqual(discipline.id, 2)
        discipline.name = "Spanish"
        self.assertEqual(discipline.name, "Spanish")
        self.assertEqual(discipline.__str__(), "2->Spanish")