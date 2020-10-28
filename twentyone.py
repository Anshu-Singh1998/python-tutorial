# let us c
# Any character is entered through the keyboard , write a program to determine whether
# the character entered is a capital letter, a small case letter, a digit or a special symbol.
ch = input("Enter a character:")
if ord(ch) >= 65 and ord(ch) <= 90:
    print("UPPERCASE")
elif ord(ch) >= 97 and ord(ch) <= 122:
    print("lowercase")
elif ord(ch) >= 48 and ord(ch) <= 57:
    print("Number")
else:
    print("Symbol")

