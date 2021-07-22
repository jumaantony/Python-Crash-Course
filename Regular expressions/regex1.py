"""
regular expressions are useful when checking validations/matching i.e password
or emails.
python regular expressions are usefull in finding a piece of information
"""

import re

string = 'Hellow Juma? Are you there? hey.. you'

# commonly used search
print('juma' in string)

# regular expressions
a = re.search('Juma', string)

print(a.span())
print(a.start())
print(a.group())  # useful when performing multiple searches

pattern = re.compile('you')
b = pattern.search(string)
c = pattern.findall(string)  # finds all the instances of the match
d = pattern.fullmatch(string)  # returns the full match of the entire string
e = pattern.match(string)

print(c)