name ="Yash"
age = 24
#print("My name is",name,"age is ", age)
s='python'
for i in s:
    print(i)

i=100
while i>=1:
    print(i)
    i-=1
print("loop ended")

n=int(input("Enter a number"))
i=1
while i<=10:
    print(n*i)
    i+=1
#TRAVERSE

ls=[2,3,4,5,67,89]
ind=0
while ind<=len(ls)-1:
    print(ls[ind])#ls[0],ls[1],ls[2]
    ind+=1

#SEARCH FOR A NUMBER X IN THIS TUPLE USING LOOP
nums=(2,4,26,16,8,9)
i=0
x=26
while i<len(nums):
    if(nums[i]==x):
        print(i)
    i+=1


