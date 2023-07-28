from typing import List
from nltk.corpus import brown
from excluded_tags import get_excluded_tags
from word_wheel_solver import WordWheelSolver

class CorpusAdder():
    def __init__(self, excluded_tags=[]):
        self.excluded_tags = excluded_tags

    def add_tagged_corpus_to_solver(self, corpus: List[tuple], solver: WordWheelSolver): 
        for word_tag_pair in corpus:
            tag = word_tag_pair[1]
            if tag not in self.excluded_tags:
                solver.add_word_to_dictionary(word_tag_pair[0])

    def add_corpus_from_file(self, file_path: str, solver: WordWheelSolver):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                solver.add_word_to_dictionary(line)

    def write_unique_words_to_file(self, file_path: str, corpus: List[tuple]): 
        with open(file_path, 'w') as file:
            for word_tag_pair in corpus:
                tag = word_tag_pair[1]
                if tag not in self.excluded_tags:
                    file.write(str(word_tag_pair) + '\n')

if __name__ == '__main__':
    excluded_tags = get_excluded_tags()
    corpus_adder = CorpusAdder(excluded_tags)
    corpus = brown.tagged_words()
    corpus_adder.write_unique_words_to_file('brown.txt', corpus)