from word_wheel_solver import WordWheelSolver 
from excluded_tags import get_excluded_tags
from corpus_adder import CorpusAdder
from nltk.corpus import brown
from typing import List
import nltk

def get_solution(hub_letter: str, outer_letters: str) -> List[str]:
    solver = __setup_solver()
    return solver.solve(hub_letter, outer_letters)

def __setup_solver() -> WordWheelSolver: 
    word_wheel_solver = WordWheelSolver()
    excluded_tags = get_excluded_tags()
    __add_corpus_to_solver(word_wheel_solver, excluded_tags)

    return word_wheel_solver

def __add_corpus_to_solver(solver: WordWheelSolver, excluded_tags: List[str]):
    __add_brown_corpus_to_solver(solver)
    # __add_scrabble_dictionary_to_solver(solver)
    
def __add_brown_corpus_to_solver(solver: WordWheelSolver):
    excluded_tags = get_excluded_tags()
    corpus_adder = CorpusAdder(excluded_tags)
    nltk.download('brown')
    brown_corpus = brown.tagged_words()
    corpus_adder.add_tagged_corpus_to_solver(brown_corpus, solver)

def __add_scrabble_dictionary_to_solver(solver: WordWheelSolver):
    corpus_adder = CorpusAdder()
    corpus_adder.add_corpus_from_file('scrabble_dictionary.txt', solver)