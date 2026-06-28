'''
Dictionary-day5
-----------
--->Dict is key  : value pair seperted by :, and keys are unique
-->in the palaece of keys we have use immutable data type...

details_ = {"name" : "harsha",
            1 : "number"(6,7):[1,2]}
print(details_)

Methods
-------
keys()
-->use dto get all  the keys forom the dictionary
sytex -->varible _name keys ()
'''
details_ ={"Name" : "harsha",
"Age" :"22",
"Gender" : "Female"}
print(details_.items())
'''
intersection():
symbol(&)
commenman elementsfrom the both sets
syntax-->set_1.intersection(set_2)

3.items()
---------
-->used to get both key and value in pair
syntex -->varible_name.items()
eg'''
any_ = [22,45,6,7]
print(any_[0])
details_ = {"Name" : "Harsha",
            "Age" : 56,
            "Gender" : "Female"}
print(details_['Name'])
'''
4.clear()
-------
-->'''

details_ = {"Name" : "Harsha",
            "Age" : 56,
            "Gender" : "Female"}
details_.clear()
print(details_)
'''
update
-------
---->'''
details_ = {"Name" : "Harsha",
            "Age" : 56,
            "Gender" : "Female"}
details_.update({"mob" : 123456789})
print(details_)
'''
Set
----
-->set is a collection of unorderd elements that are seperated by ,
--> set is a muttable
-->can remove deupicate value by itself....'''
go = {1,2,3,4,2}
print(go)
'''
methods
-------
1.union() (|)
-->combian the elements from bith set
syntex--> set_.1.union (set_2)
eg
---
'''
go = {1,2,3,4}
so = {4,5,6,7}
print(go | so)
print(go.union(so))

'''
2.intersection () &
-->common element from both sets
-->sytex-->set_1.intersection(set_2)
'''
go = {1,2,3,4}
so = {4,5,6,7}
print(go | so)
print(go.intersection (so))

'''
3. Symmetric Differnert
------------------------
-->all different elements from both sets
syntex--> set_1. Symmetric Differnert(set_2)

'''

go = {1,2,3,4}
so = {4,5,6,7}
print(go | so)
print(go.symmetric_difference(so))
'''
4.Add
-----
-->usd to add new elements into set'''

go = {1,2,3,4}
go.add(5)
print(go)
'''
5.Remove
----------
-->to del the elements from set
'''
go = {1,2,3,4}
go.remove(2)
print(go)
'''
6.pop
------
-->to del the elements from set based on elements
eg
--
'''
go = {1,2,3,4}
go.pop()
print(go)
'''
discart
-------'''
go = {1,2,3,4}
go.discard(4)
print(go)
go = {1,2,3,4}
go.discard(9)
print(go)



















