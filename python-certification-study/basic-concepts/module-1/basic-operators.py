#    +   Addition 	      x + y 	
#    -   Subtraction 	  x - y 	
#    *   Multiplication   x * y 	
#    /   Division 	      x / y 	
#    % 	 Modulus 	      x % y 	
#    **  Exponentiation   x ** y 	
#    //  Floor division   x // y


# standart Addition
print(4 + 5)


# standart Subtraction
print(9 - 3)

# standart Multiplication
print(4 * 5)

# standart Division
print(6 / 2)

# Division with retuning the lowest rounded
print(7 // 2)

# Modulus Division
print(7 % 2) # return the remander of the devision

# power operator (Exponentiation)
print(2 ** 3) # the same as: 2 * 2 * 2 = 8


# print with variables (integer, float) using operators
income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')