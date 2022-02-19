# n=int(input("enter "))
# for i in range(1,n):
#     for j in range(i,n):
#         print(j,end="")
#     print(i)


# right starat pattern
# def patter(n):
#     for i in range(0,-1):
#         for j in range(0,i+1):
#             print("*",end="")
#         print("\r")
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end="")
#         print("\r")

# patter(5)

# pyramid pattern

# def pattern(n):
#     k=3*n-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end='')
        
#         k=k-1
#         for j in range(0,i+1):
#             print("*",end="")
#         print("")
# pattern(5)


# if salary is greter than 30000 thousand please does not print
# x=[10000,20000,30000,50000,69000,130000]
# for i in x:
#     if i<30000:
#         continue
#     print(i)

"""sum of all salary which is divide by 1500"""
# x=[10000,20000,30000,1500,15000 ]
# sum=0
# for i in x:
#     if i%1500==0:
#         sum=sum+i
# print(sum)

"""pattern through input """
# n=int(input('enter a number'))
# for i in range(1,n+1):
#     for j in range(1,i-1):
#         print(j,end="")
#     print(i)


"""adding the two matrices in python firstly inserting the one and second matrices and then adding two 
matrices ,insert() functon using for adding the values"""

# r=int(input("enter a number of rows"))
# c=int(input("enter a numbero of columns"))
# x=[]
# val=[]
# for i in range(0,r):
#     for j in range(0,r):
#         val.insert(j,int(input("enter the %d %d element in row and column"%(i,j))))
#     x.insert(i,val)
#     val=[]
# y=[]
# for i in range(0,r):
#     for j in range(0,c):
#         val.insert(j,int(input('enter a  the %d%d element in rwo and column'%(i,j))))
#     y.insert(j,val)
#     val=[]

# sum=[]
# for i in range(0,r):
#     for j in range(0,c):
#         val.insert(j,x[i][j]+y[i][j])
#     sum.insert(i,val)
#     val=[]
# print(sum)

""" while loop in python 
printing any string/number  mangy times"""
# i=1
# while i<=10:
#     print("mohd HUjaifa")
#     i=i+1

# i=50
# while i>=25:
#     i=i-1
#     print(i)

num=1

sum=0
while num<=10:
    sum=sum+num
    num=num+1
print(sum)