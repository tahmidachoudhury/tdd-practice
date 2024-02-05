from lib.counter import *

def test_if_counter_reaches_5():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == 'Counted to 5 so far.'


def test_if_counter_reaches_14():
    counter = Counter()
    counter.add(9)
    counter.add(5)
    result = counter.report()
    assert result == 'Counted to 14 so far.'