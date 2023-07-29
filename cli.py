from word_wheel_solver import WordWheelSolver 
from excluded_tags import get_excluded_tags
from corpus_adder import CorpusAdder
from nltk.corpus import brown
from typing import List
import nltk

def process_user_input():
    hub_letter = input('Please enter the hub letter: ')
    outer_letters = input('Please enter the outer letters (enter as a single string e.g. "abcdefgh"):')
    solution = get_solution(hub_letter, outer_letters)
    print(solution)

def get_solution(hub_letter: str, outer_letters: str) -> List[str]:
    solver = setup_solver()
    return solver.solve(hub_letter, outer_letters)

def setup_solver() -> WordWheelSolver: 
    word_wheel_solver = WordWheelSolver()
    excluded_tags = get_excluded_tags()
    add_corpus_to_solver(word_wheel_solver, excluded_tags)

    return word_wheel_solver

def add_corpus_to_solver(solver: WordWheelSolver, excluded_tags: List[str]):
    # add_brown_corpus_to_solver(solver)
    add_scrabble_dictionary_to_solver(solver)
    
def add_brown_corpus_to_solver(solver: WordWheelSolver):
    excluded_tags = get_excluded_tags()
    corpus_adder = CorpusAdder(excluded_tags)
    nltk.download('brown')
    brown_corpus = brown.tagged_words()
    corpus_adder.add_tagged_corpus_to_solver(brown_corpus, solver)

def add_scrabble_dictionary_to_solver(solver: WordWheelSolver):
    corpus_adder = CorpusAdder()
    corpus_adder.add_corpus_from_file('scrabble_dictionary.txt', solver)