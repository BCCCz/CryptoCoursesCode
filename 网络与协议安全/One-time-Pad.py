import math

def encrypt(plaintext,key):
    str_list = list(plaintext)
    key_list = list(key)
    i = 0
    while i <len(plaintext):
        if not str_list[i].isalpha():
            str_list[i] = str_list[i]
        else:
            a = "A" if str_list[i].isupper() else "a"
            str_list[i] = chr((ord(str_list[i]) - ord(a) + ord(key_list[i]) - ord(a)) % 26 + ord(a))
        i = i + 1
    return ''.join(str_list)

def decrypt(ciphertext,key):
    str_list = list(ciphertext)
    key_list = list(key)
    i = 0
    while i <len(plaintext):
        if not str_list[i].isalpha():
            str_list[i] = str_list[i]
        else:
            a = "A" if str_list[i].isupper() else "a"
            str_list[i] = chr( ( ( ord(str_list[i]) - ord(key_list[i]) ) % 26 + ord(a)) )
        i = i + 1
    return ''.join(str_list)

if __name__ == '__main__':
    plaintext = 'THIS IS SECRET'
    key = 'XVHE UW NOPGDZ'
    ciphertext = encrypt(plaintext,key)
    print(ciphertext)

    text = decrypt(ciphertext,key)
    print(text)