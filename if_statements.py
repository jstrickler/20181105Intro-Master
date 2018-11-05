#!/usr/bin/env python

value = 56

if value > 75:
    print("wheelbarrow")
    print("cockatoo")
elif value > 50:  # else if
    print("koala")
    print("wallaby")
    if value > 55:
        print("drop bear")
else:
    print("wombat")
    print("scythe")


#  if elif else while for with def class try except finally
#  async with
#  async def


# given X
# if X is a number,  X=0 is False, X=non-0 is True
# if len(X) is 0, X is false

# True=1  False=0

count = 42

if count > 40:
    size = 'big'
else:
    size = 'medium'

size = 'big' if count > 40 else 'medium'

# create_product('big' if count > 40 else 'medium')


#  == != > < >= <=


if count == 12:
    print("Whoo-hoo")


if count != 12:
    print("Wocka-wocka")


if (value > 50) and (count < 100):
    print("rutabaga")

# and or not

#  x and y
#  x or y
#  not x

if (50 < value < 60) and (10 < count < 1000):
    print("hogweed")



