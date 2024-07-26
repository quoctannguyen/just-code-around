'''The Love Calculator script calculates the compatibility score between two partners based on their names. 
Users input their names, and the script counts occurrences of specific letters that spell "TRUE" and "LOVE."
It then combines these counts to create a score, interpreting the score to output a compatibility message. 
The code uses basic string manipulation, arithmetic operations, and conditional statements to determine and display the result.
'''
print("The Love Calculator is calculating your score... ")
name1 = input("Enter your name: ")
name2 = input("Enter your partner: ")

sum_of_name = name1 + name2 
lower_sum_of_name = sum_of_name.lower()
t = lower_sum_of_name.count("t")
r = lower_sum_of_name.count("r")
u = lower_sum_of_name.count("u")
e = lower_sum_of_name.count("e")

first_digit = t + r + u + e 

l = lower_sum_of_name.count("l")
o = lower_sum_of_name.count("o") 
v = lower_sum_of_name.count("v")
e = lower_sum_of_name.count("e")

second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"your score is {score}, you go together like coke and mentos.")
elif (score >= 40) or (score <= 50):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")



