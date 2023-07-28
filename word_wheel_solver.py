from typing import List
from trie import Trie

class WordWheelSolver():
    def __init__(self):
        self.dictionary = Trie()
        pass

    def get_words_in_dictionary(self) -> List:
        return self.dictionary.get_all_words()
    
    def add_word_to_dictionary(self, word: str):
        self.dictionary.add(word)
    
    def solve(self, hub_letter: str, outer_letters: List[str]) -> List[str]:
        return []