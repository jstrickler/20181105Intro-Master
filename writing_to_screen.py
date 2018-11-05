#!/usr/bin/env python

a = 100
b = 'wombat'
c = 4.2372432

print(a, b, c)
print("OK")
print(a, b, c, sep=':')
print("OK")
print(a, b, c, sep=' <===> ')
print("OK")
print(a,b,c,end='')
print("OK")
print(a, b, c, end='Wocka wocka')
print("OK")

print("c is {:.2f}".format(c))
print("c is %.2f" % (c))  # legacy formatting


#         0      1      2              0   1  2
#         a      b      c
#  ".....{}.....{}.....{}.....".format(a, b, c)

actor = 'Brad Pitt'
city = 'Hollywood'

print("{} lives in {}".format(actor, city))

print(f"{actor} lives in {city}") # ONLY 3.6+

count = 12
value = 23.56

print("{:5d}/{:8.1f}".format(count, value))

big_number = 230482309482039482039482038420


print("{:,d}".format(big_number))



