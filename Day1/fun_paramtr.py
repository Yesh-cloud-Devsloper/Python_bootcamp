##create a function to ADD 2 NUMBERS .
def add(a,b):
    return a+b
result = add(5,3)

print(result)

#create a  function student(name,age) to displaye student details
def student_details(name,age):
    print("Student name is:",name)
    print("Student age is:",age)    

student_details("John",20)

#create a function to calculate rectangel area(length,breadth)
def rectangle_area(length,breadth):
    area=length*breadth
    return area

result = rectangle_area(10,5)
print(result)

#create function to calculate square area(side)
def square_area(side):
    area=side*side
    return area

result = square_area(5)
print(result)

#Create a function largest(a, b, c) to print the largest number.
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

result = largest(10, 20, 15)
print(result)

#employee details
def employee(name,**details):
  print("Emp name ",name)
  for key,value in details.items():
    print(f'{key}=> {value}')

employee('yash',
         age=25,
         city="bbsr",
         sal=260000,
         job='testing')

 #Create a function student(name, course="Python").   If the course is not passed, print "Python" as the default course.
def student(name, course="Python"):
    print("Student name is:", name)
    print("Course is:", course)

student("Akash")
student("Boby", "Data Science")

#Create a function calculate_interest(amount, rate=5).
def calculate_interest(amount, rate=5):
    interest = (amount * rate) / 100
    return interest 

result = calculate_interest(1000, 10)
print(result)

#Create a function employee(name, company="TCS").
def employee(name, company="TCS"):
    print("Employee name is:", name)
    print("Company is:", company)

employee("Alina")
employee("bhasky", "Google")

#Find the sum of numbers
def sum_num(*args):
  sum=0
  for i in args:
    sum+=i
  print(sum)
sum_num(10,54,20,23)

#find the largest number
def largest_num(*args):
  largest=args[0]
  for i in args:
    if i>largest:
      largest=i
  print(largest)
largest_num(10,54,20,23)

#Create a function to print all student names using *args.
def print_student_names(*args):
    for name in args:
        print(name) 

print_student_names("Alice", "Bob", "Charlie")

##count the number of arguments using*args
def count_args(*args):
  count=0
  for i in args:
    count+=1
  print(count)
count_args(10,54,20,23)

# Create a function to display student details using **kwargs
def student_details(**details):
  for key,value in details.items():
    print(f'{key}=> {value}')
student_details(name='yash',
                age=25,
                city="bbsr",
             batch=26)

#Create a function to display employee information using **kwargs.

def emp_details(**details):
  for key,value in details.items():
    print(f'{key}=> {value}')

emp_details(empid=201,
            empname='john',
            sal=100000,
            job='QA')

 #Create a function to print all product details using **kwargs
def product_details(**details):
  for key,value in details.items():
    print(f'{key}=> {value}') 

product_details(product_id=101,
                product_name='Laptop',
                price=50000,
                brand='Dell')

# Create a function to display bank account details using **kwargs
def bank_account_details(**details):
  for key,value in details.items():
    print(f'{key}=> {value}')   
bank_account_details(account_number=123456789,
                     account_holder='Alina',
                     balance=10000,
                     account_type='Savings')    
#Create a function to display any user information using **kwargs  
def user_details(**details):
  for key,value in details.items():
    print(f'{key}=> {value}')
user_details(name='yash',
             age=25,
             city="bbsr",
             batch=26)








