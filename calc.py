#!/usr/bin/env python3.8

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(a, b):
    return a ** b

print('Select Operation')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('Divide')

Choice = input('Enter Choice(1/2/3/4): ')

num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))

if Choice == '1':
    print(num1,'+',num2,'=', add(num1,num2))

elif Choice == '2':
    print(num1,'-',num2,'=', subtract(num1,num2))

elif Choice == '3':
    print(num1,'*',num2,'=', multiply(num1,num2))

elif Choice == '4':
    print(num1,'/',num2,'=', divide(num1,num2))

else:
    print('Invalid Input')