""" Ways to debug in python:
1. linting
2. Using Ide/Editors
3. Reading the error outputted
4. Using python debugger
"""

# python debugger
import pdb


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(4, 4)
