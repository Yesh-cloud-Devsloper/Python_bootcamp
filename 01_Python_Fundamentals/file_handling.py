# f=open('C:\\Users\\Acer\\OneDrive\\Desktop\\Python_bootcamp\\Day1\\file1.txt','r')
# print(f.read())
# f.close()

# f=open('sample.txt','w')
# f.write('Welcome to netx class selenium')
# f.close()

# f=open(r'C:\\Users\\Acer\\OneDrive\\Desktop\\Python_bootcamp\\sample.txt','r')
# print(f.read())
# f.close()

# f=open(r'C:\\Users\\Acer\\OneDrive\\Desktop\\Python_bootcamp\\sample.txt','r+')
# f.write('Welcome to netx class selenium')
# f.close()

# with open(r'C:\Users\Acer\OneDrive\Desktop\Python_bootcamp\sample.txt','r') as f:
#     print(f.read())

# #Return the 5 first characters of the file:
# with open(r'C:\Users\Acer\OneDrive\Desktop\Python_bootcamp\sample.txt','r') as f:
#     print(f.read(5))

# with open(r'C:\Users\Acer\OneDrive\Desktop\Python_bootcamp\Day1\file1.txt','r+') as f:
#     print(f.readline())
#     print(f.readline())

# #Loop through the file line by line:
# with open(r'C:\Users\Acer\OneDrive\Desktop\Python_bootcamp\sample.txt','r') as f:
#     for line in f:
#         print(line)

# f=open(r'C:\Users\Acer\OneDrive\Desktop\Python_bootcamp\Day1\file1.txt','a')
# f.write('This is the new line added to the file.')
# f.close()

# with open(r'C:\Users\Acer\OneDrive\Desktop\Python_bootcamp\Day1\file1.txt','r') as f:
#     print(f.read())

# file = open('newfile.txt', 'a')
# file.write('This is the new line added to the file.')
# file.close()

# file=open('newfile.txt', 'a+')
# file.write('This is the second  new line added to the file.')
# file.close()

# with open('newfile.txt', 'r') as file:
#     print(file.read())

# file=open('Treenetra.txt', 'w')
# file.write('Treenetra is a software company that provides innovative solutions for businesses.  ')
# file.close()

# file=open('Treenetra.txt', 'a+')
# file.write("\nTreenetra opening it's new branch in bengaluru.")
# file.close()    

# with open('Treenetra.txt', 'r') as file:
#     print(file.read())

# with open('newfile.txt', 'r') as file:
#     print(file.read())

# file=open('Treenetra.txt', 'a+')
# list=['AI\n','ML\n','Python\n','Playwright\n']
# file.writelines(list)
# file.close()
# print("List of lines written to the file successfully.")

# with open('Treenetra.txt', 'r') as file:
#     print(file.readlines())

# file=open('Treenetra.txt', 'r+')
# print(file.read(5))
# file.close()

# file=open('Treenetra.txt', 'r')
# print(file.readline())
# file.close()

# file=open('Treenetra.txt', 'r')
# print(file.readlines())
# file.close()

# file=open('Treenetra.txt', 'w')
# file.write('Treenetra is opening its new branch in bengaluru.')
# file.close()

# with open('Treenetra.txt', 'r') as file:
#     print(file.read())

# file=open('Treenetra.txt', 'w')
# file.writelines(['Trust ','Truth','Treenetra'])
# file.close()

# #1. create a file name student.txt and erite your name in it.
# file=open('student.txt','w')
# file.write('Student name - Ashish')
# file.close()

# file=open('employee.txt','w')
# file.writelines(['name- debi\n','age- 24\n','city- bbs\n'])
# file.close()

# with open('employee.txt','r') as file:
#     print(file.read())

#Add some 4,5 lines data intoo student.txt file 
# file=open('student.txt','a+')
# file.write('\ndebi has good IQ level')
# file.write('\ni am adding one more line about debi,debi lives in khandagiri,he secured good mark in exam')
# file.close()

# with open('student.txt','r') as file:
#     print(file.read())


#count how many lines are present in the student.txt file 
# file=open('student.txt','r')
# lines=file.readlines()


# file=open('employee.txt','r')
# print(file.readlines())
# file.close()

# file=open('student.txt','r')
# print(file.read(6))
# file.close()


#Storing 10 students name in student file and print only the fifth line 
# file=open('student.txt','w+')
# file.writelines(['dibya\n','raj\n','rahul\n','goutam\n','farid\n','tarun\n','viajy\n','yash\n','jamil\n','deba'])
# file.close()

# with open('student.txt','r') as f:
#     for line in f:
#         print(line)

with open('employee.txt', 'r') as file:
    print(file.read())

# file=open('employee.txt','a')
# name=input("Enter your name- ")
# age=input("Enter your age - ")
# salary=input("Enter your salary -")
# dept=input("Enter your department- ")
# file.writelines(['name\n','age\n','salary\n','dept\n'])
# file.close()

















    














