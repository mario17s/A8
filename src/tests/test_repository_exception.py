import unittest

from src.repository.repository_exception import RepositoryException


class TestRepositoryException(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_repo(self):
        repo = RepositoryException("Hi")
        self.assertEqual(repo.get_message(), "Hi")
        self.assertEqual(repo.__str__(), "Hi")