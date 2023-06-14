# ========================================================================
answer_a = input('Do you like traveling? y/n: ')

if answer_a == 'y':
    print('Good!')
    answer_b = input('And do you like Asia? y/n:')
    if answer_b == 'y':
        print('Excellent, you can win a ticket to Thailand!')
    else:
        print('Sorry to heaar that you don\'t like Asia!')
else:
    print('Sorry to hear that!')