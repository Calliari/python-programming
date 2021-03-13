# decrease 
number = 10
while number > 0:
    print('*' * number)
    number -= 1

'''
**********
*********
********
*******
******
*****
****
***
**
*
'''

# increase
number = 10
adding = 1
while number > adding > 0:
    print('*' * adding)
    adding += 1

'''
*
**
***
****
*****
******
*******
********
*********
'''

# combined - decrease & increase
decrease_number = 10
hold_number = decrease_number
while decrease_number > 0:
    print('*' * decrease_number)
    decrease_number -= 1
    if decrease_number == 0:
        increase_number = 1
        while hold_number > increase_number > 0:
            print('*' * increase_number)
            increase_number += 1
'''
**********
*********
********
*******
******
*****
****
***
**
*
*
**
***
****
*****
******
*******
********
*********
'''

# combined - increase & decrease 
number = 10
for i in range(number):
    print('*' * i)
    i += 1
    if i == number:
        range_number = range(number)
        for i in range(number):
            del range_number[-1]
            print('*' * len(range_number))
'''
*
**
***
****
*****
******
*******
********
*********
*********
********
*******
******
*****
****
***
**
*
'''