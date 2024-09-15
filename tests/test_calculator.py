'''My Calculator Tests'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(6,2) == 8

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(5,2) == 3
