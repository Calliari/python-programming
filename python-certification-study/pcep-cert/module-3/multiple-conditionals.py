# Join multiple conditionals 
user_age = int(input('What is your age? '))
user_country = (input('What is your country? '))

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German exchange student programme')
else:
    print('Sorry, you do not qualify')


# ========================================================================
user_country = (input('What is your country? '))

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian exchange student programme')
else:
    print('Sorry, you do not qualify')


# ========================================================================
user_country = (input('Where do yo come from? '))

if not user_country == 'England':
    print('you are not from England')
else:
    print('You are from England')