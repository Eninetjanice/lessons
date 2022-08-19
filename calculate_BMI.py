# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
my_height = float(height)
my_weight = int(weight)
#check for BMI using the formular BMI = mass.kg/height.m**2
BMI = my_weight / (my_height ** 2)
new_BMI = int(BMI)
print(new_BMI)
