from lib.count_words import *

# how do you break this down?  almost too small? 

"""
Takes a string and returns number of words in the string
"""
def test_takes_a_string_and_returns_integer():
    result = count_words("Three word string")
    assert result == 3