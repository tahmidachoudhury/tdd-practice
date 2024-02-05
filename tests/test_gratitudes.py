from lib.gratitudes import *

"""
Initially, 
there should be no gratitudes
"""

def test_initial_gratitudes():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

"""
When a gratitude is added, it should show in list
"""

def test_added_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Waking up today")
    assert gratitudes.format() == "Be grateful for: Waking up today"


"""
Test for multiple gratitudes
"""

def test_added_multiple_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("Waking up today")
    gratitudes.add("having breakfast ready")
    assert gratitudes.format() == "Be grateful for: Waking up today, having breakfast ready"