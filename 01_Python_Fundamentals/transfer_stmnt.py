# Transfer Statement in Python
# break
# continue
# pass
#take number from user continously. stop whenn the number becomes 00

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    print( number)
#print all even numbers 1 to 30 but skip mutliples of 3 and stop when the number reaches 25
for i in range(2,30,2):
    if i%3==0:
        continue
    print(i)