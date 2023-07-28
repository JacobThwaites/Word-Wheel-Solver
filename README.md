# Word Wheel Solver

A project designed to find as many solutions as possible for a word wheel puzzle

<img src='./public/word_wheel.png' height='300px'/>


## Puzzle Definition
A word wheel puzzle has 8 outer letters and 1 hub letter. 
A player must find as many words as possible.
Each word must use the hub wheel and at least 3 other letters, and letters can only be used once.
You can't use plurals, foreign words or proper nouns. 
Verb endings with 's' are permitted.
Each puzzle contains a single 9-letter word.

## Prerequisites
Python 3

# Usage 
The project can be run locally using the terminal command:
<br />

```bash 
$ python3 main.py
```

You can modify the hub letter and outer letters inside the main function to change the puzzle. 
 
<br />

By default the solver uses the NLTK Brown Corpus for word matching. 
This can also be switched to use the Scrabble dictionary (all 4-9 letter words from this are stored locally in [scrabble_dictionary.txt](scrabble_dictionary.txt)). This tends to get much more matches, although isn't pre-tagged so the solver can't exclude invalid words. 

## Testing
Tests are written using the ```unittest``` library.
They can be run locally using:

```bash
$ python3 run_tests.py
```