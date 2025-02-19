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
   

    
# lists = [10, 50, 40, 30, 80]
# max_val = lists[0]
# a = 0

# while a < len(lists):
#     if max_val > lists[a]:
#         max_val = lists[a]
#     a += 1

# print("max value is", max_val)

#pip install and import package

#Text-to-Speech 

# import pyttsx3

# # Get text input from the user
# text = input("Enter the text you want to be spoken: ")

# # Initialize the text-to-speech engine
# sayy = pyttsx3.init()

# # Use the text-to-speech engine to say the user's input
# sayy.say(text)
# sayy.runAndWait()

# Speech Recognition
# import speech_recognition as sr

# # Initialize the recognizer
# recognizerr = sr.Recognizer()

# # Use the microphone as the audio source
# with sr.Microphone() as source:
#     print("Say something...")
#     # Listen for the first phrase and extract it into audio data
#     audio = recognizerr.listen(source)

# try:
#     # Recognize speech using Google Speech Recognition
#     text = recognizerr.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     # Handle the case where the recognizer could not understand the audio
#     print("Sorry, I could not recognize your voice.")
# except sr.RequestError as e:
#     # Handle the case where the recognizer could not reach the Google API
#     print(f"Could not request results from Google Speech Recognition service; {e}")
#generating random jokes
# import pyjokes

# joke = pyjokes.get_joke()
# print("Here's a joke for you:", joke)

#automate mouse and key
# import pyautogui

# pyautogui.moveTo(100, 100, duration=1)  # Move mouse to (100,100)
# pyautogui.write("Hello, Python!", interval=0.1)  # Type text
# import winsound

# frequency = 1000  # Hertz
# duration = 500  # Milliseconds
# winsound.Beep(frequency, duration)

# import requests

# # Make a GET request to the GitHub API
# response = requests.get("https://api.github.com")

# # Print the JSON response from the API
# print(response.json())
# print(response.json())



