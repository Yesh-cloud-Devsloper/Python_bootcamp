#List is collection of homogenous data and heterogenous data.
#List is mutable.
#List is ordered collection of data.
#List is defined by using square brackets [].
#List can contain duplicate values
#List can contain any type of data.
#List can contain list as well as tuple and set and dictionary.
#List begins with index 0 and ends with index n-1.

#Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

#Creating a list with different data types
my_list2=[1,"Hello",3.14,True]
print(my_list2)

#Creating a list with duplicate values
my_list3=[1,2,3,4,5,1,2,3]
print(my_list3)

#Creating a list with list as well as tuple and set and dictionary
my_list4=[1,2,3,[4,5],(6,7),{8,9},{"name":"John","age":30}]
print(my_list4[3])

#List slicing
my_list5=[1,2,3,4,5,6,7,8,9,10]
print(my_list5[0:5]) #Slicing from index 0 to 4
print(my_list5[5:10]) #Slicing from index 5 to 9
print(my_list5[:5]) #Slicing from start to index 4
print(my_list5[::2]) #Slicing with step 2

#creating list using list() constructor
my_list6 = list([1, 2, 3, 4, 5])
print(my_list6)