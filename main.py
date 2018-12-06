"""Benvenuti al mini corso di programmazione in Python"""

print("Hello  Bearzi\n")

mystring = 'hello'
mystring = "hello"

# La differenza tra le due è semplice: Usando le doppie virgolette
# posso inserire l'apostrofo cosa questa che non potrei fare se avessi
# usato le virgolette semplici perché l'apostrofo non sarebbe stato
#  considerato come tale ma semplicemenete un terminatore della stringa


nome = "Mario"
print("""
sd
 a  
  sd a
  sd    asd
    asda
    ds""", flush=True)

print(nome.index("r"))

print(nome.replace("io", "te"))

print(nome.upper(), flush=True)

print("({},{} )".format(3, 4))

print("-".join(["a", "b", "c"]).capitalize())

str1 = 'Hello "Python"'
str2 = "Hello 'Python'"
str3 = """Hello "'Python'" """

print(str1)
print(str2)
print(str3)



################unicode   https://unicode-table.com/it/#unified-canadian-aboriginal-syllabics
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

# \xf6 è il codice esadecimale

print('Pyth\xf6n is interesting')

print("abc".encode())

arr = bytes("ciao", 'utf-8')
print(arr)

Str = "this is string example....wow!!!";
strr = Str.encode('UTF-8', 'strict');
print(str(strr))
res = bytearray(str(strr), 'utf-8')
for i in res:
    print("byte value -->" + str(i))
print("Decoded String: " + strr.decode('utf-8', 'strict'))

s = "\xf6"
arrofb = bytearray(s, 'utf-8')

for u in arrofb:
    print(u)

    # 195
    # 182

# Stampa 2 numeri perchè ha bisogno di 2 bytes

print("Len of  array  of bytes --->" + str(len(arrofb)))
##############################################################################################
v = 3;

t = 6 * v;

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3

# prints out 1,2,3
for x in mylist:
    print(x, flush=True)

for c in nome:
    print(c, flush=True)

mylist = [1, 2, 3]  # questa lista ha 3 elementi e quindi
print(mylist[2])

a = "A" * 4
print(a)
c = "quattro"
print(" A*4 = " + c + " A")

a = [1, 2, 3]
b = [4, 5, 6]
# a + b = [1,2,3,4,5,6]
# a * 2 = [1,2,3,1,2,3]


print(a + b)
print(b * 2)

print(3.214)

c = -43
print(abs(c))

t = 2 ** c
print(t)

print(round(t))

from math import *  # importimao un modulo

print(ceil(t))

print(sqrt(4))

# input = input("Enter your name: ")
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + ", you are " + age + "\n")

num1 = input("Enter your name: ")
num2 = input("Enter your age: ")

print(num1 + num2)

print(int(num1) + int(num2))

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

num_str = "456"
# print(num_int+num_str)

# Type Conversion is the conversion of object from one data type to another data type.
# Implicit Type Conversion is automatically performed by the Python interpreter.
# Python avoids the loss of data in Implicit Type Conversion.
# Explicit Type Conversion is also called Type Casting, the data types of object are converted using predefined function by user.
# In Type Casting loss of data may occur as we enforce the object to specific data type.

print(float(5))

fromString = float('2.5')

a = {5, 2, 3, 1, 4}

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

# Generates error
print("d[2] = ", d[2]);

dd = dict([[1, 2], [3, 4]])

ss = set([1, 2, 3])

tt = tuple({5, 6, 7})

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

# n the above program, This is Python is a string literal and C is a character literal.
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
    return 2 * num


print(double(6))

print(1, 2, 3, 4, sep='#', end='&')
# Output: 1#2#3#4&

print('I love {0} and {1}'.format('bread', 'butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread', 'butter'))
# Output: I love butter and bread

print('Hello {name}, {greeting}'.format(greeting='Goodmorning', name='John'))

# import math
# print(math.pi)

import sys

print(sys.path)

# Membership operators

x = 'Hello world'
y = {1: 'a', 2: 'b'}

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


def factorial(n):
    r = 1
    for i in range(1, n):
        r *= i
    return r


def fact(n):
    """factorial of n"""
    return n > 0 if n * fact(n - 1) else 1


class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):  # polimorfismo
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


# ------------------


class MyClass:
    "This is my second class"
    a = 10

    def func(self):
        print('Hello')


# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)

"""
Addition	p1 + p2	p1.__add__(p2)
Subtraction	p1 - p2	p1.__sub__(p2)
Multiplication	p1 * p2	p1.__mul__(p2)
Power	p1 ** p2	p1.__pow__(p2)
Division	p1 / p2	p1.__truediv__(p2)
Floor Division	p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2	p1.__mod__(p2)
Bitwise Left Shift	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	p1 & p2	p1.__and__(p2)
Bitwise OR	p1 | p2	p1.__or__(p2)
Bitwise XOR	p1 ^ p2	p1.__xor__(p2)
Bitwise NOT	~p1	p1.__invert__()"""
