# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math

# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-', abs(self.imag))


# Problem 5: Write code for the Set game here
def validate_input(list):
    assert len(list) == 12, "Please enter twelve cards."
    for card in list:
        assert len(str(card)) == 4, "Make sure that each card is 4 bits!"
        for i in range(0,4):
            assert int(str(card)[i]) < 3 and int(str(card)[i]) >= 0, "Invalid card bits range"

def is_match(c1, c2, c3):
    for i in range(0,4):
        column_sum = int(str(c1)[i]) + int(str(c2)[i]) + int(str(c3)[i])
        if column_sum % 3 != 0:
            return False
    return True

# Works, but would be cleaner if cards were stored in a 4x12 array (list of
# lists) instead of as strings (less casting)
def find_num_sets(filename):
    with open(filename) as f:
        lines = f.read().splitlines() 
    validate_input(lines)
    num_sets = 0
    # heinously inefficient O(N^3) and inelegant way of finding matches, but not a big deal
    # given there will never be more than 12 cards
    for i in range(0,12):
        for j in range(i+1,12):
            for k in range(j+1,12):
                if is_match(lines[i], lines[j], lines[k]):
                    num_sets += 1 # ++/-- doesn't exist in python?
    return num_sets 

def play_set(filename):
    num_sets = find_num_sets(str(filename))
    print("Number of sets:",num_sets)









