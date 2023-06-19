# This is anotehr data-type in python calectors which is a feature that allow python program uses 'lists', 'tuples' & 'dictionaries'


# This is a example of list which is used to store multiple values at the same time
big_cities = ['London', 'New York', 'Los Angeles', 'France', 'Edinburg']
print(big_cities)
print('My favourite cite among those cities is', big_cities[2]) # it's also indexed starting from '0' zero
print('I live in', big_cities[-5]) # and the index can work with negative value starting from the last to the first
print('The city I\'d to visit and the city I already visited are, respectively', big_cities[1:3]) # combine two elements of the list - this is called slicing
print('Cites I lived before are:', big_cities[:1]) # slicing from element '0' until '1' = 'London'
print('Cites I never lived before are:', big_cities[1:]) # slicing from element '1' until 'last' = 'New York', 'Los Angeles', 'France', 'Edinburg'
print('US Cites included in the list are:', big_cities[1:3]) # slicing from element '1' until '2' = 'New York', 'Los Angeles',
print('Europe Cites included in the list are:', big_cities[0], big_cities[3:5]) # slicing from element '3' until '4' = 'France', 'Edinburg',
print('Northern Europe Cite included in the list is:', big_cities[-1]) # slicing the element from last when negative index is used = 'Edinburg',



### Manipulate elements 'delete'
big_cities = ['London', 'New York', 'Los Angeles', 'France', 'Edinburg']

del big_cities[1]
print(big_cities) # removed the index 2 'New York' from the list

del big_cities[2:]
print(big_cities) # removed the from index 3 to the last - from the new list update above

del big_cities[:]
print(big_cities) # removed all elements from the list

del big_cities
# print(big_cities) # delete the list vaiable with all elements on it - which will cause an error as the list is gone!

### Manipulate elements 'adding'
big_cities = ['London', 'New York', 'Los Angeles', 'France', 'Edinburg']

big_cities.append('Milan')
print(big_cities) # adding a new element to the list

big_cities.insert(2,'Lisbon')
print(big_cities) # adding a new element specifiing the index location