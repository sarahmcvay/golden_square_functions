from lib.grammar_check import *

"""
Given a sentence with a capital and full stop
Returns True 
"""
def test_with_valid_sentence():
    result = grammar_check("Hello this is a nice day.")
    assert result == True 

"""
Given a sentence with a capital and no full stop
Returns False 
"""
def test_with_no_full_stop():
    result = grammar_check("Hello this is a nice day")
    assert result == False 

"""
Given a sentence with a capital and question mark
Returns True 
"""
def test_with_question_mark():
    result = grammar_check("Hello this is a nice day?")
    assert result == True 

"""
Given a sentence with a capital and exclamation mark
Returns True 
"""
def test_with_exclamation_mark():
    result = grammar_check("Hello this is a nice day!")
    assert result == True 

"""
Given a sentence with a capital and ending with a comma
Returns False
"""
def test_ending_with_comma():
    result = grammar_check("Hello this is a nice day,")
    assert result == False

"""
Given a sentence with no capital and full stop
Returns True 
"""
def test_with_valid_sentence():
    result = grammar_check("hello this is a nice day.")
    assert result == False 