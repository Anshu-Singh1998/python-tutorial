# let us c
# Write a general purpose program to convert any given year into its roman equivalent.
a = int(input("Enter any year:"))


val = [1000, 900, 500, 400, 100,
       90, 50, 40, 10, 9, 8, 5, 4,
       3, 2, 1]
symbol_val = ['M', 'CM', 'D', 'CD', 'C',
              'XC', 'L', 'XL', 'X', 'IX',
              'IIIV', 'V', 'IV', 'III', 'II',
              'I']
roman_num = ''
i = 0
while a > 0:
    for _ in range(a // val[i]):
        roman_num = roman_num + symbol_val[i]
        a = a - val[i]
    i = i + 1

print("year in roman number:", roman_num)
