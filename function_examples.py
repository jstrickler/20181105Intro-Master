#!/usr/bin/env python


def hi():
    print("Hi, students!!")


def get_message():
    return "Hello, world"


h = get_message()
print(h)

print("My message is {}".format(get_message()))


def hello():
    m = get_message()
    print(m)

hello()
print()


def greet(target):
    print("Hello, {}".format(target))


greet('world')
greet('Mom')
greet('Sailor')
greet(1234)
greet(None)


def blank():
    pass


b = blank()
print(b)
print(blank())



def invade(method='land', *countries):
    print("starting campaign:")
    print("\tcountry list:", countries)
    for country in countries:
        print("\tInvading {} by {}".format(country, method))
    print()

invade('air', 'Guatemala')
invade('land', 'Canada')
invade('sea', 'Micronesia')
invade('air', 'Benin', 'Togo', 'Burkina Faso')
invade()



















