from Crypto.Util.number import *
from gmpy2 import *
import gmpy2
import random
import math
import sys

#数组初始化
a = []
mi = []
#读取数据行数
count = len(open("CryptoCourcesCode/信息安全密码实验/First/2.txt",'rU').readlines())

with open("CryptoCourcesCode/信息安全密码实验/First/2.txt","r") as f :
    m = f.read().strip().split()
    for i in (1,count):
        a.append(int(m[2*i-2]))
        mi.append(int(m[2*i-1]))

M = 1 #初始化
x = 0 #初始化
l =len(mi) #方程组数

#判断能否使用中国剩余定理
for i in range(l):
    for j in range(i+1,l):
        if(gcd(mi[i],mi[j])!=1):
            print("Can't Use 中国剩余定理")
            exit(0)

#计算M
for i in range(l):
    M = mi[i]*M

#求解x
for i in range(l):
    Mi = M/mi[i]
    Mi = gmpy2.mpz(Mi)
    Mj = invert(Mi,mi[i])#逆元
    xj = powmod( (Mi * Mj * a[i]),1 ,M ) 

    x = x + powmod( xj ,1 ,M)

print(x)
   