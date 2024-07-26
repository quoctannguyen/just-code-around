height = input("height: ")
weight = input("weight: ")
height_as_float = float(height) 
weight_as_float = float(weight)
BMI = weight_as_float / (height_as_float ** 2)
BMI_as_int = int(BMI)
print(BMI_as_int)
# or 
print("BMI: " + str(BMI_as_int))     
# the final print statement is trying to concatenate a string and an integer directly, which will cause an error.

