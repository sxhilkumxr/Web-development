weight = 75
height = 167

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5 : 
    print("underweight")
elif bmi >=18.5:
     print(" normal weight")
elif bmi<25:
    print("normal weight")
else:
    print("overweight")
    