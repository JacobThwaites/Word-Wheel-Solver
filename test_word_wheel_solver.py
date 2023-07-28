import unittest
from word_wheel_solver import WordWheelSolver
from corpus_adder import CorpusAdder

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

    # def test_can_get_solution_for_word_wheel_from_corpus(self):
    #     word_wheel_solver = WordWheelSolver()
    #     corpus_adder = CorpusAdder()
    #     dictionary = [('abcd','NN'), ('bcde','NN'), ('z','NN')]
    #     corpus_adder.add_corpus_to_solver(dictionary, word_wheel_solver)
    #     solution = word_wheel_solver.solve('b', ['a', 'c', 'd', 'e'])

    #     self.assertEqual(2, len(solution))
    #     self.assertIn('abcd', solution)
    #     self.assertIn('bcde', solution)

if __name__ == '__main__':
    unittest.main()