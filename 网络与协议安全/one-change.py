# 矩阵换位加密与解密
import math

def encrypt(key,plain):
    str = ''
    cipher_list = list(key)
    plain_text_list = list(plain.replace(" ",""))
    # 密钥ASCII码列表
    cipher_ord_list = []
    # 密钥顺序列表，储存每个字母在整个密钥中的排序
    cipher_sort_list = []
    # 密文列表，存放明文加密后的密文
    cipher_text_list = plain_text_list[:]
    # 密钥长度
    cipher_length = len(cipher_list)
    # 明文长度
    plain_text_length = len(plain_text_list)
    # 要补齐的'x'字母数目
    l =(cipher_length - plain_text_length % cipher_length) % cipher_length
    # 矩阵的行数
    row = math.floor(plain_text_length / cipher_length)
    for j in range(0,l):
        plain_text_list.append('x')
    for i in range(0,cipher_length):
        cipher_ord_list.append(ord(cipher_list[i]))
    for i in range(0,cipher_length):
        sum = 0
        for j in range(0,cipher_length):
            if cipher_ord_list[i] < cipher_ord_list[j]:
                sum +=1
        cipher_sort_list.append(cipher_length-sum-1)
    # 矩阵换位加密
    for i in range(0,cipher_length):
        for k in range(0,row):
            cipher_text_list[k*cipher_length+i] = \
                plain_text_list[k*cipher_length+cipher_sort_list[i]]
    for i in range(0,plain_text_length):
        str = str + cipher_text_list[i]
    return str

def decrypt(key,ciphertext):
    str = ''
    cipher_list = list(key)
    cipher_text_list = list(ciphertext.replace(" ", ""))
    # 密钥ASCII码列表
    cipher_ord_list = []
    # 密钥顺序列表，储存每个字母在整个密钥中的排序
    cipher_sort_list = []
    # 明文列表，存放密文解密后的明文
    plain_text_list = cipher_text_list[:]
    # 密钥长度
    cipher_length = len(cipher_list)
    # 密文长度
    cipher_text_length = len(cipher_text_list)
    # 矩阵的行数
    row = math.floor(cipher_text_length / cipher_length)
    for i in range(0, cipher_length):
        cipher_ord_list.append(ord(cipher_list[i]))
    for i in range(0, cipher_length):
        sum = 0
        for j in range(0, cipher_length):
            if cipher_ord_list[i] < cipher_ord_list[j]:
                sum += 1
        cipher_sort_list.append(cipher_length - sum - 1)
    # 矩阵换位解密
    for i in range(0, cipher_length):
        for k in range(0, row):
            plain_text_list[k * cipher_length + cipher_sort_list[i]] = \
                cipher_text_list[k * cipher_length + i]

    for i in range(0,cipher_text_length):
        str = str + plain_text_list[i]
    return str

if __name__ == '__main__':
    plain = 'attack begins at five'
    key = 'cipher'
    #加密
    ciphertext = encrypt(key,plain)
    #矩阵形式输出，与课本保持一致
    print('Cipher Matrix:')
    for i in range(0, len(ciphertext)):
        if i % len(key) == 0:
            print('')
        print(ciphertext[i], end="")
    print('')
    print('')
    #解密
    text = decrypt(key,ciphertext)
    #矩阵形式输出
    print('Text Matrix:')
    for i in range(0, len(text)):
        if i % len(key) == 0:
            print('')
        print(text[i], end="")
