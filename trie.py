from typing import List

class Trie:
    def __init__(self):
        self.dictionary = {}

    def add(self, word: str):
        pointer = self.dictionary
        for char in word:
            if char not in pointer:
                pointer[char] = {}
            pointer = pointer[char]
        
        self.__mark_word_end(pointer)
    
    def __mark_word_end(self, dictionary_pointer):
        if '#' not in dictionary_pointer:
            dictionary_pointer['#'] = True

    def has(self, word: str) -> bool:
        pointer = self.dictionary

        for char in word:
            if char not in pointer:
                return False 
            
            pointer = pointer[char]
        
        return '#' in pointer
    
    def get_all_words(self) -> List[str]:
        words_list = []
        self._get_words_from_node(self.dictionary, "", words_list)
        return words_list

    def _get_words_from_node(self, node, current_word, words_list):
        if '#' in node and node['#'] is True:
            words_list.append(current_word)

        for char, child_node in node.items():
            if char != '#':
                self._get_words_from_node(child_node, current_word + char, words_list)
