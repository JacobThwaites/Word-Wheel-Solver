import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def test_returns_false_if_does_not_have_word(self):
        trie = Trie()
        self.assertFalse(trie.has('a'))
    
    def test_returns_true_if_word_is_added(self):
        trie = Trie()
        trie.add('asd')
        self.assertTrue(trie.has('asd'))

    def test_returns_false_if_checking_proper_substring_of_word(self):
        trie = Trie()
        trie.add('asdf')
        self.assertFalse(trie.has('asd'))

    def test_can_return_list_of_all_words_added(self):
        trie = Trie()
        trie.add('ab')
        trie.add('a')
        trie.add('b')

        words_added = trie.get_all_words()
        self.assertEqual(['a', 'ab', 'b'], words_added)

    def test_ignores_letter_case_when_adding_letters(self):
        trie = Trie()
        trie.add('a')
        
        words_added = trie.get_all_words()
        self.assertEqual(1, len(words_added))

        trie.add('A')

        words_added = trie.get_all_words()
        self.assertEqual(1, len(words_added))

if __name__ == '__main__':
    unittest.main()