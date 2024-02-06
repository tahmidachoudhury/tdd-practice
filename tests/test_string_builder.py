from lib.string_builder import *

def test_if_hello_returns_5():
    greeting = StringBuilder()
    greeting.add('hello')
    result = greeting.size()
    assert result == 5

def test_if_hello_returns_hello():
    greeting = StringBuilder()
    greeting.add('hello')
    result = greeting.output()
    assert result == 'hello'

def test_simple_sentences():
    greeting = StringBuilder()
    greeting.add('hello')
    greeting.add(' ')
    greeting.add('there!')
    result = greeting.output()
    assert result == 'hello there!'