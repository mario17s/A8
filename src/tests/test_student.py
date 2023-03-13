import unittest

from src.domain.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_student(self):
        student = Student(1, "Mario")
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "Mario")
        student.id = 2
        self.assertEqual(student.id, 2)
        student.name = "David"
        self.assertEqual(student.name, "David")
        self.assertEqual(student.__str__(), "2->David")