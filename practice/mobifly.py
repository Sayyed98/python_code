# program of even number

# # prime_input=int(input("enter a nubmer"))
# if prime_input>1:
#     for i in range(2,int(prime_input//2)+1):
#         if prime_input%i==0:
            
#             print("this is not a prime number")
#             break
#     else:
#         print("this is prime number")
# else:
#     print("this is not a prime nubmer")

#sum of even number

# x=8
# count=0
# for i in range(0,x):
#     if (i%2)==0:
#         count=count+i
# print(count)

#factorial program

# abc=int(input('enter a nubmer'))
# def factorial(num):
#     if num==1:
#         return num
#     else:
#         return num*factorial(num-1)
# print(factorial(abc))


#palindrome program

# input_of_pali=int(input('enter a number'))
# reverse=0
# temp=input_of_pali
# while temp!=0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp=temp//10
# if reverse==input_of_pali:
#     print("this is a palindrome number")
# else:
#     print("this is not palindrome number")

# fibonacci series
# input_fibo=int(input("enter a number"))
# def fibonacci(num):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(2,input_fibo):
#         c=a+b
#         a=b
#         b=c
#         print(c)
# fibonacci(input_fibo)

#armstrong number

# input_arm=int(input('enter a number'))
# sum=0
# temp=input_arm
# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10
# if sum==input_arm:
#     print("this is an armstrong number")
# else:
#     print('this is not an armstrong number')


# swapping of two variable value
# a=10
# b=120
# a=a+b
# b=a-b
# a=a-b
# print("new value of a:",a)
# print("new value of b:",b)

#Swapping string using three variable
# a="hujaifa"
# b="anis"
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

#finding middle character of string

# x="hujaif"
# if len(x)%2==0:
#     print(x[len(x)//2-1]+x[len(x)//2])
# else:
#     print(x[len(x)//2])

# reversing a string without using any built-in function
# x="sir sayyed mohd hujaifa"
# for i in range(len(x)-1,-1,-1):
#     print(x[i],end='')

# leap year
# x=int(input('enter a year'))
# if x%4==0:
#     if x%100==0:
#         if x%400==0:
#             print("this is leap year")
#         else:
#             print("this is not leap year")
#     else:
#         print("this is  a leap year")
# else:
#     print('this is not a leap year')

#finding occurence of charactter

# input_string=str(input('enter a string'))
# input_char=str(input('enter a char'))
# count=0
# for i in range(len(input_string)):
#     if (input_string[i]==input_char):
#         count=count+1
# print(count)
# 
# #this is comment through file handling