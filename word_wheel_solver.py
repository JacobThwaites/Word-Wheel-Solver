from typing import List
from trie import Trie
from word_validator import WordValidator

class WordWheelSolver():
    def __init__(self):
        self.trie = Trie()
        self.word_validator = None
        pass

    def get_words_in_dictionary(self) -> List[str]:
        return self.trie.get_all_words()
    
    def add_word_to_dictionary(self, word: str):
        self.trie.add(word)
    
    def solve(self, hub_letter: str, outer_letters: str) -> List[str]:
        self.word_validator = WordValidator(hub_letter, outer_letters)
        all_letters = hub_letter + outer_letters

        self.solutions = []
        self.__get_solutions('', self.trie.dictionary, [char for char in all_letters])
        return self.solutions
    
    
    def __get_solutions(self, current_word: str, dictionary_pointer, remaining_letters: List[str]) -> List[str]: 
        for i, char in enumerate(remaining_letters):
            if char in dictionary_pointer: 
                current_word += char
                print(current_word)
                if self.word_validator.is_word_valid(current_word):
                    self.solutions.append(current_word)

                new_remaining_letters = remaining_letters[:i]+ remaining_letters[i+1:]
                self.__get_solutions(current_word, dictionary_pointer[char], new_remaining_letters)
                current_word = current_word[:-1]