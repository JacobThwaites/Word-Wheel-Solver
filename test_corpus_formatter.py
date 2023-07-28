import unittest
from corpus_formatter import CorpusFormatter
import os

class TestCorpusFormatter(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_file.txt'
    
    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_can_write_unique_words_from_corpus_to_file(self):
        corpus_formatter = CorpusFormatter()

        test_corpus = [('test/nn')]
        corpus_formatter.write_unique_words_to_file(self.file_path, test_corpus)

        self.assertTrue(os.path.exists(self.file_path))

        with open(self.file_path, "r") as file:
            first_line = file.readline().strip()
            self.assertEqual(first_line, 'test/nn')

if __name__ == '__main__':
    unittest.main()