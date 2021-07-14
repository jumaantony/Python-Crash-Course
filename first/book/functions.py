def addition():
    return x + y


x = 2
y = 3
print(addition())


# Function Arguments
# required arguments
def printme(str):
    """this prints a passed string into this func"""
    print(str)
    return


printme('hellow')

# Keyword Arguments
printme(str="My string")

# lambda func
add = lambda arg1, arg2: arg1 + arg2
print(add(10, 20))
