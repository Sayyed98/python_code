"""A Name in Python Program is called Identifier.
It can be Class Name OR Function Name OR Module Name OR Variable Name.
a = 10
Rules to define Identifiers in Python:
1. The only allowed characters in python are alphabet symbols(either lower case or upper case)
    digits(0 to 9)
    underscore symbol(_)
    By mistake if we are using any other symbol like $ then we will get syntax error.
    cash = 10 √
    ca$h =20 
2. Identifier should not starts with digit
    123total 
    total123 √

3. Identifiers are case sensitive. Of course Python language is case sensitive language.

    total=10
    TOTAL=999
    print(total) #10
    print(TOTAL) #999
4.  Dollar ($) Symbol are not allowed in python identifier
"""

# for finding the keyword through programm
import keyword
print(keyword.kwlist)
