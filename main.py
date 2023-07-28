from word_wheel_solver import WordWheelSolver 
from excluded_tags import get_excluded_tags
from corpus_adder import CorpusAdder
from nltk.corpus import brown
import nltk

def main():
    word_wheel_solver = WordWheelSolver()
    excluded_tags = get_excluded_tags()
    corpus_adder = CorpusAdder(excluded_tags)
    nltk.download('brown')
    brown_corpus = brown.tagged_words()
    corpus_adder.add_tagged_corpus_to_solver(brown_corpus, word_wheel_solver)

    # Solve using Scrabble dictionary
    # corpus_adder = CorpusAdder()
    # corpus_adder.add_corpus_from_file('scrabble_dictionary.txt', word_wheel_solver)
    
    test_solution = word_wheel_solver.solve('c', 'farnagre')
    print(test_solution)

if __name__ == '__main__':
    main()