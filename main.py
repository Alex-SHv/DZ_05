import colorama

help(colorama)

intro_list = []
for mathod in dir(intro_list):
    print(mathod)


def first_function():
    pass


class Human:
    pass


cr = colorama
first_f = first_function
nick = Human

print(colorama.__name__)
print(cr.__name__)
print(first_function.__name__)
print(first_f.__name__)
print(Human.__name__)
print(nick.__name__)

print(__name__)