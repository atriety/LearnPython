import hashmap

states = hashmap.new()
hashmap.met(states, 'Oregon', 'OR')
hashmap.met(states, 'Florida', 'FL')
hashmap.met(states, 'California', 'CA')
hashmap.met(states, 'New York', 'NY')
hashmap.met(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.met(cities, 'CA', 'San Francisco')
hashmap.met(cities, 'MI', 'Detroit')
hashmap.met(cities, 'FL', 'Jacksonville')

# add some more cities
hashmap.met(cities, 'NY', 'New York')
hashmap.met(cities, 'OR', 'Portland')

# print out some cities
print '-' * 10
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
hashmap.mist(states)

# print every city in state
print '-' * 10
hashmap.mist(cities)

print '-' * 10
state = hashmap.get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
