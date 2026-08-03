#conditonal statements in python
#syntax(if-elif-else)
# You can also apply logical operators such as and, or, and not to combine multiple conditions within a single if statement.

# age=19
# if age>=18:
#     print("You are eligible to vote.")

#if-else statement
age=16
if age>=18:
    print("You can drivea car")
else:
    print("You cannot drive a car")

#if-elif-else statement
# marks=75
# if (marks>=90):
#     print("You got A grade")
# elif(marks>=80):
#     print("You got B grade")
# elif(marks>=70):
#     print("You got C grade")
# else:
#     print("You got D grade")
# print("End of program")

marks = int(input('Enter yourmarks:'))
if(marks>=90):
    grade='A'
elif(marks>=80):
    grade='B'
elif(marks>=70):
    grade='C'
else:
    grade='D'
print("Your grade is:",grade)

#WAP to check whether a number is odd or even.
number= int(input('Enter a number:'))
if(number%2==0):
    print("The number is evenn")
else:
    print("The number is odd") 

#WAPto check wjhether a number is multiple of  7 or not.
numberr= int(input('Enter a number : '))
if(numberr%7==0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7") 

#WAP to find the greates of 3 numbers entered by the user.
num1= int(input('Enter first number: '))
num2= int(input('Enter second number: '))
num3= int(input('Enter third number: '))
if(num1>num2 and num1>num3):
    print("The greatest number is:: ",num1)
elif(num2>num1 and num2>num3):
    print("The greatest nummber is :",num2)
else:
    print("The greatest number is :",num3)

