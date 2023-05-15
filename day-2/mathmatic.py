# priorities
# 1- ()
# 2- **
# 3- * /
# 4- + -

# print(3 * 3 + 3 / 3 - 3)



height_feet = float(input("print your feet: "))
height_inches = float(input("print your inches: "))
weight_pound = int(input("print your pound: "))

# weight_kilograms = weight_pound / 2.205
weight_kilograms = weight_pound / 2.205

# height_in_inches = (height_feet*12) + height_inches
height_in_inches = (height_feet * 12) + height_inches

# height_meters = height_in_inches / 39.37
height_meters = height_in_inches / 39.37

BMI = weight_kilograms / height_meters ** 2

print("BMI: " + str(int(BMI)))



# BMI = Weight(KG) / Height^2(m^2)
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# bmi = int(weight) / float(height) ** 2
# print("BMI: " + str(int(bmi)))


# priorities
# 1- ()
# 2- **
# 3- * /
# 4- + -

# print(3 * 3 + 3 / 3 - 3)