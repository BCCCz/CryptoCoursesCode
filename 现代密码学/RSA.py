from Crypto.Util.number import *
from numpy import *
from gmpy2 import *

p = getPrime(1024)
q = getPrime(1024)
n = p*q

phi = (p-1)*(q-1)
e = mpz(65537)
d = invert(e,phi)

#扩展欧几里得算法
def Euclid(a,b):
    x1,x2,x3 = 1,0,a
    y1,y2,y3 = 0,1,b
    while(y3 != 0):
        Q = x3//y3
        t1,t2,t3 = x1-Q*y1,x2-Q*y2,x3-Q*y3
        x1,x2,x3 = y1,y2,y3
        y1,y2,y3 = t1,t2,t3
    return x3,x1,x2

#M明文
input = b'Crypto_is_so_east'

#加密
M = bytes_to_long(input)
C = powmod(M,e,n)
print(C)

#解密
output = powmod(C,d,n)
M = long_to_bytes(output)
print(M)
