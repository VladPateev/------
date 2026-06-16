import pytest
from frog import is_anagram

def test_two_roots():
    assert is_anagram('дом', 'мод') == True

def add(x, y):
    return x + y

def test_add_numbers():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
