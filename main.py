

"""Benvenuti al mini corso di programmazione in Python"""

print("Hello  Bearzi\n")

mystring = 'hello'
mystring = "hello"

# La differenza tra le due è semplice: Usando le doppie virgolette
# posso inserire l'apostrofo cosa questa che non potrei fare se avessi
# usato le virgolette semplici perché l'apostrofo non sarebbe stato
#  considerato come tale ma semplicemenete un terminatore della stringa


nome= "Mario"
print("""
sd
 a  
  sd a
  sd    asd
    asda
    ds""" , flush=True)

print(nome.index("r"))

print(nome.replace("io", "te"))

print(nome.upper() , flush=True)

v = 3;

t = 6 * v;


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x , flush=True)

for c in nome:
    print(c , flush=True)


mylist = [1, 2, 3]  # questa lista ha 3 elementi e quindi
print(mylist[2])

a = "A" * 4
print(a)
c = "quattro"
print(" A*4 = " + c + " A")

a = [1,2,3]
b = [4,5,6]
#a + b = [1,2,3,4,5,6]
#a * 2 = [1,2,3,1,2,3]


print(a+b)
print(b*2)


print(3.214)

c=-43
print(abs(c))

t=2 **c
print(t)

print(round(t))

from math import * #importimao un modulo


print(ceil(t))

print(sqrt(4))

#input = input("Enter your name: ")
name = input("Enter your name: ")
age= input("Enter your age: ")
print("Hello " + name + ", you are "+ age +"\n")


num1 = input("Enter your name: ")
num2= input("Enter your age: ")

print(num1+num2)

print(int(num1)+int(num2))


num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

num_str = "456"
#print(num_int+num_str)

#Type Conversion is the conversion of object from one data type to another data type.
#Implicit Type Conversion is automatically performed by the Python interpreter.
#Python avoids the loss of data in Implicit Type Conversion.
#Explicit Type Conversion is also called Type Casting, the data types of object are converted using predefined function by user.
#In Type Casting loss of data may occur as we enforce the object to specific data type.

print(float(5))

fromString = float('2.5')



a = {5,2,3,1,4}


fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

d = {1:'value','key':2}
print(type(d))


print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

# Generates error
print("d[2] = ", d[2]);

dd= dict([[1,2],[3,4]])

ss = set([1,2,3])

tt = tuple({5,6,7})

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

#n the above program, This is Python is a string literal and C is a character literal.
# The value with triple-quote """ assigned in the multiline_str is multi-line string literal.
# The u"\u00dcnic\u00f6de" is a unicode literal which supports characters other than English and r"raw \n string" is a raw string literal.

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

def double(num):
    """Function to double the value"""
    return 2*num

print(double(6))

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

#import math
#print(math.pi)

import sys
print(sys.path)


# Membership operators

x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")