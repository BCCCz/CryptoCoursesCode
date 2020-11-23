from Crypto.Util.number import *
from gmpy2 import *
import math
import random

p = 2579
g = 2
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
