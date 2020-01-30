import pytest
import bar as test
 
def test_bar_under_age():
    assert test.bar(15) == "Sorry, 15 is too young for a beer, how about a soda?"

def test_bar_over_age():
    assert test.bar(25) == "Have a beer!"

def test_bar_under_1_yr():
    assert test.bar(20) == "So close..one more year kid."