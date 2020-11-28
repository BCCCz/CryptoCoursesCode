from Crypto.Util.number import *
from Crypto.Util import number
from gmpy2 import *
import gmpy2
import random
import math

'''
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
'''

#文件再次读取大素数
with open("/home/bc/桌面/CODE/CryptoCourcesCode/信息安全密码实验/First/prime.txt","r") as f :
    m = f.read()

#转换int型方便检验
m = int(m)

#k循环次数
k = 4
for i in range(1,k+1):
    a = random.randint(2,m-2)
    g = gcd(a,m)
    if(g != 1):
        print("The number is not Prime")
        sys.exit(0)
    else:
        r = pow(a,m-1,m)
        if(r != 1):
            print("The number is not Prime")
            sys.exit(0)
        else:
            print("Maybe Priexitme and the probability is")
            print(1-pow(1/2,i))
            
print('The number is prime')
# 验证结果是否正确


print('结果验证')
print(gmpy2.is_prime(m))
