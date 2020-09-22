from Crypto.Util.number import *
from gmpy2 import *
import gmpy2
import random
import math

#m待检验
m = 4
#k循环次数
k = 4
for i in range(1,k+2):
    a = random.randint(k,m)
    g = gcd(a,m)
    if(g != 1):
        print("Not Prime")
        break
    else:
        r = pow(a,m-1,m)
        if(r != 1):
            print("Not Prime")
            break
        else:
            print("Maybe Prime and the probability is")
            print(1-pow(1/2,i))
# 验证结果是否正确
print("Test:Is prime?")
print(gmpy2.is_prime(m))

