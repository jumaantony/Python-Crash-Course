# raw_input function. it reads one line from a standard input and returns it as a string
import pipenv.vendor.click._compat
from pip._vendor.distlib.compat import raw_input

name = raw_input("Input your name")
print(name)

# input function. it returns an evaluated python result
Enter_str = input('Enter desired expression')
print(Enter_str)