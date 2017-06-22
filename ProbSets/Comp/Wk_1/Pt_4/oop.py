import math

class Backpack(object):
    """ A backpack object class. Has a name and a list of contents.

    Attributes:
        name (str): the name of the backpack's owner
        contents (list): the contents of the backpack

    """
    def __init__(self, name, colour, max_size = 5):
        """ Set the name and intialize an empty contents list.

        Inputs:
            name (str): the name of the backpack's owner.

        Returns:
            A Backpack object with no contents.
        """

        self.name = name
        self.colour = colour
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        if len(self.contents) == self.max_size:
            print("No Room!")
            return
        self.contents.append(item)

    def take(self, item):
        self.contents.remove(item)

    def dump(self):
        self.contents = []

    def __eq__(self, other):
        return (self.colour == other.colour 
                and len(self.contents) == len(other.contents)
                and self.name == other.name)
        
    def __str__(self):
        return "{}{}{}{}{}{}{}{}{}{}".format('Owner:\t\t',self.name,
                '\nColour:\t\t', self.colour,
                '\nSize:\t\t', len(self.contents),
                '\nMax Size:\t', self.max_size,
                '\nContents:\t', self.contents)

def test_backpack():
    testpack = Backpack("Barry", "black")
    if testpack.max_size != 5:
        print("Wrong default max_size!")
    for item in ["pencil", "pen", "paper", "computer", "calculator"]:
        testpack.put(item)
    if len(testpack.contents) != 5:
        print("Put didn't add all items")
    testpack.dump()
    if len(testpack.contents) != 0:
        print("Dump didn't remove all items")
    print("Everything working well!")


class Jetpack(object):
    def __init__(self, name, colour, max_size = 2, fuel = 10):
        self.name = name
        self.colour = colour
        self.max_size = max_size
        self.fuel = fuel
        self.contents = []

    def fly(self, to_burn):
        if to_burn > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= to_burn

    def dump(self):
        self.contents = []
        self.fuel = 0

class ComplexNumber(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __abs__(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __lt__(self, other):
        return self.__abs__() < other.__abs__()

    def __gt__(self, other):
        return self.__abs__() > other.__abs__()

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)

    def __ne__(self, other):
        return (self.real != other.real) or (self.imag != other.imag)

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
            raise ValueError("Cannot divide by zero.")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.image/bottom)

















