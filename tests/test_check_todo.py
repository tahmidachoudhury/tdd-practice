from lib.check_todo import *


"""
a given string could contain #TODO 
"""
def test_if_string_contains_todo():
    assert check_string("I need to clean my room #TODO") == True

"""
a given string that doesn't contain #TODO returns False
"""

def test_if_string_doesnt_contain_todo():
    assert check_string("I need to get a haircut") == False

"""
a given string that contains #TODO but in lowercase will give False
"""

def test_lowercase_todo_should_be_false():
    check_string("I have to my wash my car #todo") == False