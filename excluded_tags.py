from typing import List

def get_excluded_tags() -> List[str]:
    PLURAL_NOUN_TAG = 'NNS'
    PROPER_NOUN_TAG = 'NP'
    FOREIGN_WORD_TAG = 'FW'
    PLURAL_PROPER_NOUN_TAG = 'NPS'
    POSSESSIVE_PROPER_NOUN_TAG = 'NP$'
    POSSESSIVE_PLURAL_PROPER_NOUN_TAG = 'NPS$'
    SENTENCE_CLOSER_TAG = 'n'
    LEFT_PAREN_TAG = '('
    RIGHT_PAREN_TAG = ')'
    NOT_TAG = '*'
    DASH_TAG = '--'
    COMMA_TAG = ','
    COLON_TAG = ':'


    return [
        PLURAL_NOUN_TAG, 
        PROPER_NOUN_TAG, 
        FOREIGN_WORD_TAG, 
        PLURAL_PROPER_NOUN_TAG, 
        POSSESSIVE_PROPER_NOUN_TAG, 
        POSSESSIVE_PLURAL_PROPER_NOUN_TAG,
        SENTENCE_CLOSER_TAG,
        LEFT_PAREN_TAG,
        RIGHT_PAREN_TAG,
        NOT_TAG,
        DASH_TAG,
        COMMA_TAG,
        COLON_TAG
    ]