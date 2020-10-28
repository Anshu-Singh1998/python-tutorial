# let us c
#  A certain grade of steel is graded according to the following conditions:
# (1) Hardness must be greater than 50
# (2) Carbon content must be less than 0.7
# (3) Tensile strength must be greater than 5600
# The grade are as follows:
# Grade is 10 if all three conditions are met
# Grade is 9 if conditions (1) and (2) are met
# Grade is 8 if conditions (2) and (3) are met
# Grade is 7 if conditions (1) and (3) are met
# Grade is 6 if only one condition is met
# Grade is 5 if none of the conditions are met

# write a program which will require the user to give values of hardness, carbon content
# and carbon content and tensile strength of steel under consideration and output the
# grade of the steel.
hardness = int(input("Enter hardness :"))
Carbon_content = float(input("Enter carbon content:"))
Tensile = int(input("Enter tensile strength:"))
if hardness > 50 and Carbon_content < 0.7 and Tensile > 5600:
    print("Grade 10")
    if hardness > 50 and Carbon_content < 0.7:
        print("Grade 9")
        if Carbon_content < 0.7 and Tensile > 5600:
            print("Grade 8")
            if hardness > 50 and Tensile > 5600:
                print("Grade 7")
                if hardness > 50 or Carbon_content < 0.7 or Tensile > 5600:
                    print("Grade 6")
                else:
                    print("Grade 5")
            else:
                print("Not met")
        else:
            print("Not met")
    else:
        print("Not met")
else:
    print("Not met")
