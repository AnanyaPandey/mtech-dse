# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 06:37:57 2022

@author: pandey
"""
def flatten(arr):
    res = []
    for each in arr:
        if type(each) is list:
            res.extend(flatten(each))
        else:
            res.append(each)
    return res
 
def capitalizeFirst(arr):
    res = []
    if len(arr) == 0:
        return res
    res.append(arr[0][0].upper() + arr[0][1:])
    return res + capitalizeFirst(arr[1:])


def fibo(n):
    if n in (0,1):
        return n
    return fibo(n-1)+fibo(n-2)

# Write a recursive function that takes a list of numbers as an input and returns the product of all the numbers in the list.

def prodo(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * prodo(arr[1:])

# Write a function that takes a string and returns if the string is a palindrome.

def reverse(stri):
    if len(stri)==0:
        return ''  
    new = stri[-1] + ispali(stri[:-1])
    return new

def ispali(stri):
    if len(stri) <2 : 
        return True
    if stri[0] != stri[-1]:
        return False
    return ispali(stri[1:-1])

def nestedsum(ob,s=0):
    for ke in ob:
        if type(ob[ke]) is dict:
            s = s + nestedsum(ob[ke])
        elif ob[ke]%2 == 0 and (type(ob[ke]) is int):
            s = s + ob[ke]
    return s

def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum+=obj[key]
    return sum

def capitalizeWords(arr):
    res=[]
    if len(arr) == 0 :
        return res
    res.append(arr[0].upper())
    return res + capitalizeWords(arr[1:])

def stringifyNumbers(objj):
    '''
 funcion takes a nested dictionary as input and converts the integer values into string
    '''
    obj = objj.copy()
    for ke in obj:
        if type(obj[ke]) is dict:
            stringifyNumbers(obj[ke])
        elif type(obj[ke]) is int : 
            obj[ke] = str(obj[ke])
    return obj

def collectStrings(obj):
    ''' function that takes an object and returns sub object with string values
    '''
    res = []
    for ke in obj:
        if type(obj[ke]) is dict :
            res = res + append(collectStrings(obj[ke]))
            # + creates a new list with empty space
            # append will add it to the same list which will be 
            # again initialized to [] when called so we need +
        elif type(obj[ke]) is str :
            res.append(obj[ke])
    return res

# When to use + for a list and when to use append 
# The use of the ‘+’ operator causes Python to access each element of that first list. When ‘+’ is used a new list is created with space for one more element.
# 