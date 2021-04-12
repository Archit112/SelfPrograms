# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:45:27 2021

@author: archi
"""

a=input('Enter the linear equation: ')
#a='8x-6x+3-6=5x-55x-9'
print(a)

print("")
print("creating intial arrays")
left=''
right=''
flag=0
check=['-', '+', '*', '/']
for n in a:
    print(n)
    if n=="=":
        flag=1
    if flag==1:
        right+=n
    else:
        left+=n

print("")
print('left', left)
right=right[1:]
print('right', right)

print("")
print("Creating left side array")       
tmp=''
arr_left=[]
for n,i in enumerate(left):
    if i in check:
        arr_left.append(tmp)
        tmp=''
    tmp+=i
    print(i, tmp)
arr_left.append(tmp)
print(arr_left)

print("")
print("Creating right side array")
tmp=''
arr_right=[]
for n,i in enumerate(right):
    if i in check:
        arr_right.append(tmp)
        tmp=''
    tmp+=i
    print(i, tmp)
arr_right.append(tmp)
print(arr_right)

print("")
print("converting string to int if possible..")
for n, i in enumerate(arr_left):
    print(i)
    if i[-1]!='x':
        arr_left[n]=int(arr_left[n])
if "" in arr_left:
    arr_left.remove("")
print(arr_left)

for n, i in enumerate(arr_right):
    print(i)
    if len(i)>0 and i[-1]!='x':
        arr_right[n]=int(arr_right[n])
if "" in arr_right:
    arr_right.remove("")
print(arr_right)

print("")
#Move all the integers to right array
print('Moving all integers to right array')
for i in arr_left:
    #print(type(i))
    if str(type(i)) == "<class 'int'>":
        #print(i)
        arr_right.append(-1*i) 
for n, i in enumerate(arr_left):
    print(i, type(i))
    if str(type(i)) == "<class 'int'>":
        arr_left[n]=""
print(arr_left, arr_right)
print("")
#Moving all strings to left array
print('Moving all strings to left array')
for i in arr_right:
    #print(type(i), i)
    if str(type(i)) == "<class 'str'>":
        #print(i)
        tmp=i
        tmp=tmp[:-1]
        tmp=int(tmp)
        tmp*=-1
        tmp=str(tmp)
        tmp+=i[-1:]
        #print('changong', tmp)
        arr_left.append(tmp)
for n, i in enumerate(arr_right):
    print(i, type(i))
    if str(type(i)) == "<class 'str'>":
        arr_right[n]=""
        
print(arr_left, arr_right)
print("")

print("Solving right hand-array")
res_right=0
for i in arr_right:
    if i!='':
        res_right+=i
print(res_right)

print("")
print('Solving left hand array')
res_left=''
tmp=0
for i in arr_left:
    if i!='':
        tmp+=int(i[:-1])
res_left=str(tmp)+i[-1:]
print(res_left)

print("")
print("Normalizing the right hand value to get the final value of x")
res_right/=int(tmp)
res_right=round(res_right, 2)
print(res_right)

print("")
print("Value of x =", res_right)