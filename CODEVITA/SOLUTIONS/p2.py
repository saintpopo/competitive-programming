# /*
#  *
#  ********************************************************************************************
#  * AUTHOR : AKASH KANDPAL                                                                   *
#  * Language : Python2                                                                       *
#  * Motto : The master has failed more times than the beginner has even tried.               *
#  * IDE used: Atom                                                                           *
#  * My Domain : http://harrypotter.tech/                                                     *
#  ********************************************************************************************
#  *
#  */
from collections import Counter
from math import ceil
from fractions import gcd
import math
import itertools
from itertools import permutations
from itertools import combinations
import calendar
from itertools import product
from datetime import date
from string import ascii_uppercase

import math
# from itertools import permutations
# import statistics
import calendar
def readInts():
    return list(map(int, raw_input().strip().split(',')))
def readInt():
    return int(raw_input())
def readStrs():
    return raw_input().split(',')
def readStr():
    return raw_input()
def readnumbertolist():
    a=[int(i) for i in list(raw_input())]
    return a
def dec2hex(num):
    if num == 0:
        return 0
    ans = ""
    while num > 0:
        ans = str(num%6) + ans
        num /= 6
    return int(ans)

def hex2dec(num):
    if num == 0:
        return 0
    num = str(num)
    ans = int(num[0])
    for i in num[1:]:
        ans *= 6
        ans += int(i)
    return ans

def printdec(ans):
    print '{0:.6f}'.format(ans)
def countchars(stra):
    s=Counter(stra)
    return s
# def readInts():
#     return list(map(int, raw_input().strip().split()))
# def readInt():
#     return int(raw_input())
# def readStrs():
#     return raw_input().split()
# def readStr():
#     return raw_input().strip()
def readarr(n):
    return [map(int,list(readStr())) for i in xrange(n)]
def readnumbertolist():
    a=[int(i) for i in list(raw_input())]
    return a
def strlistTostr(list1):
    return ''.join(list1)
def numlistTostr(list1):
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
    return '{0:063b}'.format(x)
def findpermute(word):
    perms = [''.join(p) for p in permutations(word)]
    perms = list(set(perms))
    return perms
def findsubsets(S,m):
    return list(set(itertools.combinations(S, m)))
def sort1(yy,index):
    return yy.sort(key = lambda x:x[index])
def reversepair(yy):
    return yy[::-1]
def checkint(x):
    return (x).is_integer()
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")
    for alphabet in str:
        if alphabet in vowel:
            count = count + 1
    return count
def leapyear(year):
    return calendar.isleap(year)
def factorial(n):
	p=1
	for i in range(2,n+1):
		p=p*i
	return p
def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes
def distinctstr(s):
    t =''.join(set(s))
    return t
def countdict(s):
    d ={}
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]]=1
        else:
            d[s[i]]+=1
    return d
import operator as op
def nck(n, k):
    k = min(n-k,k)
    result = 1
    for i in range(1, k+1):
        result = result* (n-i+1) / i
    return result
def gcd(a,b):
    if (a == 0):
        return b;
    return gcd(b%a, a);
def power(x,y,m=1000000007):
    if (y == 0):
        return 1;
    p = power(x, y/2, m) % m;
    p = (p * p) % m;
    if(y%2 == 0):
    	return p
    else:
    	return (x * p) % m;
def modInverse(a,m):
   	g = gcd(a, m);
	if(g!=1):
		return -1
 	else:
   		return power(a, m-2, m);
def lcm(a, b):
    return a * b / gcd(a, b)
def matrixcheck(x,y):
    faadu = []
    directions = zip((0,0,1,-1),(1,-1,0,0))
    for dx,dy in directions:
        if R>x+dx>=0<=y+dy<C and A[x+dx][y+dy]==0:
            faadu.append((x+dx,y+dy))
    return faadu
def stringcount(s):
    return [s.count(i) for i in "abcdefghijklmnopqrstuvwxyz"]
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def isSubsetSum(st, n, sm) :
    # arr, n, k
    subset=[[True] * (sm+1)] * (n+1)
    for i in range(0, n+1) :
        subset[i][0] = True
    for i in range(1, sm + 1) :
        subset[0][i] = False
    for i in range(1, n+1) :
        for j in range(1, sm+1) :
            if(j < st[i-1]) :
                subset[i][j] = subset[i-1][j]
            if (j >= st[i-1]) :
                subset[i][j] = subset[i-1][j] or subset[i - 1][j-st[i-1]]
    return subset[n][sm];
def decimal_to_octal(dec):
    decimal = int(dec)
    return oct(decimal)
def decimal_to_binary(dec):
    decimal = int(dec)
    return bin(decimal)
def decimal_to_hexadecimal(dec):
    decimal = int(dec)
    return hex(decimal)
def find_duplicate(expr):
  stack=[]
  char_in_between = 0
  f =1
  for i in range(0, len(expr)):
    if expr[i] == '}' or expr[i] == ')':
      pair = '{' if expr[i] == '}' else '('
      pop=''
      while(len(stack) > 0 and pop != pair):
        pop = stack.pop()
        if (pop != '{' and pop != '('): char_in_between +=1
      if char_in_between == 0:
        print "Duplicate"
        f =0
        break
      char_in_between = 0
    else:
      stack.append(expr[i])
  return f
def dictlist(keys,values):
    {d.setdefault(key,[]).append(value) for key, value in zip(keys,values)}
    return d
def mullistbyconst(my_list,r):
    my_new_list = []
    for i in my_list:
        my_new_list.append(i * r)
    return my_new_list
def coinchange(S, m, n):
    # (arr,length,sum)
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
    return table[n]
import itertools
def permutation_of_list(lista):
    return list(itertools.permutations(lista))
def palincheck(i):
    return str(i) == str(i)[::-1]
def bigMod(a, b, c):
    if (a == 0 or b == 0) :
        return 0
    if (a == 1) :
        return b
    if (b == 1) :
        return a
    a2 = bigMod(a, b / 2, c)
    if ((b & 1) == 0) :
        return (a2 + a2) % c
    else :
        return ((a % c) + (a2 + a2)) % c
def days(year1,year2):
    begin = date(year1, 1, 1)
    end = date(year2, 1, 1)
    return (end-begin).days
from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
def prelongfact(factt):
    for i in reversed(range(1,int(factt**0.5))):
        if factt%i==0:
            break
    return  factt/i
def factmul(n,lim,m):
    mul=1
    ans=1
    if(n>=lim):
        print 0
    else:
        for j in range(1,n+1):
            mul=(mul*j)%m
            ans=(ans*mul)%m
        print ans
def knapSack(W , wt , val , n):
    if n == 0 or W == 0 :
        return 0
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))

# m = 329885391853
# lim =  prelongfact(m)

mod = 10 ** 9 + 7
# fact=[1]
# for i in xrange(1,100001):
#     fact.append(((arr[i-1]%mod)*(i%mod))%mod)
# for i,j in product(xrange(R),xrange(C)):
# print "Case #{}: {}".format(i+1,ans)

# for __ in range(readInt()):
arr = readInts()
arr = sorted(arr)
a,b,c,d,e,f =-1,-1,-1,-1,-1,-1
c0 = arr.count(0)
c2 = arr.count(2)
c4 = arr.count(4)
################
val1,val2=-1,-1
for i in range(len(arr)):
    for j in range(len(arr)):
        if i!=j and (arr[i]*10+arr[j])<=23:
            a = max(a,arr[i]*10+arr[j])
            val1,val2 = arr[i],arr[j]
if val1 in arr:
    arr.remove(val1)
if val2 in arr:
    arr.remove(val2)
################
for i in arr:
    if i<=5:
        c = max(c,i)
if c in arr:
    arr.remove(c)
for i in arr:
    if i<=9:
        d = max(d,i)
if d in arr:
    arr.remove(d)
for i in arr:
    if i<=5:
        e = max(e,i)
if e in arr:
    arr.remove(e)
for i in arr:
    if i<=9:
        f = max(f,i)
if f in arr:
    arr.remove(f)
# print a,b,c,d,e,f
if c2>0 and c4>0 and c0>=4:
    print("24:00:00")
elif val1==-1 or val2==-1 or c==-1 or d==-1 or e==-1 or f==-1:
    print "Impossible"
else: 
    stri = str(val1)+str(val2)+":"+str(c)+str(d)+":"+str(e)+str(f)
    print stri

'''
Example 1

Input
0,1,3,4,2,1,5,8,0
0,0,7,8,2,4,5,0,0
0,0,0,0,0,0
0,0,1,1,3,5,6,7,7

0,0,5,6,7,7
Output

17:57:36

The maximum valid time in a 24 hour clock that can be formed using some six of the 9 digits precisely once is 17:57:36

Example 2

Input

3,3,3,3,3,3,3,3,3

Output

Impossible

'''