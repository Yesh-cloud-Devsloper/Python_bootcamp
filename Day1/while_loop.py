#WAP to all even numbers from 1 to 20 using while loop
number=1
while number<=20:
    if number%2==0:
        print(number)
    number+=1

#divided by 3 between 1 to 30 using while loop
number=1
while number<=30:
    if number%3==0:
        print(number)
#WAP to print all numbers between 1 to 30 which are divisible by both 3 and 5 using while loop
number1=1
while number1<=30:
    if number1%3==0 and number1%5==0:
        print(number1) 
    number1+=1

#reverse a string using while loop
text='python'
emp=''
while len(text)>0:
    emp+=text[-1]
    text=text[:-1]
print(emp)

#sum of digits of a number using while loop
num=int(input("Enter a number: "))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
print(sum)

#count the number of digits in a number using while loop
number=543543
count=0
while number>0:
    number//=10
    count+=1
print(count)

#largest digit in a number using while loop
num=5678
lrg=0
while num>0:
    digit=num%10
    if digit>lrg:
        lrg=digit
    num//=10
print("The largest digit is:",lrg)

#smallest digit in a number using while loop
num=int(input("Enter a number: "))
small=num%10
while num>0:
    digit=num%10
    if digit<small:
        small=digit
    num//=10
print("The smallest digit is:",small) 

#divided by 3 and 5 between 1 to 30 using while loop
number=1
while number<=30:
    if number%3==0 and number%5==0:
        print(number)
    number+=1
