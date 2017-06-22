# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest
import math

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(1,3) == 4, "Addition failed on positive integers"
    assert soln.addition(-5,-7) == -12, "Addition failed on negative integers"
    assert soln.addition(1,0) == 1, "Additive identity failed"
    assert soln.addition(-4,2) == -2

def test_smallest_factor():
    assert soln.smallest_factor(2) == 2
    assert soln.smallest_factor(121) == 11 
    assert soln.smallest_factor(1) == 1


# Problem 2: Test the operator function from solutions.py
def test_operator():

    #exception testing
    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 1, float(1))
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be a string"

    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 1, "abc")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper should be one character"

    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 0, "/")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "You can't divide by zero!"

    with pytest.raises(Exception) as excinfo:
        soln.operator(1, 1, "?")
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Oper can only be: '+', '/', '-', or '*'"

    #output testing
    assert soln.operator(1, 1, "+") == 2, "Addition failed."
    assert soln.operator(2, 1, "/") == 2, "Division failed."
    assert soln.operator(1, 1, "-") == 0, "Subtraction faield."
    assert soln.operator(2, 2, "*") == 4, "Multiplication failed."

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_init(set_up_complex_nums):
    number_1 = soln.ComplexNumber(1, 2)
    assert number_1 == soln.ComplexNumber(1, 2) 

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_subtraction(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
    assert number_1 - number_3 == soln.ComplexNumber(-1, -7)
    assert number_2 - number_3 == soln.ComplexNumber(3, -4)
    assert number_3 - number_3 == soln.ComplexNumber(0, 0)

def test_complex_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.norm() == math.sqrt(5)
    assert number_2.norm() == math.sqrt(50)
    assert number_3.norm() == math.sqrt(85)

def test_complex_conjugate(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.conjugate() == soln.ComplexNumber(1, -2)
    assert number_2.conjugate() == soln.ComplexNumber(5, -5)
    assert number_3.conjugate() == soln.ComplexNumber(2, -9)

def test_complex_division(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 / number_2 == soln.ComplexNumber((3/10), (1/10))
    assert number_1 / number_3 == soln.ComplexNumber((4/17), (-1/17))
    assert number_2 / number_3 == soln.ComplexNumber((11/17), (-7/17))
    assert number_3 / number_3 == 1
    
    with pytest.raises(Exception) as excinfo:
        number_1 / 0
    assert excinfo.typename == 'ValueError'
    assert excinfo.value.args[0] == "Cannot divide by zero"

def test_complex_string(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1.__str__() == '1+2i'
    assert number_2.__str__() == '5+5i'
    assert number_3.__str__() == '2+9i'

def test_complex_eq(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert (number_1 == number_2) == False 
    assert (number_1 == number_1) == True

# Problem 4: Write test cases for the Set game.
def test_error_msgs():
    with pytest.raises(Exception) as excinfo:
        soln.play_set(nonexistent)
    assert excinfo.typename == 'NameError'
    assert excinfo.value.args[0] == "name 'nonexistent' is not defined"

    with pytest.raises(Exception) as excinfo:
        soln.play_set("foo.txt")
    assert excinfo.typename == 'FileNotFoundError'

    with pytest.raises(Exception) as excinfo:
        soln.play_set("badfile1.txt")
    assert excinfo.typename == 'AssertionError'
    assert excinfo.value.args[0] == "Please enter twelve cards."

    with pytest.raises(Exception) as excinfo:
        soln.play_set("badfile2.txt")
    assert excinfo.typename == 'AssertionError'
    assert excinfo.value.args[0] == "Make sure that each card is 4 bits!"

    with pytest.raises(Exception) as excinfo:
        soln.play_set("badfile3.txt")
    assert excinfo.typename == 'AssertionError'
    assert excinfo.value.args[0] == "Invalid card bits range"

    assert soln.is_match(1111, 1111, 1111) == True
    
    assert soln.find_num_sets("test.txt") == 6

