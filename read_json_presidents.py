#!/usr/bin/env python
import json
from pprint import pprint

with open('DATA/presidents.json') as pres_in:
    president_data = json.load(pres_in)

pprint(president_data)
print('-' * 60)

print(type(president_data))
print()

for potus in president_data['presidents']:
    print(potus['fname'], potus['lname'])


json_data = """
{ "mystuff": [
    {
        "num":1,
        "lname":"Washington",
        "fname":"George",
        "dstart":"1789-04-30",
        "dend":"1797-03-04",
        "birthplace":"Westmoreland County",
        "birthstate":"Virginia",
        "dbirth":"1732-02-22",
        "ddeath":"1799-12-14",
        "party":null
    },

    {
        "num":2,
        "lname":"Adams",
        "fname":"John",
        "dstart":"1797-03-04",
        "dend":"1801-03-04",
        "birthplace":"Braintree, Norfolk",
        "birthstate":"Massachusetts",
        "dbirth":"1735-10-30",
        "ddeath":"1826-07-04",
        "party":"Federalist"
    }
    ]
}
"""

my_data = json.loads(json_data)
print(my_data)


