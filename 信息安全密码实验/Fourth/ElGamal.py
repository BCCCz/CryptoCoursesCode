from Crypto.Util.number import *
from gmpy2 import *
import math
import random

def multimod(a,k,n):    #快速幂取模
    ans=1
    while(k!=0):
        if k%2:         #奇数
            ans=(ans%n)*(a%n)%n
        a=(a%n)*(a%n)%n
        k=k//2          #整除2
    return ans

def yg(n):		# 这样默认求最小原根
    k=(n-1)//2
    for i in range(2,n-1):
        if multimod(i,k,n)!=1:
            return i

p = 2579
g = yg(p)
a = 765
#明文
m = 1299

#加密
k = random.randint(1,p-2)
c1 = powmod(g,k,p)
c2 = (m*(g**a)**k) % p

#解密
v = powmod(c1,a,p)
c = mpz(c1**a)
v = invert(c,p)
m = (c2*v) % p
print(m)
