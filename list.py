#!/usr/bin/python3
a=[1,2,3,4,5,6,7]
b=[]
c=[]
print("original list")
print(a)
for i in a:
    if i>5:
       b.append(i)
    if i<=2:
       c.append(i)
print(b)
print(c)

