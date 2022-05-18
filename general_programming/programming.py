"""factorial programming"""
# def factorial(num):
#     if num==1:
#         return num
#     else:
#         return num*factorial(num-1)
# print(factorial(5))

"""palindrome number"""

# xyz=int(input("enter a number"))
# reverse=0
# temp=xyz
# while temp!=0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp=temp//10
# if reverse==xyz:
#     print('this is palinfrome number')
# else:
#     print("this is not a palindrome number")

"""fibonacci series"""
# fibo=int(input("enter a number"))
# def fibonacc(num):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,num):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fibonacc(fibo)


"""armstrong number"""

# arm_input=int(input('enter a number'))
# sum=0
# temp=arm_input
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if sum==arm_input:
#     print("this is an armstrong number")
# else:
#     print("this is not an armstrong number")


"""leap year"""
# leap_year=int(input("enter  yaer"))
# if (leap_year%4==0):
    
#     if (leap_year%100==0):
        
#         if(leap_year%400==0):
#             print("this is leap yeare")

#         else:
#             print("this is not a lepo year")
#     else:
#         print(" a leap year")
# else:
#     print("not a leap year")


"""swapping a number"""
# a=10
# b=20
# a,b=b,a
# print(a,b)

# a=10
# b=65
# a=a+b
# b=a-b
# a=a-b
# print("new  value of a:{}".format(a))
# print("new value ojf b:{}".format(b))

# a=20
# b=90
# temp=a+b
# b=temp-b
# a=temp-a
# print("new value of a:",a)
# print("new value of b:",b)


"""finding occurence of character"""

# str1=str(input("enter a string  --> "))
# char1=str(input('enter a character for counting occurence --> '))
# a=0
# count=0
# for i in range(len(str1)):
#     if (str1[i]==char1):
#         count=count+1
# print(count)

"""finding the middle character of string"""

# str2=str(input('enter a string --> '))
# if len(str2)%2==0:
#     print(str2[len(str2)//2-1]+str2[len(str2)//2])
# else:
#     print(str2[len(str2)//2])

"""reversing a string without using in-built function"""
# str=(input("enter a string"))
# for i in range(len(str)-1,-1,-1):
#     print(str[i],end="")


""" pattern programmin"""


# n=int(input("enter a number"))
# for i in range(1,n):
#     for  j in range(i):
#         print("*" ,end="")
#     print('\r')


# n=7
# m=0
# for i in range(0,n+1):
#     for j in range(0,(n-i)+1):
#         print(end="")
#     m=m-1
#     for j in range(0,2*i-1):
#         print("*",end="")
#         m=m+1
#     m=0
#     print('\r')


# def factorial(nnum):
#     if nnum<=1:
#         return nnum
#     else:
#         return nnum*factorial(nnum-1)
# print(factorial(6))


# def fibonacci(num):
#     if num==0:
#         return num
#     elif num==1:
#         return num
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)
# print(fibonacci(8))



# var=11
# if var>1:
#     for i in range(2,(var//2)+1):
#         if var%i==0:
#             print("this is not prime number")
#             break
#     else: 
#         print("this is prime number")
# else:
#     print("this is not prime number")


# strin="my name is mohd hujaifa"
# str=strin.split()
# acd=list(reversed(str))
# print(" ".join(acd))



# var=121
# reverse=0
# temp=var
# while temp>0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp=temp//10
# if var==reverse:
#     print("this is palindrome number")
# else:
#     print("this is not palindrome number")


# string="Hujaifaq"
# if len(string)%2==0:
#     print(string[len(string)//2-1]+string[len(string)//2])    
# else:
#     print(string[len(string)//2])
        

# stri="sayyed"
# for i in range(len(stri)-1,-1,-1):
#     print(stri[i],end="")

# string=input("enter a string")
# char=input('enter a characater')
# a=0
# count=0
# for i in range(len(string)):
#     if (string[i]==char):
#         count=count+1
# print(count)


abc="MOhd hujaifa saidaha urraon allahabasd"
word=abc.split()
reversing=list(reversed(word))
joining=" ".join(reversing)
print(joining)    