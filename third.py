# let us c
# If the marks obtained by a student in five different subjects are input through the keyboard
# find the aggregate marks and percentage marks obtained by a student.
# Assume each subject is of 100 marks.
english = int(input("Enter marks for english:"))
maths = int(input("Enter marks for maths:"))
geography = int(input("Enter marks for geography:"))
commerce = int(input("Enter marks for commerce:"))
hindi = int(input("Enter marks for hindi:"))
total = 500
aggregate = (english + maths + geography + commerce + hindi)
percentage = (aggregate*total)/100
print(aggregate)
print(percentage)
