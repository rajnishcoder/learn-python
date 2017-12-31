######## Accessing Values in Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']  # dict['Name']:  Zara
print "dict['Age']: ", dict['Age'] # dict['Age']:  7


####### Updating Dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print "dict['Age']: ", dict['Age'] # dict['Age']:  8
print "dict['School']: ", dict['School'] # dict['School']:  DPS School


####### Delete Dictionary Elements
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary


###### Properties of Dictionary Keys
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']: ", dict['Name']  # dict['Name']:  Manni # When duplicate keys encountered during assignment, the last assignment wins



