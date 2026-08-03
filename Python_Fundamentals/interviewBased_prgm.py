#WAP to print character at even index of a string
text='python'
for i in range(len(text)):
    if i%2==0:
        print(text[i])

text1='pythonprog'
for i in range(0,len(text1),2):
    print(text1[i])

#WAP to reverse a list using for loop
list1=[1,2,3,4,5]
for i in range(len(list1)-1, -1, -1):
    print(list1[i])

#WAp to find the 2nd largest number in a list using for loop    
list2=[1,2,3,4,5]
largest=list2[0]
second_largest=list2[0]
for i in list2:
    if i>largest:
        second_largest=largest
        largest=i 
    elif i>second_largest and i!=largest:
        second_largest=i
print("The 2nd largest number is:", second_largest)

#WAP to replace vowels with * in a string using for loop 
text='high'
vowels='aeiou'
result=''
for i in text:
    if i in vowels:
        result+='*'
    else:
        result+=i
print(result)

#WAP to check wether a number is armstrong number using for loop
num=int(input("Enter a number: "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

#WAP to check wether a number is armstrong number using for loop
num=int(input("Enter a number: "))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==num:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")

#WAP to check wether a number is prime or not using for loop
num=int(input("Enter a number: "))
is_prime=True
if num>1:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

#WAP to find sum of all values in a list using for loop
list3=[1,2,3,4,5]
sum=0
for i in list3:
    sum+=i
print("The sum of all values in the list is:", sum)

tups=(1,2,3,4,5)
small=tups[0]
for i in tups:
    if i<small:
        small=i
print("The smallest number in the tuple is:", small) 

#remove duplicate character  from a list using for loop
text='crickbuzz'
unique=[]
for i in text:
    if i not in unique:
        unique.append(i)
print("The unique characters in the string are:", unique)

#wap to find sum of nested list using for loop
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in nested_list:
    for j in i:
        sum+=j
print("The sum of all values in the nested list is:", sum)  

text='python'
i=0
while i<len(text):
    print(text[i])
    i+=1
#'gf@ed#ca
textt='ac@de#fg' 
#'gf@ed#ca


