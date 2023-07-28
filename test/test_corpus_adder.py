import unittest
import os
from corpus_adder import CorpusAdder
from word_wheel_solver import WordWheelSolver

class TestCorpusAdder(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.txt'
    
    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_can_write_unique_words_from_corpus_to_file(self):
        corpus_adder = CorpusAdder()

        test_corpus = [('test','nn')]
        corpus_adder.write_unique_words_to_file(self.file_path, test_corpus)

        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, "r") as file:
            first_line = file.readline().strip()
            self.assertEqual(eval(first_line), ('test', 'nn'))

    def test_can_add_valid_unique_words_from_tagged_corpus_to_solver(self):
        excluded_tags = ['a', 'b']
        corpus_adder = CorpusAdder(excluded_tags)
        test_corpus = [('test','nn'), ('should_not_appear','a'), ('also_should_not_appear','b')]
        solver = WordWheelSolver()
        corpus_adder.add_tagged_corpus_to_solver(test_corpus, solver)

        dictionary = solver.get_words_in_dictionary()
        self.assertEqual(1, len(dictionary))
        self.assertEqual('test', dictionary[0])
    
    def test_can_add_unique_words_from_untagged_corpus_from_file_to_solver(self):
        corpus_adder = CorpusAdder()
        words = ['a', 'ab', 'a']
        with open(self.file_path, 'w') as file:
            for word in words:
                file.write(word + '\n')

        solver = WordWheelSolver()
        corpus_adder.add_corpus_from_file(self.file_path, solver)

        dictionary = solver.get_words_in_dictionary()
        self.assertEqual(2, len(dictionary))
        self.assertEqual('a', dictionary[0])
        self.assertEqual('ab', dictionary[1])

if __name__ == '__main__':
    unittest.main()