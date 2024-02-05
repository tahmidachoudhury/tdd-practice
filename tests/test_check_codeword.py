from lib.check_codeword import *

def test_if_codeword_is_horse():
    assert check_codeword('horse') == 'Correct! Come in.'

def test_different_codewords():
    assert check_codeword('hello') == 'WRONG!'
    assert check_codeword('heeeeeey') == 'WRONG!'
    assert check_codeword('HorsE') == 'WRONG!'