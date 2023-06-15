# The while loop is basicaly  - while we met the condition keep runnig.

# Secret while look Game!


print('''
=================================
====== SECRET NUMBER GAME =======    
=================================
''')

secret_number = 7
user_unput = int(input('Try to guess the secret number from 0 to 20: '))
while user_unput != secret_number:
    print('Wrong guess!')
    user_unput = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! You have guessed the secret number! ')

