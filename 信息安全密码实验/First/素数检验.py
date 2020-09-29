from Crypto.Util.number import *
from Crypto.Util import number
from gmpy2 import *
import gmpy2
import random
import math

#素数生成
def get_prime(key_size):
    while True:
        num = random.randrange(2**(key_size-1), 2**key_size)
        if is_prime(num):
            return num

#m生成的大素数
Prime = get_prime(1024)

#大素数写入文件
with open("CryptoCourcesCode/信息安全密码实验/First/prime.txt","w") as f :
    f.write(str(Prime))
f.close()

#文件再次读取大素数
with open("CryptoCourcesCode/信息安全密码实验/First/prime.txt","r") as f :
    m = f.read()
print(m)

#转换int型方便检验
m = int(m)

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
            print("Maybe Priexitme and the probability is")
            print(1-pow(1/2,i))
            
# 验证结果是否正确
print(m)
print("Test:Is prime?")
print(gmpy2.is_prime(m))