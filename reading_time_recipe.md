## 1. Describe the Problem

_write the user story here._

Problem: As a user,
So that I can manage my time,
I want to see an estimate of reading time for a text, 
assuming I can read 200 words a minute.

To solve, I require the number of words in a text. Which can then be divided by 200 to work out number of minutes it will take to read. 

## 2. Design the Function Signature
```python
def reading_time(my_string):
    """ counts number of words in the string and divides by 200

    Parameters: 
        my_string: string containg words (e.g. "hello world")

    Returns: 
        Integer, number of minutes it takes to read the string
        Built into an f'string with message:
        "This text takes {number} minutes to read"

    Side effects: 
        None

    Creating long text: 
    text = " ".join(["word" for i in range(0, 200)])
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests
_list of examples of what the function will take and return._
```python

"""
Given a string of less than 200 words
Returns "This text takes less than 1 minutes to read"
"""
reading_time("Short Text") => "This text takes less than 1 minutes to read"

def test_reading_time_short_text():
    result = reading_time("Short Text")
    assert result == "This string takes less than 1 minute to read"

"""
test, if the string is empty 
returns, error message
"""
def test_reading_time_empty_string():
    with pytest.raises(Exception) as e:
        reading_time("")
    error_message = str(e.value)
    assert error_message == "There is no text to read"

"""
test, long text
returns, number of minutes to read in a f'string
"""
def test_reading_time_long_text():
    long_text = "This is an example passage written to contain exactly two hundred words while remaining clear, neutral, and easy to adapt for different purposes. The text does not follow a particular theme, because the goal is to provide a flexible sample that can be used for practice, testing, or demonstration. When preparing a passage of a specific length, it is helpful to focus on steady pacing and straightforward language. This allows the words to flow naturally without appearing forced or overly repetitive. In this example, the content touches on general ideas about writing, intention, and the way people work with text. Many learners use controlled passages like this when exploring reading speed, software behaviour, or editing techniques. By avoiding specialised terminology, the passage stays accessible to a wide audience and can be repurposed in classrooms, coding exercises, or design mock-ups. Another advantage of neutral text is that it encourages attention to structure rather than meaning. Writers can experiment with rewriting sentences, expanding ideas, or making the language more concise, all while maintaining the required word count. Creating a two-hundred-word passage also demonstrates how small adjustments influence length. Adding or removing short phrases can shift the total significantly. This example therefore serves as a practical illustration of how to produce a measured and coherent block of writing."
    result = reading_time(long_text)
    assert result == "This string takes 1 minutes to read"

## 4. Implement the Behaviour
_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

