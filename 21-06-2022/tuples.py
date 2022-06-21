print("######################## TUPLES ####################################")
"""tuples are immutable and it can also contain different data types.represented inside ().
A tuple is a collection which is ordered and unchangeable.

Two built-in methods
count()	Returns the number of times a specified value occurs in a tuple
index() Searches the tuple for a specified value and returns the position of where it was found
"""

tup=(1,2,3,4,2,3,5,"A","raju")
print(tup)
x=tup.count(2)
print("COUNTING:",x)
tup1=(1,2,3,4,5,6,7,8)
y=tup1.index(7)
print("INDEXING:",y)
tup2=(1,2,3,4,5,"RAJU")
z=tup2.index("RAJU")
print("INDEXING:",z)