'''
Explain Exception handling? What is an Error in Python?
Exception handling is a way to respond to unexpected events using
try and except in python. There are two errors type:logical and syntax errors
'''

'''
How many except statements can a try-except block have? 
Name Some built-in exception classes:
 At least one except statements. Here are few built-in exceptions:valueerror,
 keyerror,Indexerror,ZeroDivisionError,etc.
'''
'''
When will the else part of try-except-else be executed?
The else part of try-except-else is executed when no exception happens.
'''
'''Can one block of except statements handle multiple exception?
 Yes. one block of except statements can handle multiple exceptions.
 
'''

'''When is the finally block executed?
Finally block is always executed after try/except.
'''

'''How Do You Handle Exceptions With Try/Except/Finally In Python? 
Explain with coding snippets'''
#try block
try:
    a=1
    b="f"
    mul=1*b
    #except if it is different output than try
except:
    print("Invalid input")

else:
    print("Welcome")

#finally will always occur regardless of the output. 
finally:
    print("Thank you for using the application")


'''What happens when "1"== 1 is executed?
It gives a false.
'''
'''Write python program that user to enter only odd numbers, 
else will raise an exception.'''

#user defined exception
class EvenException(Exception):
 pass

try:
    #accept odd numbers from user
    num1= int(input("Enter only odd numbers:"))
    #check condition
    if num1%2!=0:
        print("Odd Number")
    else:
     #raise exception
     raise EvenException
    
    
except EvenException:
    print("User input is even number")
    
#Tasks
'''
Accept a number from a user raise exception if user enter below zero value
'''
#user defined Exception
class belowZero(Exception):
   pass

#user input
num= int(input("Enter a number:"))

try:
   #check condition
   if num>0:
      print("postive")
   else:
   #raise exception
    raise belowZero

except belowZero:
   print("Your number is below zero")


#compare two numbers and raise a exception if first number is smaller than second number

#user defined Exception
class compare_Number(Exception):
   pass
#user input
num1=int(input("Enter a number1:"))
num2=int(input("Enter a number:"))

try:
   #check condition
   if num1<num2:
      print("num2 is greater")
   else:
      #raise exception
      raise compare_Number
except compare_Number:
   print("Num1 is smaller than num2")
      

