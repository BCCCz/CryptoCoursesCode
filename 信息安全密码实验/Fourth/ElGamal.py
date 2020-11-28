'''
实验四验收要求：
1. 秘密长度近150位，验收用的5个秘密（145，140，135，130，125位）
2. 大素数的形式为p=2q+1形式的强素数，这里面q也是素数，要求p为150位的大素数，大素数p和本原根自己生成。（关于强素数，请同学们查阅文献资料了解学习）
3. 解密出的结果要与明文对比，验证解密是否正确。
另：另：中间数据显示在屏幕上，包括P，g，y，k及密文c=(y1, y2)等。
'''
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

while(1):
    p = getPrime(150)
    p = 2*p + 1
    if(isPrime(p) == 1):
        break
print("大素数p:",p)#大素数

g = yg(p)
print("最小原根g:",g)#原跟

a = 765

#明文
with open("/home/bc/桌面/CODE/CryptoCourcesCode/信息安全密码实验/Fourth/data/secret0.txt","r") as f :
    m = f.read()
print("明文m:",m)

#加密
k = random.randint(1,p-2)
print("k:",k)
c1 = powmod(g,k,p)

r = pow(g,a)
r = pow(r,k)
r = r*m

c2 = powmod(r,1,p)
print("c1:",c1)
print("c2:",c2)

#解密
v = powmod(c1,a,p)
c = mpz(c1**a)
v = invert(c,p)
m = (c2*v) % p
print(m)
