# From internet
# Write a program to insert a new item in the given array before the second element.
from array import *
num = list("i",[1, 0, 4, 8, 6])
print("This is the existing list: "+str(num))
print("Insert new element before 0:")
num.insert(1, 3)
print("New list is:"+str(num))
