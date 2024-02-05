from lib.greet import *

def test_greet():
    greet('Tom')
    assert 'Hello, Tom'