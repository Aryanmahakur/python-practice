# import re

# def is_strong_password(password):
#     # Check if the password is at least 8 characters long
#     if len(password) < 8:
#         return False
    
#     # Check if the password contains at least one uppercase letter
#     if not re.search(r'[A-Z]', password):
#         return False
    
#     # Check if the password contains at least one lowercase letter
#     if not re.search(r'[a-z]', password):
#         return False
    
#     # Check if the password contains at least one digit
#     if not re.search(r'[0-9]', password):
#         return False
    
#     # Check if the password contains at least one special character
#     if not re.search(r'[!@#$%^&*]', password):
#         return False
    
#     return True

# # Example usage
# print(is_strong_password("Password123!"))  # This will print: True
# print(is_strong_password("weakpass"))      # This will print: False # This will print: False
#
# s = "aryan"
# reversed_s = s[::-1]
# print(reversed_s)  # This will print: "nayra" # This will print: "nayra"

# def fac(num):
#     fact = 1
#     for i in range(1, num + 1):
#         print(i)
#         fact *= i  # Multiply numbers from 1 to num
#     return fact  # Return the factorial result

# # Example usage
# result = fac(5)  
# print(result)  # Output: 120

# a = "aryan"
# av = 0

# for i in range(len(a)):
#     if a[i] in "aeiou":  # Check if the character is a vowel
#         av += 1
#     print(a[i])
    
# print(av)
# zero =0
# list1 = [1, 2, 3, 4, 5,0,2,4,0]

# for i in list1:
#   if i == 0:
#     zero += 1
# print(zero)  # Output: 1

# num ={1,2,3,4,5,6,7,8,9,10}
# sum=0
# for i in num:
#     sum +=i
#     print(sum)

# print(sum)  # Output: 55

# list2=[1,2,3,4,5,6,7,8,9,10,"aryan"]
# list2[10] = "hey"
# print(list2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hey']
# list2.append("hey")
# print(list2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'aryan', 'hey']
 
# message = "hey how are you hope you doing fine click on this link to get 1000$ and make money"

# for word in message.split():
#     if word == "click":
#         print(word ,"found spam")
#         break
    
# # Output: spam hey
# subjectfail = 0
# marksub1 = int(input("Enter your mark for subject 1: "))
# marksub2 = int(input("Enter your mark for subject 2: "))
# marksub3 = int(input("Enter your mark for subject 3: "))
# subject = int(input("Enter the number of subjects: "))

# total_marksobtained = marksub1 + marksub2 + marksub3
# total_marks = 100 * subject
# total_percentage = (total_marksobtained / total_marks) * 100

# if total_percentage > 33:
#     print("You have passed")
# else:
#     print("You have failed")

# # Check if the student has failed in any subject
# if marksub1 < 33:
#     subjectfail += 1
#     print("You have failed in subject 1")
# if marksub2 < 33:
#     subjectfail += 1
#     print("You have failed in subject 2")
# if marksub3 < 33:
#     subjectfail += 1
#     print("You have failed in subject 3")

# print(f"Total subjects failed: {subjectfail}")

# n = 1
# m = 5
# while n <= 10:
#     print(f"{m} * {n} = {m * n}")
#     n += 1
# n=10
# m=5
# while n>0:
#     print(f"{m} * {n} = {m * n}")
#     n -=1
# Open the file in read mode
# Open poem.txt in read mode
with open("poem.txt", "r") as file:
    content = file.read()  # Read the entire content of the file
    print(content)  # Print it to the console
content = content.replace("donkey", "#")  # Replace the word "donkey" with "#"
# Open the file in write mode
with open("poem.txt", "w") as file:
    file.write(content)  # Write the modified content to the file
