from lib.make_snippet import *

"""
If the string is empty, 
Returns an empty string 
"""
def test_string_empty():
    result = make_snippet("")
    assert result == ""

"""
If the string is less than five words, 
Return string as is.
"""
def test_string_five_words():
    result = make_snippet("This string is five words")
    assert result == "This string is five words"

"""
If the string is more than five words, 
Returns the first five words, followed by '...'
"""
def test_string_more_than_five_words():
    result = make_snippet("This string is a bit too long")
    assert result == "This string is a bit..."

"""
If integer is passed instead of a string. 
"""