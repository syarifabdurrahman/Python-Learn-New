# Keyword Arguments

from mimetypes import init


def my_function(a, b, c):
    pass
    # Do this with a
    # The do that with b
    # Finally do this with c

# Keyword default Arguments


def my_function(a=1, b=2, c=3):
    pass
    # Do this with a
    # The do that with b
    # Finally do this with c
# my_function(a=1, b=2, c=3)

# *args: many positional arguments


# def add(*args):
#     # print(args[2])
#     return sum(args)


# print(add(1, 2, 3, 4, 5))

# *kwargs: many keyword arguments


# def calculate(n, **kwargs):
#     print(type(kwargs))
#     # print(kwargs['add'])
#     # for key, value in kwargs.items():
#     #     print(value)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)


# calculate(3, add=3, multiply=5)

# how **kwarg work on tkinter


class Car:
    def __init__(self, **kw):
        # if this all not exist will return none instead of error so using get will solve this problemn
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('color')


my_car = Car(make="Nissan")
print(my_car.model)
