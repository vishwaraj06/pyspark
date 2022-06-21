"""Dictionary has key and values,keys are immutable and values are mutable
{}
"""
mydict={"Name":"Raju","age":23,"Address":"Salem"}
print(mydict)
y=mydict.get("Name")
print(y)
mydict.pop("age")
print("after pop:",mydict)
z=mydict.values()
print("VALUES I DICT:",z)
w=mydict.keys()
print("KEYS IN DICT:",w)
"""NESTED DICT"""
mydict1 = {
  "child1" : {
    "name" : "gowri",
    "age" : 26
  },
  "child2" : {
    "name" : "Asha",
    "age" : 30
  },
  "child3" : {
    "name" : "raj",
    "age" : 28
  }
}
print(mydict1)
c=mydict1.keys()
print(c)
d=mydict1.values()
print(d)