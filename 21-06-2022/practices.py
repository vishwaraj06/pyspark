#variables are reserved memory locations to store values
# Python has five standard data types −
# Numbers
# String
# List
# Tuple
# Dictionary
print("###################### INTEGER ###################################")
new="Raj"
print(new)
new1=new2=20
new3=12.09
new5=True
new6=3J
print(new1)
print(new2)
print(type(new1))
print(type(new))
print(type(new3))
print(type(new5))
print(type(new6))
print("################ TYPE CONVERSION ######################################")

print("integer to float:",float(new1))
print("float to integer:",int(new3))
print("int to complex:",complex(new2))

print("##################### STRINGS #################################")

new_str="Hello Raj"
print(new_str)
print("positive index:",new_str[2])
print("index range:",new_str[2:6])
print("reverse of str:",new_str[::-1])
print("negative indexing:",new_str[-3])
print("prints str two times:",new_str*2)
new_str2="Tharun"
new_int=1998
print("Concatination of two strings:",new_str+new_str2)
print("concatination of string and integer is :{}{}".format(new_str2,new_int))

print("######################LIST##################################")
"""list is used to store multiple values using square brackets,list are mutable and list  we can store different types of data,some of the build in methods are

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()   	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()"""

lst1=[1,2,3,4,5,6,"A",12.5,3j]
lst2=["Raj","Tharun"]
print(lst1)
print("INDEXING:",lst1[3])
print("INDEX RANGING:",lst1[2:6])
print("INDEXING AFTER:",lst1[2:])
print("Concatination of two list:",lst1+lst2)
lst2.append("gowri")
print("appending:",lst2)
lst2.remove("Tharun")
print("after removing:",lst2)
lst2.clear()
print("After clear:",lst2)
lst3=lst1.copy()
print("New list3 after copying:",lst3)
x=lst3.count("A")
print("count of particular value:",x)
lst3.extend(lst1)
print("EXTENDING LIST",lst3)
lst3.pop(6)
print("AFTER POP:",lst3)
lst3.remove(3j)
print("AFTER Remove:",lst3)
lst3.reverse()
print("AFTER REVERSE:",lst3)
lst3.sort()
print("SORTING:",lst3)


