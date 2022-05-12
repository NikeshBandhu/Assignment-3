#Q1)            
n = int(input("Enter the value:"))
print (bin(n),"in binary")

#Q2)
expression = input("enter expression:")
print(eval(expression))

#Q3)
import math as mt

n = int(input("Enter the number n: "))
r = int(input("Enter the number r: "))
a = int(input("Enter the angle a: "))
b = int(input("Enter the angle b: "))

x1 = int(input("Enter the number x1: "))
x2 = int(input("Enter the number x2: "))

y1 = int(input("Enter the number y1: "))
y2 = int(input("Enter the number y2: "))

print("(3+4)(5) = ", (3+4)*5)
print("n(n-1)/2 = ", (n*(n-1)/1))
print("4(pi)r^2 = ", 4*mt.pi*(r^2) )
print("sqrt(r(cosa)^2 + r(sinb)^2) = ", ((r*((mt.cos(a))**2)) + (r*((mt.sin(b))**2)))**(0.5))
if x2 == x1:
    print("NOT DEFINED")
else: 
    print("y2-y1/x2-x1 = ", (y2 - y1)/(x2 - x1))

#Q4)
for i in range(5):
    print(i)
print ("")
for i in range(4,13,3):
    print(i)
print(" ")
for i in range(15,5,-2):
    print(i)
print(" ")
for i in range(5,3):
    print(i)

#Q5)
a = int(input("Enter number of carbon atom: "))
b = int(input("Enter number of oxygen:"))
c = int(input("Enter number of hydrogen atoms:"))
d = a*12.0107+ b*15.9994 +c*1.00794
print("total weight of carbohydrate is:",d)