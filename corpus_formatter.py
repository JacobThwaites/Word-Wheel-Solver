from typing import List
from nltk.corpus import brown

class CorpusFormatter():
    def __init__(self):
        pass

    def write_unique_words_to_file(self, file_path: str, corpus: List[tuple]): 
        with open(file_path, 'w') as file:
            for word in corpus:
                file.write(f'{word}\n')

if __name__ == '__main__':
    corpus_formatter = CorpusFormatter()
    corpus = brown.tagged_words()
    corpus_formatter.write_unique_words_to_file('brown.txt', corpus)