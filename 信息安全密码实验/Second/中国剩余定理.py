from Crypto.Util.number import *
from gmpy2 import *
import gmpy2
import math
import sys

#数组初始化
a = []
mi = []

#读取数据行数
count = len(open("/home/bc/桌面/CODE/CryptoCourcesCode/信息安全密码实验/Second/2.txt",'rU').readlines())

with open("/home/bc/桌面/CODE/CryptoCourcesCode/信息安全密码实验/Second/2.txt","r") as f :
    m = f.read().split()
    for i in range(0,int(count/2)):
        a.append(int(m[i]))
 
    for i in range(int(count/2),int(count)):
        mi.append(int(m[i]))



M = 1 #初始化
x = 0 #初始化
count = int(count) #
l = int(count/2) #方程组数


#判断能否使用中国剩余定理
for i in range(0,l):
    for j in range(i+1,l):
        if(gcd(mi[i],mi[j])!= 1):
            print("Can't Use 中国剩余定理")
            sys.exit(0)
            
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
