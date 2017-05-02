# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 1 - print out some cities
print '-' * 10
print '1'
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# 2 - print some states
print '-' * 10
print '2'
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: ", states["Florida"]

# 3 - do it by using the state then cities dict
print '-' * 10
print '3'
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# 4 - print every state abbreviation
print '-' * 10
print '4'
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# 5 - print every city in state
print '-' * 10
print '5'
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# 6 - now do both at the same time
print '-' * 10
print '6'
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

# 7 - safely get an abbreviation by state that might not be there
print '-' * 10
print '7'
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX is: %s" % city

