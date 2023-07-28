from word_wheel_solver import WordWheelSolver 
from excluded_tags import get_excluded_tags
from corpus_adder import CorpusAdder
from nltk.corpus import brown

def main():
    word_wheel_solver = WordWheelSolver()
    excluded_tags = get_excluded_tags()
    corpus_adder = CorpusAdder(excluded_tags)
    corpus = brown.tagged_words()
    corpus_adder.add_corpus_to_solver(corpus, word_wheel_solver)

    test_solution = word_wheel_solver.solve('e', 'fhiiorrd')
    print(test_solution)
    pass

if __name__ == '__main__':
    main()