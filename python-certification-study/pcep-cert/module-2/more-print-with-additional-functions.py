# These are the special functions to manipulate the end pf print function.

# 'sep' adds a separator between strings to be printed defined as (sep='-') or (sep='@') or (sep=',')
greeting_begining_of_the_day = 'Good morning'
print('The greeting at the begining of the day is: ', greeting_begining_of_the_day, ' everyone.', sep='-')

# end=' ' is used to place a space or what has been set after the displayed string default is a newline. 
greeting_begining_of_the_day = 'Good morning'
print('The greeting at the begining of the day is: ', greeting_begining_of_the_day, ' everyone', end='!!! ')
print('That is all.') # without the "end=" ot will just be the default of NewLine added!
print('Next module, please!')


