'''My Calculator Tests'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(6,2) == 8

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(5,2) == 3

def test_multiplication():
    '''Test that addition function works '''    
    assert multiply(8,8) == 64

def test_division():
    '''Test that addition function works '''    
    assert divide(5,5) == 1.0
