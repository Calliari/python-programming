# When python calcultes the power of a number, it starts from the right 

result = 2 ** 2 ** 3 
# which is:
# 2**3 = 8 
# 2**8 = 256
print(result)

result_two = 2 ** 3 ** 1
# which is:
# 3**1 = 3 
# 2**3 = 8
print(result_two)

result_three = 3 ** 2 ** 2
# which is:
# 2**2 = 4 
# 3**4 = 81
print(result_three)



#==================================================================================================
# The Bit operators are six: [&, |, ~, ^, <<, >>]

# Logical AND (&)
first_bit = 1
second_bit = 0
print(first_bit & second_bit)

# Logical OR (|)
first_bit = 0
second_bit = 0
print(first_bit | second_bit)

# Logical NOT , negation (~) 
print(~0)
print(~1)
print(~2)


# Logical XOR , excluded OR(^) excludedd OR
first_bit = 1
second_bit = 0
print(first_bit ^ second_bit)


# The left-shift operator used with the number one (<< 1) on an integer multiply the integer's value by two.
print(50 << 1)
print(20 << 1)
print(12 << 2)
print(2 << 3)

# The right-shift operator used with the number one (>> 1) on an integer divides the integer's value by two.
print(50 >> 1)
print(20 >> 1)
print(12 >> 2)
