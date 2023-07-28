import unittest
from corpus_adder import CorpusAdder
import os

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
    
    # def test_only_adds_words_not_in_excluded_tags(self):
    #     excluded_tags = ['a', 'b']
    #     corpus_adder = CorpusAdder(excluded_tags)

    #     test_corpus = [('test','nn'), ('should_not_appear','a'), ('also_should_not_appear','b')]
    #     corpus_adder.write_unique_words_to_file(self.file_path, test_corpus)

    #     self.assertTrue(os.path.exists(self.file_path))

    #     with open(self.file_path, "r") as file:
    #         line_count = sum(1 for _ in file)
    #         self.assertEqual(line_count, 1)

    #         first_line = file.readline().strip()
    #         self.assertEqual(first_line, ('test','nn'))

    def test_can_add_valid_unique_words_from_corpus_to_solver(self):
        excluded_tags = ['a', 'b']
        corpus_adder = CorpusAdder(excluded_tags)
        test_corpus = [('test','nn'), ('should_not_appear','a'), ('also_should_not_appear','b')]
        valid_unique_words = corpus_adder.get_valid_unique_words(test_corpus)

if __name__ == '__main__':
    unittest.main()