""" factorial problem using recursion
this is a process in which a function calls itself repeatedly
 """


# recursion using factorial func
"""def fact(n):
    if n == 6:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
"""
"""""fibonacci sequence is a sequence where each number is the sum 
of the two preceding one e.g 0,1,1,2,3,5,8,13 .... """


def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
