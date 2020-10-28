# let us c
# Using conditional operators determine:
# (1) Whether the character entered through the keyboard is a lowercase alphabet or not.
# (2) Whether a character entered through the keyboard is a special symbol or not.
# a-z    97-122
# symbol 0-47
n = (input("Enter any lowercase alphabet or symbol:"))
if ord(n) > 97 and ord(n) < 122:
    print("lowercase alphabet")
    if ord(n) > 0 and ord(n) < 47 :
         print("Symbol")
    else:
        print("conditions not met!")
else:
    print("conditions not met")



