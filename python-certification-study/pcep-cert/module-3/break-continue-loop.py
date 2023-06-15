# Inside the looks it's very comom to se BREAK or CONTINUE functions, ie:


# Infinity look with 'break'
while True:
    name = input('Enter a name until you type EXIT to close the program: ')
    if name == 'EXIT':
        break
    print('Hello', name)



# Looks for a somethinhg when conditionn met skip and 'continue'
# All the division modules by 5 equals to 0,  skip and 'continue' the priting
for i in range(1, 20):
    if i % 5 == 0:
        continue
    print(i)
