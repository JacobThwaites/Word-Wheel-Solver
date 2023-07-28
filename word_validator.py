class WordValidator():
    def __init__(self, hub_letter: str):
        self.hub_letter = hub_letter

    def is_word_valid(self, word: str) -> bool:
        if self.hub_letter not in word:
            return False
        
        if len(word) < 4:
            return False
    
        return True