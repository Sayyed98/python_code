"""Data Type represents the type of data present inside a variable.
 In Python we are not required to specify the type explicitly. Based on value provided,
the type will be assigned automatically.Hence Python is dynamically Typed Language.
Python contains the following inbuilt data types
1) Int
2) Float
3) Complex
4) Bool
5) Str
6) Bytes
7) Bytearray
8) Range
9) List
10) Tuple
11) Set
12) Frozenset
13) dict 
14) None"""

# finding the type of data types basically we use type() built in function .
# finding the address of object we use id() built in function

# int data types 
# abc=123
# print(abc)
# print(type(abc))

# av=0

# a=bin(av)
# print(type(a))
# print(a)
# abc=0o11
# print(bin(abc))
# c=oct(av)
# print(c)
# print(type(c))
# d=hex(av)
# print(d)


# float data types

# c=1.2e3
# print(c)
# print(type(c))

# f=1.255
# print(f)

# complex  types values 
# a=10 +2.6j
# print(a)
# print(type(a))

# a=200
# b=20
# print(a>20)
# print(a<b)
# c=a!=b
# print(type(c))

# y=a==b
# print(y)

# string in python

# a="""mohd hujaifa
#     mohd anees
#     kahkashan begum"""
# print(a)    


#  bytes data types
# bytes data types represents the group of bytes number just like an array 
# bcm=[10,50,32,200,1]
# print(type(bcm))
# b=bytes(bcm)
# print(b)
# print(type(b))
# for i in b:
#     print(i)

# bytearray data types
# bytearray same as bytes data types but different is its elements can be change.


# xyz=[120,251,120,255]
# ck=bytearray(xyz)
# for i in ck:
#     print(i)

# print(ck[1])
# ck[2]=12
# print(ck,)
# list data types

# abc=["hujiafa","sayyed",123,14,56]
# print(abc)
# print(abc[2])
# print(abc[-1])
# print(abc[::--1])

# for i in abc:
    # print(i)

# abc.append("last element")
# print(abc)
# abc.extend("badshah")
# print(abc)

# abc.remove(56)
# print(abc)
# print(len(abc))
# bx=abc.count('a')
# print(bx)
# print(abc.index(14))

# abc2=[1123,456,789,2123,55]
# print(abc+abc2)

# print(abc2*3)

# tuple data types 

# abc_tuple=("hujaifa",'anis','saidahan','utraonnnnn','anis')

# print(type(abc_tuple))
# print(abc_tuple.count('anis'))
# print(abc_tuple.index(123456))
# print(len(abc_tuple))

# print(min(abc_tuple))
# print(sorted(abc_tuple))

"""range data types"""
# r=range(10)
# for i in r:
#     print(i)

# even=range(10,20)
# for i in even:
#     if i%2==0:
#         print(i)

# student=range(20,56,2)
# for i in student:
    # print(i)

# odd=set((9,15,3,57,69,23,21,3,65,95))
# print(type(odd))
# print(odd)

# abc={1,23,4,5,6,3,95}
# print(type(abc))

# print(odd.union(abc))

# print(odd.intersection(abc))
# print(odd.difference(abc))

"""frozenset data type"""
# set={12,56,32,59}
# print(set)
# s=frozenset(set)
# print(type(s))
# print(s)
# dictionary={1:2,3:4,5:67}
# print(dictionary)
# print(type(dictionary))

# dictionary={'1':'mohd',2:'hujaifa'}
# print(dictionary)

# dictionary2={1:{'firstname':"mohd","lastname":"hujaifa"},2:["address" ,"allahabad"]}
# print(dictionary2)
# dictionary2[0]="adding"
# print(dictionary2)
# print(dictionary2.values())
# print(dictionary2.keys())


# dictionary2[1]]="saidahan"
# print(dictionary2)


"""none data type"""
# def m1():
#     a=10
# print(m1())

"""ternary operator or conditional operator"""
# a=100
# b=20
# m=a if a>b else b
# print(m)

# read two values from the keyboard and print minimum value
# input1=int(input("enter a number1"))
# input2=int(input("enter number2"))
# min= input1 if ]input1<input2 else input2
# print("minimum value is :",min)

"""special operator"""

# a=10
# b=10
# print(id(a))
# print(id(b))
# print(a is not b)
# print(a is b)
# list1=['one','two','three']
# list2=['one','two','three']
# print(id(list1))
# print(id(list2))
# print(list1 is list2)
# print(list1 is not list2)

# list4=1,2,3
# list5=1,2,3
# print(id(list4))
# print(id(list5))
# print(list4 is list5)

# """membership operator"""
# """ 'in' and 'in not' """
# x="hello world th]is is the programming language "
# print("worlds" in  x)
# print("world" in x)
# print("hujaifa" not in  x)


"""operator precedence """
"""
1. parenthesis ()
2. ** exponential operator
3. ~ , -  bitwise complement operator, unary minus operator 
4. *,/,%,//  multiplication, division, modulo,floor division
5. +,-  addition , substraction
6. <<, >> left shift]], right shift
7. & bitwise And
8. ^  bitwise xor
9. | bitwise or 
10. relational or comparision operator
11. assignment operator
12. identity operator
13. membership operator 
14. logical not
15. logical and 
16. logical or
"""


# a=20 
# b=3
# c=56
# d=23
# e=52
# print((a**b)/e-c*d%e)

# x=2**3(5/9+3)-569
# print(x)

# x=123.9654
# y=int(x)
# print(y)
# bool=True
# z=int(bool)
# print(z)


# a=10
# b=20
# c=20
# print(c&b)
# print(a|b)
# print(a^b)
# print(~a)

# print(a<<b)
# print(a>>b)
# print(10<<2)
# print(10>>2)

# import math
# print(math.sqrt(36))
# print(math.pi)
# print(math.ceil)

# from math import sqrt,pi
# print(sqrt(16))
# print(pi)

# find the area of circle
# from math import pi
# r=16

# print("area of circle is :",pi*r**2)

""" reading multiple value from the keyboard in a single line """
# a,b=[int(x) for x in input("enter 2 numbers:").split()]
# print("product is :",a*b)
# abc=eval("10+20")
# print(abc)

# x=eval(input("enter a expression"))
# print("expression is the :",x)

# name="Mohd Hujaifa"
# Age=25
# salary=35000
# print("employee name is {0} and age is {1} and lastly salary is {2}".format(name,Age, salary))


""" conditional statements"""
from inspect import classify_class_attrs
from re import A
from tkinter.messagebox import NO
from turtle import speed


# a=10
# if a%2==0:
#     print("this is even numver")

# b=20
# if b>10:
#     print("this is greater number")
# else:
#     print("this is less number")

# ch='i'
# if ch=='a':
#     print("this is vowel char")
# elif ch=='e':
#     print("this is vowel char")
# elif ch=='i':
#     print("this is vowel")
# elif ch=='o':
#     print("this is vowel char")
# elif ch=='u':
#     print("this is vowel char")
# else:
#     print('this is consnant')

"""iterative statements 
for loop
"""
# x="mohd hujaifa"
# for y in x:
#     print(y)

# list=eval(input("enter a element of list"))
# sum=0;
# for i in range(list):
#     sum=sum+i
# print("sum of list is ",sum)

# x=12
# for i in range(x):
#     if i==8:
#         print("precessing is enough ")
#         break
# else:
#     print('this is out of range')

""" continue keyword"""
# for i in range(20):
#     if i%2==0:
#         continue
#     print(i)

"""pass keyword"""
# for i in range(7,71):
#     if i%7==0:
#         print(i)
#     else:
#         pass

# x=20
# print(x)
# del x
# # print(x)

# s="hujaifa"
# s=None
# print(s)

"""string"""

# s='hujaifa\'anis'
# print(s)

# s=input("enter a string")
# i=0
# for x in s:
#     print("the index of string is postitive {} and negative {} ".format(i,i-len(s),x))
    # i=i+1


# s="learning python is very very easy!!!"
# print(s[::])
# print(s[2:-10:1])
# print(s[::-1])
# print(s[0::-5])





# s1="Durga Youtube channel is one of the best python tutor"
# print(s+s1)

# main_string=input('enter a string')
# sub_string=input("enter a string")
# if sub_string in main_string:
#     print("string is found in main_string")
# else:
#     print("string is not found in main string")

# main_string=input('enter a string')
# sub_string=input("enter a string")
# if main_string==sub_string:
#     print("both string are same")
# elif main_string>sub_string:
#     print("main string is grater than  sub_string")

# scity=input("enter a city name")
# city=scity.strip()
# if city=="hyderabad":
#     print("hello hyderabadi...adab")
# elif city=='chennai':
#     print("hello madarasi...vanakkam")
# elif scity=="allahabad":
#     print("   hello allahabadi....ka guru" ,city.strip())
# else:
#     print('your entered city is invalid')

# s="  hujailfa anis"
# print(s.strip())

# string="python is very easey language"
# print(string.find("very"))
# print(string.find('java'))

# s="hujaifa"
# y=s.replace("a", "i")
# print(y)
# print(id(s))
# print(id(y))

# s="python is very popular language "
# l=s.split()
# print(l)
# for x in l:
#     print(x)



"LIST DATA STRUCTURE"
# LIST=eval(input("ener a list"))
# print(LIST)
# print(type(LIST))

# lst=[]
# n=int(input("enter number of element"))
# for i in range(0,n):
#     ele=[int(),int(input())]
#     lst.append(ele)
# print(lst)

# list=list(range(0,10,2))
# print(list)
# print(type(list))

# s='learning python is very easy'
# lst=s.split()
# print(lst)

# n=[1,2,4,3,5,6,9,8,7,10]
# i=0;
# while i<len(n):
#     print(n[i])
#     i=i+1






# order1=["chicken","mutton","fish"]
# order2=["ko",'rc','kf']
# order1.extend(order2)
# print(order1)

# n=[10,20,30,40]
# n.remove(20)
# print(n)

# n.pop()
# print(n)



# s={10,20,60,90,50,60}
# print(s.pop())
# s.discard(10)
# print(s)
# print(s.clear())

# x={10,20,50,60,90}
# y={60,50,20,10,8070,70}
# print(x.symmetric_difference(y))



# d={}
# d[100]="Mohd"
# d[200]="Hujaifa"
# d["number"]=8173846711
# print(d)
# print(len(d))
# print(d.clear())
# d={1:"mohd",2:"hujaifa"}
# x={1:"sayyed",2:"sahab"} 
# d1={3:"hujaifa"}
# d.update(d1)
# print(d)

# def f1(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
# f1(3,2)
# f1(10,20,30,40)
# f1()
