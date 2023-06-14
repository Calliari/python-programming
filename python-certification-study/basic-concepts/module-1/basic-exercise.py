# 1 - Ask the user to provide their login and native language. Use the following prompts:

# Enter your login: << remember to add a space at the end of this prompt!
# Enter your native language: << remember to add a space at the end of this prompt!

# ========================================================================
# 2 - Then, show the user the following message:

# Your login is {login provided} and you speak {language provided}


##############################################################################
# For example, if the user provides the login h_potter and language British English, show:

# Your login is h_potter and you speak British English

# Watch out for typos: you must show the output in this particular format!


##############################################################################
## Sulution

# Enter your login: << remember to add a space at the end of this prompt!
login_provided = input('Enter your login: ')

# Enter your native language: << remember to add a space at the end of this prompt!
native_language = input('Enter your native language: ')

# Your login is {login provided} and you speak {language provided}
print('Your login is', login_provided, 'and you speak', native_language)



x = 11
y = 4

# 3 = 11 % 4
x = x % y
print(x)

# 3 = 3 % 11
x = x % y
print(x)

# 1 = 4 % 3
y = y % x
print(y)

print(x, y)



magical_number = 3 ** 3
magical_number *= 2.
print(magical_number)