
import math
from fractions import gcd
from itertools import permutations
from itertools import combinations

def readInts():
    return list(map(int, raw_input().strip().split()))
def readInt():
    return int(raw_input())
def readIntsindex0():
    return list(map(lambda x: int(x) - 1, input().split()))
def readStrs():
    return raw_input().split()
def readStr():
    return raw_input()
def numlistTostr(list1):
    return ''.join(list1)
def strlistTostr(list1):
    return ''.join(str(e) for e in list1)
def strTolist(str):
    return str.split()
def strlistTointlist(str):
    return map(int, str)
def slicenum(number,x):
    return int(str(number)[:x])
def precise(num):
    return "{0:.10f}".format(num)
def rsorted(a):
    return sorted(a,reverse=True)
def binar(x):
    return '{0:031b}'.format(x)
def permute(word):
    perms = [''.join(p) for p in permutations(word)]
    # print perms
    return set(perms)

for __ in range(readInt()):
    n,k = readInts()
    a = []
    for i in range(n+1):
        a.append(i)
    # print a
    comb = combinations(a, k)
    s= 0
    for i in list(comb):
        # print i
        if(sum(i)==n):
            s+=1
            # print(i)
    print 2*s


'''
Input:
2
3 2
5 2

Output:
4
6

'''
