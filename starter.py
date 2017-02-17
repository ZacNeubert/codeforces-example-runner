#!/usr/bin/python
import re
import inspect
from sys import argv, exit

def rstr():
    return input()

def rint():
    return int(input())

def rints(splitchar=' '):
    return [int(i) for i in input().split(splitchar)]

def varnames(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]

def pvar(var, override=False):
    prnt(varnames(var), var)

def prnt(*args, override=False):
    if '-v' in argv or override:
        print(*args)

if __name__ == '__main__':
    n = rint()
