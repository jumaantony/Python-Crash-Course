# decorators
# A function returning another function, usually applied as a function 
# transformation using the @wrapper syntax.

def my_decorator(func):
    def warp_func():
        print('***********')
        func()
        print('***********')

    return warp_func


@my_decorator
def hello():
    print('hellow')


hello()


# # decorators
# def my_decorator2(func):
#     def warp_func2(*args, **kwargs):
#         print('***********')
#         func(*args, **kwargs)
#         print('***********')

#     return warp_func2


# @my_decorator2
# def hello2(greetings, emoji=':('):
#     print(greetings, emoji)


# hello2('Hiiiiii')
