# Interating with elements using loop


big_cities = ['London', 'New York', 'Los Angeles', 'France', 'Edinburg']
for city_index in range(len(big_cities)):
    print('The city on index:', city_index ,'is:', big_cities[city_index])


# A loop that will sum on the elements using loop
spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
print('Total spent is:', sum)