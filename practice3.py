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