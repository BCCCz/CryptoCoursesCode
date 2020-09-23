from Crypto.Util.number import *
from gmpy2 import *
import gmpy2
import random
import math
import sys

a = [2,2]
mi = [7,13]
M = 1 #初始化
x = 0 #初始化
l =len(mi) #方程组数
for i in range(l):
    for j in range(i+1,l):
        if(gcd(mi[i],mi[j])!=1):
            print("Can't Use 中国剩余定理")
            exit(0)

for i in range(l):
    M = mi[i]*M

for i in range(l):
    Mi = M/mi[i]
    Mi = gmpy2.mpz(Mi)
    Mj = invert(Mi,mi[i])#逆元
    xj = powmod( (Mi * Mj * a[i]),1 ,M ) 

    x = 0 + powmod( xj ,1 ,M)


 
  
        