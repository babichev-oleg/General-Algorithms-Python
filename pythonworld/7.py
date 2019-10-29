#!/usr/bin/python3.6
x = 10
while x>0:
    print(x)
    x-=1
print('\n')
print('\n')
#------------------------------------
for i in 'hello world':
    print(i * 2, end='')
print('\n')
print('\n')
#-----------------------------------
for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')
print('\n')
print('\n')
#-----------------------------------
for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')
print('\n')
print('\n')
#----------------------------------
for i in 'hello world':
    if i == 'a':
        break
else:
    print("letter a is not exists")
