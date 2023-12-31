from typing import List
from trie import Trie
from word_validator import WordValidator

class WordWheelSolver():
    def __init__(self):
        self.trie = Trie()
        self.word_validator = None
        self.solutions = []
        pass

    def get_words_in_dictionary(self) -> List[str]:
        return self.trie.get_all_words()
    
    def add_word_to_dictionary(self, word: str):
        self.trie.add(word)
    
    def solve(self, hub_letter: str, outer_letters: str) -> List[str]:
        self.word_validator = WordValidator(hub_letter)
        all_letters = hub_letter + outer_letters

        self.solutions = []
        self.__get_solutions('', self.trie.dictionary, [char for char in all_letters])
        self.__remove_duplicates_from_solution()
        return self.solutions
    
    
    def __get_solutions(self, current_word: str, dictionary_pointer, remaining_letters: List[str]) -> List[str]: 
        for i, char in enumerate(remaining_letters):
            if char in dictionary_pointer: 
                current_word += char
                if self.__is_valid_word(current_word, dictionary_pointer):
                    self.solutions.append(current_word)

                new_remaining_letters = remaining_letters[:i]+ remaining_letters[i+1:]
                self.__get_solutions(current_word, dictionary_pointer[char], new_remaining_letters)
                current_word = current_word[:-1]
    
    def __is_valid_word(self, word: str, dictionary_pointer) -> bool:
        return self.word_validator.is_word_valid(word) and '#' in dictionary_pointer[word[-1]]
    
    def __remove_duplicates_from_solution(self):
        self.solutions = [x for i, x in enumerate(self.solutions) if x not in self.solutions[:i]]