import unittest

from src.domain.grade import Grade


class TestGrade(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_grade(self):
        grade = Grade(1, 2, 10)
        self.assertEqual(grade.discipline_id, 1)
        self.assertEqual(grade.student_id, 2)
        self.assertEqual(grade.value, 10)
        grade.discipline_id = 2
        self.assertEqual(grade.discipline_id, 2)
        grade.student_id = 3
        self.assertEqual(grade.student_id, 3)
        grade.value = 6
        self.assertEqual(grade.value, 6)
        self.assertEqual(grade.__str__(), "2,3->6")