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
# fibonacc(9)


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
str=(input("enter a string"))
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")