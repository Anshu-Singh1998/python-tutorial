# let us c
# An Insurance company follows following rules to calculate premium.
# (1) If a person's health is excellent and the person is between 25 and 35 years of age
# and lives in a city and is a male then the premium is Rs.4 per thousand and his policy
# amount cannot exceed Rs.2 lakhs.

# (2) If a person satisfies all the above conditions except that the sex is a female
# then the premium is Rs.3 per thousand and her policy amount cannot exceed Rs.1 lakhs

# (3) If a person's health is poor and the person is between 25 and 35 years of age
# and lives in a village and is a male then the premium is Rs.6 per thousand and
# his policy cannot exceed Rs.10,000.

# (4) In all other cases the person is not insured.

# Write a program to output whether the person should be insured or not,
# his/her premium rate and maximum amount for which he/she can be insured.
pers_health = (input("Enter excellent, poor:"))
age = int(input("Enter age:"))
sex = (input("Male, female:"))
location = (input("Enter city, village:"))
if pers_health == 'excellent' and location == 'city' and sex == 'male' and age >= 25 or age <= 35:
    print("\nThe Premium Is Rs.4 Per Thousand And His Policy Cannot Exceed Rs.2 Lakhs")
elif pers_health == 'excellent' and location == 'city' and sex == 'female' and age >= 25 or age <= 35:
    print("\nThe Premium Is Rs.3 Per Thousand And Her Policy Cannot Exceed Rs.1 Lakhs")
elif pers_health == 'poor' and location == 'village' and sex == 'male' and age >= 25 or age <= 35:
    print("\nThe Premium Is Rs.6 Per Thousand And Cannot Exceed Rs. 10,000")
else:
    print("\n not Insured")
