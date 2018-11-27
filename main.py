
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