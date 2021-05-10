import math

def encrypt(plaintext,key):
    ciphertext = ''
    flag = 0
    key_list = key
    for plain in plaintext:
        if flag % len(key_list) == 0:
            flag = 0
        if plain.isalpha(): #判断是否为英文
            str = chr( (ord(plain)-97-97+ ord(key_list[flag]))%26 +97)
            ciphertext =  ciphertext + str
            flag += 1
        else:#不是英文不加密
            ciphertext += plain
    return ciphertext

def decrypt(ciphertext,key):
    text = ''
    flag = 0
    key_list = key
    for str in ciphertext:
        if flag % len(key_list) == 0:
            flag = 0
        if str.isalpha():  # 判断是否为英文
            str = chr( (ord(str) - ord(key_list[flag])) % 26 + 97)
            text = text + str
            flag += 1
        else:  # 不是英文不加密
            text += str
    return text

if __name__ == '__main__':
    plaintext = 'youngbcyoungbc'
    key = 'bc'
    ciphertext = encrypt(plaintext,key)
    print(ciphertext)

    text = decrypt(ciphertext,key)

    print(text)