## 1. Describe the Problem
    As a user, 
    So that I can improve my grammar
    I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

we will assume one sentence 

## 2. Design the Function Signature
```python

def grammar_check(my_text):
    """ Checks text starts with a capital letter
        Checks text ends with either "." "?" or "!"

    Parameters: 
        my_text: a string containing words and punctuation (e.g. "hello WORLD")

    Returns: 
        Boolean: True if valid or False otherwise

    Side effects: 
        None
    """
    pass 
```

## 3. Create Examples as Tests
```python
# EXAMPLE

"""
Given a sentence with a capital and full stop
Returns True 
"""
grammar_check("Hello this is a nice day.")
=> True 

"""
Given a sentence with a capital and question mark
Returns True 
"""
grammar_check("Hello this is a nice day?")
=> True 

"""
Given a sentence with a capital and no full stop
Returns False 
"""
grammar_check("Hello this is a nice day")
=> False 

"""
Given a sentence with no capital and no full stop
Returns False 
"""
grammar_check("hello this is a nice day")
=> False 

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
