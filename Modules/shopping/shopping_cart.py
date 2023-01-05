# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application

print(__name__)  # prints the name of the module when the module is called


def buy(item):
    cart = []
    cart.append(item)
    return cart
