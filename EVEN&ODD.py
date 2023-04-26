#BABIERA,ALEXA | CMPE-103-MODULE-2-FILE-HANDLING-IN PYTHON | PROGRAMMING EXERCISE 1
#P-1( 25 points). Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; 
# The first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. 
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt

'''PSEUDOCODE
#GET user input (20 numbers/Integers)
#OPEN file (numbers.txt,even.txt,odd.txt) as write
#LOOP the lines in number.txt file
FOR number in Number_File:
  #ASSIGN each line from number.txt as an integer variable
    Number = int(number)
 
  #CHECK if Number is EVEN
  IF Number %2 == 0
      APPEND the Number to even.txt file
 
  #CHECK if Number is ODD
  IF Number %2 != 0
      APPEND the Number to odd.txt file

#DISPLAY the numbers in even.txt and odd.txt file    
          
'''
