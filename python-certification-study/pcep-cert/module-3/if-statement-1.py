# Basic conditionals with if statements

user_age = int(input('What is your age?'))
if user_age > 30:
    print('Your are over 30 years old.')
    print('You probably know what you\'re doing! Mature person!!!')
elif user_age == 30:
    print('You are exacly 30 years old.')
    print('Time to become a mature person and think before act!!!')
else:
    print('You are less than 30 years old.')
    print('Still have time to make mistakes and enjoy before take all the responsability in life!!!')