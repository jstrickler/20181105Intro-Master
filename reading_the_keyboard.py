#!/usr/bin/env python


name = input("What is your name? ")
country = input("What country are you from? ")
count = input("How many cheers? ")

print("Welcome, {} from {}".format(name, country))
print("Rah! " * int(count))

