# Basic conditionals with if statements


## Logical operatos
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# == equals
# != not equals

login_password = (input('Do you know the secret password: '))
if login_password == "--secret007":
    print('Correct, yo know the login password')
else:
    print('Not correct, you don\'t know the password!')


# A sligly different way of doing the same above but with the (not equals)
guess_word = (input('Do you know the word: '))
if guess_word != "programming":
    print('Not correct, you don\'t know the word!')
else:
    print('Correct, you know the word')


# Boolean [True, False]
if True:
    print('Condition met, print this string')

if False:
    print('Condition not met, never print this sting')