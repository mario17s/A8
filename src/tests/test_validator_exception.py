import unittest

from src.domain.validator_exception import ValidatorException


class TestValidatorException(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_validator_exception(self):
        exception = ValidatorException("incorrect id")
        self.assertEqual(exception.get_message(), "incorrect id")
        self.assertEqual(exception.__str__(), "incorrect id")