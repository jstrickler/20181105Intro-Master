#!/usr/bin/env python

d1 = dict()
print(d1, type(d1))
airports = {'BOS': 'Boston Logan', 'RDU': 'Raleigh-Durham', 'LGA': 'La Guardia'}
d3 = {}  # empty dict

airports['ANC'] = 'Anchorage'

airports['AUS'] = 'Austin'

airports['JFK'] = 'Kennedy'

print(airports)

airports['JFK'] = 'NY/Kennedy'
airports['LGA'] = 'NY/La Guardia'

print(airports)

print(airports['ANC'])

print(airports.get('LAX'))
print(airports.get('LAX', 'NOT FOUND'))

more_airports = {'ALB': 'Albany', 'IAD': 'Dulles', 'YYZ': 'Toronto', 'BOS': 'Logan'}

airports.update(more_airports)

print(airports, '\n')

print(len(airports))
print(airports.items())

for abbr, airport in sorted(airports.items()):
    print(abbr, airport)




