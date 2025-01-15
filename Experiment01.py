'''
        Implementing data types like List ,Set ,Tuples and Dictionary
            Name : Antuley Aman Siraj
            Roll No : 23CO25
            Batch - 01


    Theory : Python is a versatile and user-friendly programming language known for its simplicity and ease of use. It provides a variety of built-in data types, including Lists, Sets, Tuples, and Dictionaries, each serving different purposes.
    1) A List is an ordered, mutable collection of elements, which can hold items of different data types.
    2) A Set is an unordered collection that only allows unique elements,making it ideal for eliminating duplicates. 
    3) A Tuple is similar to a List but is immutable, meaning its elements cannot be changed after creation,which       makes it suitable for fixed data. 
    4) A Dictionary is an unordered collection of key-value pairs, where each key is unique, and is particularly useful for representing mappings between objects.
    These data types allow developers to efficiently store, manage, and manipulate data in Python, making it a powerful language for both simple and complex tasks.



'''

##### List #####

print("Implenting the List\n")

l = [] #an empty list
l1 = list() #an empty list

l = [20,10,40,30]
n = int(input("Enter a number to enter inside the list ::"))

l.append(n) #Enters the value at the end of the list
print(l)    #print the list
print("")

l.sort() #This will sort the list in Ascending order
print("The Sorted list is :")
print(l) #print the list
print("")

l.sort(reverse=True) #This will sort the list in Descending Order
print("The Sorted List in Reverse is :")
print(l) #print the list
print("")

x = input("Enter Your Name ::")
l.insert(4,x) #Insert the value at a given index
print(l) #print the list
print("")

print("Removing the element of Index 0 :")
l.pop(0) #Pop the element from the given Index
print(l)
print("")

print("Index Value of the element 10 :")
a = l.index(10) #print the Index value of the Object
print(a)
print("")




##### Set #####

s = set() #a empty set
s1 = {2,4,6,8,10,12} #set1
s2 = {2,3,5,8,9,11}  #set2

print(f"This is Set 1: {s1}")
print(f"This is Set 2: {s2}")
print("")



x = int(input("Enter a value to Add inside the set ::"))
s1.add(x) #Add inside the Set
print(s1) #print the set
print("")

print("The Difference between the two set is ::")
result = s1.difference(s2) #give the differnce between the two set
print(result) #prints the result
print("")

print("Removing the value 11 from set 2:")
s2.discard(11) #removes the value from the set
print(s2)
print("")

print("Intersecting the 2 sets :")
inter = s1.intersection(s2) #Gives us the intersection of both sets
print(inter)
print("")

print("Using the Unio function:")
u = s1.union(s1) #gives us the union of both sets
print(u)
print("")

print("Updating the Set :")
s2.update(s1) #update the values of Set1 as per Set 2
print(s2)
print("")

print("Removing a Value form s1")
s1.pop() #removes the value
print(s1)
print("")

print("Clearing the whole set 1 :")
s1.clear() #Clear the whole set
print(s1) #print the empty set
print("")


##### Tuples #####


t = ("Aman Antuley" , "23CO25" , "Mumbra" , 10 , 9 , 9 , 9 , 8 , 7) #Tuple
t1 = () #an empty tuple
print("The Tuple is :")
print(t) #printing the tuple
print("")

print("Counting the Value of 9 inside of the tuple")
c = t.count(9) #count the number of Element which has occured in the tuple
print(c)

print("Using Index method finding the index value of 10 :") #print the index value of 10
print(t.index(10))



##### Dictionaries #####

d = {
    "Name" : "Aman",
    "Age" : 19,
    "Roll No" : "23CO25"
}

print("Printing the Name :")
a = d.get("Name") #Get the Value which has been stored inside the Key
print(a)
print("")

print("Printing All the items Inside of the list :")
b = d.items() #give the items stored inside the Dictionary
print(b)
print("")

print("Printing Only the Keys inside of the Dictionary :")
c = d.keys() #print all the keys inside of the Dictionary
print(c)
print("")

print("Removing the element fromm the Dictionary :")
d.pop("Age") #Remove the Age from the dictionary
print(d)
print("")

print("Printing only the Values inside from the Dictionary :")
e = d.values() #give only the values inside of the Dictionary
print(e)
print("")

print("Clearing the whole Dictionary :")
a = d.clear() #Clear the Dictionary
print(a)