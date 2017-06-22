# Solutions to Exceptions.pdf (Exceptions and File I/O) Lab #6

import math
from random import choice

def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
            "digits differ by 2 or more: ")
    if len(step_1) != 3:
        raise ValueError("number must be three digits")

    if abs(int(step_1[0]) - int(step_1[2])) != 2:
        raise ValueError("first and last digits must differ by 2 or more")
    

    step_2 = input("Enter the reverse of the first number, obtained "
            "by reading it backwards: ")
    for i in range(0, 3):
        if (step_1[i] != step_2[2-i]):
            raise ValueError("second number must be reverse of first.")

    step_3 = input("Enter the positive difference of these numbers: ")
   
    if int(step_3) != abs(int(step_1) - int(step_2)):
        raise ValueError("3rd number must be positive difference of first two")

    step_4 = input("Enter the reverse of the previous result: ")
    for i in range(0,3):
        if (step_4[i] != step_3[2-i]):
            raise ValueError("fourth number must be reverse of third.")

    print(str(step_2), "+", str(step_4), "= 1089 (ta-da!)")

def random_walk(max_iters=1e12):
    walk = 0
    direction = [1,-1]
    for i in range(int(max_iters)):
        try:
            walk += choice(direction)
        except KeyboardInterrupt as e:
            print("Process interrupted at iteration", i)
            break
    else:
        print("Process completed")
    return walk

class ContentFilter(object):

    def __init__(self, filename):
        if not isinstance(filename, str):
            raise TypeError("Filename must be a string")
        self.name = filename
        with open(filename, 'r') as myfile:
            self.contents = myfile.read()
        myfile.close()

    def uniform(self, filename,  mode='w', case="upper"):
        if mode != 'w' and mode != 'a':
            raise ValueError("Mode must be 'w' or 'a'")
        with open(filename, mode) as outfile:
            if case == "upper":
                outfile.write(self.contents.upper())
            else:
                outfile.write(self.contents.lower())

    def reverse(self, filename, mode='w', unit="line"):
        if unit != "line" and unit != "word":
            raise ValueError("Mode must be 'line' or 'word'")
        with open(filename, mode) as outfile:
            if unit == "word":
                out_str = self.contents.split(" ")
                out_str.reverse()
                outfile.write(" ".join(out_str))
            else:
                out_str = self.contents.split("\n")
                out_str.reverse()
                outfile.write("\n".join(out_str))

    #TODO: implement this function
    def transpose(self, filename, mode='w'):
        with open(filename, mode) as outfile:
            out_str = self.contents.split("\n")


            outfile.write(out_str)

    def __str__(self):
        num_alpha = 0
        num_num = 0
        num_white = 0
        num_lines = 0
        for i in range(len(self.contents)):
            if self.contents[i].isalpha():
                num_alpha += 1
            if self.contents[i].isdigit():
                num_num += 1
            if self.contents[i].isspace():
                num_white += 1
            num_lines = self.contents.count('\n')

        return "{}{}{}{}{}{}{}{}{}{}{}{}".format('Source file:\t\t', self.name,
                '\nTotal characters:\t', len(self.contents),
                '\nAlphabetic characters:\t', num_alpha,
                '\nNumerical characters:\t', num_num,
                '\nWhitespace characters:\t', num_white,
                '\nNumber of lines:\t', num_lines)
















