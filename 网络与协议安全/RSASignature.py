from Crypto.Util.number import *
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from numpy import *
from gmpy2 import *
import hashlib
import random

#扩展欧几里得求最大公约数
def Euclid(a,b):
    x1, x2, x3 = 1, 0, a
    y1, y2, y3 = 0, 1, b
    while y3 != 0:
        Q = x3//y3
        t1,t2,t3 = x1-Q*y1,x2-Q*y2,x3-Q*y3
        x1,x2,x3 = y1,y2,y3
        y1,y2,y3 = t1,t2,t3
    return x1

#大素数生成
def generateLargePrime():
    while True:
        num = random.randrange(2 ** (1024 - 1), 2 ** 1024)
        if is_prime(num):
            return num

# 快速幂取模
def multimod(a, k, n):
    ans = 1
    while k != 0:
        if k % 2:
            ans = (ans % n) * (a % n) % n
        a = (a % n) * (a % n) % n
        k = k // 2
    return ans

if __name__ == '__main__':
    p = generateLargePrime()
    q = generateLargePrime()
    n = p*q
    phi = (p-1)*(q-1)
    e = mpz(65537) #公钥
    d = Euclid(e, phi) #私钥

    message = b'It was the best of times, it was the worst of times, it was the age of wisdom, ' \
              b'it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, ' \
              b'it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair'

    sha256 = hashlib.sha256()
    sha256.update(message)

    #先Hash
    Hash = sha256.digest()
    #再用私钥加密
    C = bytes_to_long(Hash)
    signature1 = multimod(C,d,n)

    #公钥解密
    M = multimod(signature1,e,n)
    text = long_to_bytes(M)

    #相关参数输出
    print('Large prime number P:',p)
    print('Large prime number Q:',q)
    print('N:',n)
    print('Private key:',d)
    print('Public key:',e)
    print('message:',message)
    print('Message_Sha256_Digest:',Hash)
    print('Signature_Text:',signature1)

    if text == Hash:
        print('Right Signature')
    else:
        print('Flase')