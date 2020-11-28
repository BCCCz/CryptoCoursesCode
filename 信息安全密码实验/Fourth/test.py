'''
Author: M@tr1x
Date: 2020-11-06 17:15:32
LastEditTime: 2020-11-11 20:22:49
Description: Elgamal密码加解密程序
'''


import gmpy2
from Crypto.Util import number
import random

class Elgamal():
    def __init__(self,p_length):
        self.q = number.getPrime(p_length)#a random prime number with 2 ^ p_length
        while self.q%10==7:
             self.q = number.getPrime(p_length)
        self.p = 2*self.q + 1#强素数
        print("强素数p:"+str(self.p))
        self.x = random.randint(2,self.p-3)#private key
        while 1:
            h = random.randint(2,self.p-1)
            self.g = gmpy2.powmod(h,2,self.p)#生成元生成算法
            if self.g != 1:
                break
        self.y = int(gmpy2.powmod(self.g,self.x,self.p))#public key y

    def encrypt(self,m):
        """crypto function

        Args:
            m (num): plain decimal message

        Returns:
            y1,y2: encrypted k&m
        """
        self.k = random.randint(1,self.p-2)
        while int(gmpy2.gcd(self.k,self.p-1))!=1:
            self.k = random.randint(1,self.p-2)
        y1 = int(gmpy2.powmod(self.g,self.k,self.p))
        y2  = m*int(gmpy2.powmod(self.y,self.k,self.p))%self.p
        
        return y1,y2
    
    def decrypt(self,y1,y2):
        """decrypto function

        Args:
            y1 (num): 
            y2 (num): 

        Returns:
            m: plain message
        """
        yi = int(gmpy2.invert(y1,self.p))
        m = int(gmpy2.powmod(yi,self.x,self.p))*y2%self.p
        return m


if __name__ == "__main__":
    new_elgamal = Elgamal(512)#加密的密文不能位数不能超过生成的大素数p
    # (y1,y2) = new_elgamal.encrypt(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)#encrypt 9999999
    fp = open('/home/bc/桌面/CODE/CryptoCourcesCode/信息安全密码实验/Fourth/data/secret0.txt','r')
    for line in fp.readlines():
        print("明文为:"+str(line))
        (y1,y2) = new_elgamal.encrypt(int(line))
    print("原根g:"+str(new_elgamal.g))
    print("y:"+str(new_elgamal.y))
    print("公钥k:"+str(new_elgamal.k))
    print("密文y1:"+str(y1))
    print("密文y2:"+str(y2))
    m = new_elgamal.decrypt(y1,y2)#decrypt y1&y2
    print("解密后:"+str(m))
    print(new_elgamal.x)