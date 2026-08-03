larg= lambda a,b: a if a>b else b
print(larg(10,20)) 

#check number is even or odd using lambda function
even_odd= lambda num: "Even" if num%2==0 else "Odd"
print(even_odd(10))
print(even_odd(15))

cube=lambda num: num**3
print(cube(3))

largest=lambda a,b,c: a if a>b and a>c else b if b>a and b>c else c
print(largest(10,20,15))

#reverse every string in a list using lambda function
strings = ["hello", "world", "python"]
reversed_strings = list(map(lambda s: s[::-1], strings))
print(reversed_strings) 

#cube of every number in a list using lambda function
numbers = [1, 2, 3, 4, 5,6,7,8,9,10]   
cubes = list(map(lambda x: x**3, numbers))  
print(cubes)

#use a lambda function to print the cube of numbers from 1 to 18
cubes = list(map(lambda x: x**3, range(1, 19)))
print(cubes)    

#from a list of words , calculate each word's length using lambda function,keep lenghts greter than 4 then find the maximum length using lambda function    
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)
max_length = max(map(lambda word: len(word), long_words))
print(max_length)
