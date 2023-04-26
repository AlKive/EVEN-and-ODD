# BABIERA,ALEXA | CMPE-103-MODULE-2-FILE-HANDLING-IN PYTHON | PROGRAMMING EXERCISE 1
# P-1( 25 points). Write a Python program that reads a text file named numbers.txt that contains 20 integers.
# The program will create two other text file;
# The first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt.
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt

# import the necessary module
from pyfiglet import figlet_format
import pygame
from termcolor import colored
import pyfiglet
from colorama import Back, Fore, Style, init
import time

# formatting the header
art = figlet_format(" ODD or EVEN?", font='digital', width=250)
c_art = colored(art, 'yellow')

print(Fore.LIGHTCYAN_EX + "┏━━━━━༻❁༺━━━━━┓" * 7)
for line in c_art.split("\n"):
    print(line.center(80))
print(Fore.LIGHTCYAN_EX + "┗━━━━━༻❁༺━━━━━┛" * 7)

# OPEN file (numbers.txt,even.txt,odd.txt) as write
with open("number.txt", 'w') as Number_File, open("even.txt", 'w') as Even_Number, open("odd.txt", 'w') as Odd_Number:

    # GET user input (20 numbers/Integers) and store it in numbers.txt file
    for i in range(20):
        user = input(Fore.LIGHTBLUE_EX + "Enter a number: " + Fore.YELLOW)
        Number_File.write(str(user) + "\n")

with open("number.txt", 'r') as Number_File, open("even.txt", 'w') as Even_Number, open("odd.txt", 'w') as Odd_Number:
    # LOOP the lines in number.txt file
    for line in Number_File:
     # ASSIGN each line from number.txt as an integer variable
        Number = int(line)

        # CHECK if Number is EVEN
        if Number % 2 == 0:
            # APPEND the Number to even.txt file
            Even_Number.write(str(Number) + "\n")

        # CHECK if Number is ODD
        elif Number % 2 != 0:
            # APPEND the Number to odd.txt file
            Odd_Number.write(str(Number) + "\n")
        
print("Checking the numbers...")
time.sleep(3)
with open("even.txt", 'r') as Even_Number :    
  even = Even_Number.read().split('\n')  
#DISPLAY the numbers in even.txt and odd.txt file  
  print("Even Numbers: " + str(even))
with open("odd.txt", 'r') as Odd_Number:  
  odd = Odd_Number.read().split('\n')  
  print("Odd Numbers: " + str(odd))         
