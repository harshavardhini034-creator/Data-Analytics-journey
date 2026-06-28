'''qurias

procedural language day-1
--------------------
----> this follows a step-by step approach where code is structure into procedure such as function or routines...


OOP's 
-----
----->This is based on concepts of object and class... 

python
------
#1.dynamically typed  
-------------------
--> python know the type of data e are passing to the variable

print(89+67)
num==89
num_2=67
total_=num+num_2
print (id(num))
print (id(num_2))
print(id(total_))

#2. interpreter
-->python execute code line-by-line,  if an error it will stope the execution in that and before will goes the output...

num =89
print(type(num))
num_2=67
total_=num+num_2
print(id(num))
print(id(num_2))

print(total_)

#3.High_level
-------------
int num=89
1991-->guide van Russum intrudes

why use python
---------------
-->easy syntax 
-->cross-platform
-->wide application 
-->Huge library support

Tokens
-------
#1. Keywords 
------------
-->there are reserved word in python 
eg
--
if, else, for, while 

#2.Identifiers
--------------
--.names given to variables, functions ,class  
#3.Literals
-----------
-->89,"hello",4.56

#4.operators
-----------
--> - + * /
#5.Punctuators
--------------
-->(),{},[]
#6. Rules of variable 
--------------------
-->A-Z, a-z
num_1=7
num = 8
Num_2 = 9


special char, number, space 
$num = 0
su@m = 8
S O = 89
num _2 + 9

#comments
1.single line-->
2.muti line-->''' ''',""" """ ...)

num = 9
if num % 2 == 0: # checking a number is even or odd
 print("Even")
else:
 print("Odd")

#Boolean
 
1 True
2 Flase

#python day-2
------------

#operators:

#1 Arithmetic Operator(+, -, *,**, //, %)
a=9
b=12
print(a+b)
print(a*b)
print(a-b)

#2 Asseigment Operator(=, +=, -=, *=, %=,...)
a=8
a+=3 #a= a + 4

#3 comparision Operator(==, !=,<,>=,<,>
a = 10
b = 5

print(a == b)   # False
print(a != b)   # True
print(a < b)    # False
print(a > b)    # True
print(a <= b)   # False
print(a >= b)   # True
#4 Logical Operator

and --> Returns true if both are true..
or  -->Return true if any one is correct 
not -->Reverser the output
a = 10
b = 20
print(a < b and b > 15)
a = 10
b = 20
print(a > b or b > 15)

#5 identity Operator

is  --> same object or not
a = 20
b =20
print(a == b)
print(a is b)
is not --> not the same object
a = 20
b =20
print(a == b)
print(a is not b)

#6 membership Operator

in -->
a =[1,2,3,4,5]
print(2 in a)
not in -->
a =[1,2,3,4,5]
print(20 in a)

#7 Biwise Operator
&, <<, >>,|, ^

print(5 & 4)
print(5 | 3)
print(5>>6)
print(6<<2)
'''

