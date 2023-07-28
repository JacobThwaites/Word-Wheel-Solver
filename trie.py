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