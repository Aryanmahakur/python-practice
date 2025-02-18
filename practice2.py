#q1
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))

# print(f"Name: {name} Age: {age} Height: {height} Weight: {weight}")

#q2
# a=0
# while a<=100:
#     if(a%3==0 and a%5==0):
#      print(a)
#     a +=1
#3
#4

# a = 0
# Input = [10, 20, 5, 8, 50]

# # Initialize max_val and second_max_val
# max_val = float('-inf')
# second_max_val = float('-inf')

# while a < len(Input):
#     print(Input[a])
#     if Input[a] > max_val:
#         second_max_val = max_val
#         max_val = Input[a]
#     elif Input[a] > second_max_val and Input[a] != max_val:
#         second_max_val = Input[a]
#     a += 1

# print(f"The second maximum value is {second_max_val}")

# num = 5
# factorial = 1

# while num > 0:
#     factorial *= num
#     num -= 1

# print(f"The factorial of 5 is {factorial}")
   

    
lists = [10, 50, 40, 30, 80]
max_val = lists[0]
a = 0

while a < len(lists):
    if max_val < lists[a]:
        max_val = lists[a]
    a += 1

print("max value is", max_val)