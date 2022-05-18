
# def mohd():
#     print("hello mohd, how are you?")
# mohd()

# def calculator(a,b,c):
#     add=a+b+c
#     mul=a*b*c
#     div=a/b/c
#     minus=c-a-b
#     print(add)
#     print(mul)
#     print(div,minus)
# calculator(10,25,45)

# def calculator(a,b,c):
#     add=a+b+c
#     mul=a*b*c
#     div=a/b/c
#     minus=c-a-b
#     print(add)
#     print(mul)
#     print(div,minus)
# calculator(b=10,a=25,c=45)

""""adding element in fucntion and outside the function and finding the store space id."""
# def add(a,b):
#     print(id(a),id(b))
#     a=10
#     b=20
#     print(id(a),id(b))
#     total=a+b
#     print("the multiplication value is ",total)
# x=5
# y=20
# print(id(x),id(y))
# add(x,y)
# print("sum of", (x+y))

""" if we want to add n number of list so we don't have to declare parameter in def function"""
def add(*a):
    total=0
    for i in a:
        total=total+i
    print(total)
add(40,20,30,45,95)
