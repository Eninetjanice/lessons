#program that calculates the number of days, months and years one has to live
#assuming one is to live for a period of 90 years.
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#convert age to int
current_age = int(age)

#declare expected number of years to be 90
years = 90

#calculate number of days left
days_in_yr = 365
days_in_year90 = days_in_yr * years
daysleft = days_in_year90 - days_in_yr * current_age

#calculate number of weeks left
weeksyr1 = 52
weeksyr90 = weeksyr1 * years
weeksleft = weeksyr90 - weeksyr1 * current_age

#calculate number of months left
monthsyr = 12
monthsyr90 = 12 * 90
monthsleft = monthsyr90 - monthsyr * current_age

#print the result
print(f"You have {daysleft} days, {weeksleft} weeks, and {monthsleft} months left.")
