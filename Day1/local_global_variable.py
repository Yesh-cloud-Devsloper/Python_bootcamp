x=5 #global varaible
def my_func():
    y=50#local variable
    print("local variable:",y)
    print("global variable:",x) 

my_func()
print("global variable:",x)
# print("local variable:",y) #this will give error because y is local variable and can not be accessed outside the function   
