

# Python bitwise operators
a = 0b11110000
b = 0b11001100

# binary operation 
# For Bitwise & ('and' operations) - only '1' and '1' would be '1'
bin(a&b)
'0b11000000'

# For Bitwise | ('or' operations) - only '0' and '0' would be '0'
bin(a|b)
'0b11111100'

# For Bitwise ^ ('xor' operations) - both are '1' would be '0' - both are '0' would be '0'. (The two missing '0' are not shown as they are '0's in the beginning)
# Thi is the case that if both are equals number then '0'
bin(a^b)
'0b111100'

# For Bitwise >> ('Right Shift' operations) - Shifting value of 'b' three steps
# 0b11001100 = 204
# 0b---11001 (Moving the 'b' three steps from the lst to the right)
# 0b11001 = 25
bin(b>>3)
'0b11001'

# For Bitwise << ('Left Shift' operations) - Shifting/adding three '0's at the end of the 'b' value.
# 0b11001100 = 204
# 0b11001100000 =  1632
bin(b<<3)
'0b11001100000'
