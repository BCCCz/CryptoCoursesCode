'''
秘密共享算法注意事项：
1   （3,5）门限秘密共享
2    500位左右的大整数，作为秘密，验收时给，每个放到一个txt文件中
3    随机生成5个d值
4    中间数据显示在屏幕上，包括5个d值，N值，M值，以及最后恢复了的秘密值
5    最后恢复秘密k，利用compare()函数，验证是否跟给的秘密相同
'''
import random  # 调用random模块
from Crypto.Util.number import *
from gmpy2 import *
import numpy as np
import gmpy2
import math
import sys

def compare(list, x):  # 定义一个compare()函数 传入参数为一个列表list和一个数据x
    for i in range(0, len(list) - 1):
        if gcd(list[i],x) == 1:    
            continue               
        else:                      
            return 0
    return 1                       


while True:                                       
    count = 1                                     
    list = []
    list.append(random.randint(10**167,10**168))  
    for i in range(1, 5):                         
        list.append(random.randint(10**167,10**168))
        if compare(list, list[i]) != 1:
            break                                 
        else:
            count += 1                            
    if count == 5:                               
        break
    else:                                         
        continue
for i in list:                                    
    print(i)


#中国剩余定理
#数组初始化
a = []
mi = []
li = []
x = 0

with open("Thirdcret0.txt","r") as f :
    m = f.read()
m = int(m)

print(m)

#5个随机数存入
for i in list:
    li.append(int(i))

#求mod
for i in range(5):
    n = m % li[i]
    a.append(n)

M = li[0]*li[1]*li[2]
#求解x
for i in range(3):
    Mi = M//li[i]
    Mi = gmpy2.mpz(Mi)
    Mj = gmpy2.invert(Mi,li[i])#逆元
    xj = Mi * Mj * (a[i] % M ) 
    x = x + powmod( xj ,1 ,M)

x = x % M
print(x)