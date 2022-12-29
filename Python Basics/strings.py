#Strings are immutable meaning they cant be changed...
#  declaring a string
protein = 'eggs'

possession = 'juma\'s ' # escaping a quote

# new line
newline = 'This is a line \n  this is a new line'

print(newline)

word = 'helloo'

# String Slicing

print(word[0]) # character in position zero

print(word[-2]) # character in second last position

print(word[0:2]) # print charcters between 0 and 2

print(word[2:5]) # print charcters between 2 to 5 i.e 2,3,4

print(word[:3]) # print characters from 0 to 3 ie. 0,1,2

print(word[3:]) # print charcters as from 3 

print(len(word)) # printing the length