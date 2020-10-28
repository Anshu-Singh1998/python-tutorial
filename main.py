# exercise from let us c
# Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary,
# and house rent allowance is 20% of basic salary.Write a program to calculate his gross salary.
bs = int(input("enter basic salary:"))
da = (40*bs)/100
print(da)
hra = (20*bs)/100
print(hra)
gs = (bs*12 + da*12 + hra*12)
print(gs)
