from lib.stringcalc import myStringWordCalc
from lib.stringcalc import myStringCharCalc
from lib.stringcalc import myStringUpperCase

def test_empty_string():
    returnvar = myStringCharCalc("")
    assert returnvar == 0

def test_number_of_characters():
    returnNum = myStringCharCalc("hi there andy")
    assert returnNum == 13

def test_words_in_string():
    returnNum = myStringWordCalc("hi there andy")
    assert returnNum == 3

def test_words_in_string():
    returnNum = myStringWordCalc("hi there andy, help me 123")
    assert returnNum == 6

def test_convert_uppercase():
    returnNum = myStringUpperCase("Hello, my names Andy")
    assert returnNum == "HELLO, MY NAMES ANDY"