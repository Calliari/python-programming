Question 1:
When the following code is executed and the user provides the following in the console: 5.0

average_rating = input('Please provide your avg rating: ')
print(average_rating * 3)


==============================================================================
Question 2:
Given the following code, what will be the output when the user enters two numbers, first 13 and then 3?

a = int(input('First number: '))
b = int(input('Second number: '))
 
a = a % b
b = b % a
 
print(a, b)


==============================================================================
Question 3:
What is the result of the following expression in Python?

1 // 2 * 3


==============================================================================
Question 4:
What will happen after the following code is run and the user provides the following: boom!

number = int(input('Please provide a number: '))
print(number)


==============================================================================
Question 5:
What is the result of the following division in Python?

1 / 1


==============================================================================
Question 6:


The following piece of code:

print(0.1 + 0.1 + 0.1)

shows 0.30000000000000004  instead of simply 0.3. Why is that?
==============================================================================
Question 7:
What does \n do inside a string passed to the print() function?


==============================================================================
Question 8:
What will happen after running the following code?

first_name = 'John'
print(sep=' - ', 'Your first name is', first_name, 'Welcome!')

# In the code, the keyword sep argument appears before positional arguments, which is why Python will show an error
==============================================================================
Question 9:
What is the output of the following code?

x = 0
y = 1
a = x ^ y
b = x | y
c = x & y
print(a + b + c)

# That's because: 
# a = 0 ^ 1 = 1
# b = 0 | 1 = 1 
# c = 0 & 1 = 0
# Then: a + b + c = 1 + 1 + 0 = 2

==============================================================================
Question 10:
What will be the output of the following snippet?

print(18 >> 1)

# The right-shift operator used with the number one (>> 1) on an integer divides the integer's value by two.
==============================================================================