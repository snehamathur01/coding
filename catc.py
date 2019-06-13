#!/usr/bin/python3
option='''
Press  1  to  view file contents :
Press  2  to  view multiple files contents :  
Press  3  to  show content preceding with line number :  
Press  4  to create a file  :  
'''
print(option)
choice=int(input())
if   choice == 1 :
     print("enter file name")
     f=input()
     fi=open(f)
     print(fi.read())
elif choice == 2 :
     print("enter names of files")
     files =input()
elif choice == 3:
     name = input("Enter file name")
     f = open(name)
     text = f.readlines()
     for i in range(1,len(text)+1):
         print(i,text[i-1])
elif choice == 4:
     name = input("enter file name to be created")
     f=open(name,'w')
else :
     print("invalid choice")
