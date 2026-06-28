'''
Datatypes 
---------
int--> num
string 
------
-->strig  is sequence of char that are enclosed in (' ' , " """ """ )
-->String is immutable 
Concatination 
-------------
-->Here ,the (+) operator act as to concetinate more then 2 string....

so = "python'
any_ = "is a language"
print(so +any_)
 
indexing
--------
-->this is used to access the particulre char iin the string by pass index postition value 
-->Index start from 0....--.we have negative indexing to count position from last to first .....
so =  "python  is a language"
print(so[12])
print(so[-2])

Methods 
-------
1.replace ()
--> This method is used to change any substring in that particular string 
so = "python is a language"
print(so.replace ("python","Java"))
syntex--> variable_name d.replae("old string ","new string ",count)
so = "python is a language"
print(so.replace ("a","A",2))


2.join()
--------
-->This method used to add a new substring after each char in the string....
syntex-->"string".join(varible_name)
so ="python is language"
print("$".join(a))

3.split()
---------
--->This method can divide the string into different index into list, based on the string pass by us .....
synetx -->variable _name.slipt ('substring')
eg...
so ="python is language"
print(so.split(" "))
print (so.split("is"))

4.count()
---------
-->used too count the substring in the particular string and also specify the index postion
sytex-->variable name.count ("substring ",start index, ending)
eg....
so ="python is language"
print(so.count("a",0,12))

string bulit-in function 
------------------------
len()
-----
-->This will find the length of the string, which is numbers char present in the string....
eg
so ="python is language"
print(len(so))

max()
----
-->will get the max char in the string 
so ="python is language"
min
----
will get the min char in the string...
'''
