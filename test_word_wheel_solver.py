import unittest
from word_wheel_solver import WordWheelSolver

class TestWordWheelSolver(unittest.TestCase):
    def test_starts_with_an_empty_dictionary_of_words(self):
        word_wheel_solver = WordWheelSolver()
        dictionary = word_wheel_solver.get_words_in_dictionary()
        self.assertEqual(0, len(dictionary))
    
    def test_can_add_a_word_to_dictionary(self):
        word_wheel_solver = WordWheelSolver()
        word = 'asdf'
        word_wheel_solver.add_word_to_dictionary(word)
        dictionary = word_wheel_solver.get_words_in_dictionary()
        self.assertEqual(1, len(dictionary))
        self.assertEqual(word, dictionary[0])

if __name__ == '__main__':
    unittest.main()