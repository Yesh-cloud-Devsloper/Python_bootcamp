#WAP to stop the user input whne it is 0
while True:
    num=int(input("Enter a number:"))
    if num==0:
        break
    print(num)

#WAP to search a number in given list
l=[10,20,30,25,40,55]
x=25
for i in l:
    if i==x:
        print("found")
        break
    print(i)

#WAp to print even numbers from 1 to 100 and skip mutliples of 3 and 25
for i in range(2,30,2):
    if i%3==0:
        continue
    print(i)

#WAP to check the first character is vowel or not
s='eight'
for i in s:
    if i in 'aeiou':
        print(i)
        break
    else:
        print("not a vowel")

#WAP to print even numbers from 1 to 100 with multiples of 12.
for i in range(1,101):
    if i%12==0:
        break
    print(i)
    
