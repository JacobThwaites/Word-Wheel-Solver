import unittest
from word_validator import WordValidator

class TestWordWheelSolver(unittest.TestCase):
    def test_returns_false_if_word_does_not_contain_hub_letter(self):
        word_validator = WordValidator('a')
        is_word_valid = word_validator.is_word_valid('bcde')
        self.assertFalse(is_word_valid)
        pass

    def test_returns_false_if_word_has_fewer_than_four_characters(self):
        word_validator = WordValidator('a')
        is_word_valid = word_validator.is_word_valid('abc')
        self.assertFalse(is_word_valid)
        pass

if __name__ == '__main__':
    unittest.main()