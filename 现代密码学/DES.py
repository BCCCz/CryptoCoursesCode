import re

IP_table = [58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7]

IP_re_table = [40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25]

E = [32,1,2,3,4,5,4,5,
     6,7,8,9,8,9,10,11,
     12,13,12,13,14,15,16,17,
     16,17,18,19,20,21,20,21,
     22,23,24,25,24,25,26,27,
     28,29,28,29,30,31,32,1]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

S = [
    [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
     0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
     4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
     15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13],

    [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
     3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
     0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
     13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9],

    [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
    13,7,00,9,3,4,6,10,2,8,5,14,12,11,15,1,
    13,6,4,9,8,15,3,00,11,1,2,12,5,10,14,7,
    1,10,13,00,6,9,8,7,4,15,14,3,11,5,2,12,],

    [7,13,14,3,00,6,9,10,1,2,8,5,11,12,4,15,
    13,8,11,5,6,15,00,3,4,7,2,12,1,10,14,9,
    10,6,9,00,12,11,7,13,15,1,3,14,5,2,8,4,
    3,15,00,6,10,1,13,8,9,4,5,11,12,7,2,14,],

    [2,12,4,1,7,10,11,6,8,5,3,15,13,00,14,9,
    14,11,2,12,4,7,13,1,5,00,15,10,3,9,8,6,
    4,2,1,11,10,13,7,8,15,9,12,5,6,3,00,14,
    11,8,12,7,1,14,2,13,6,15,00,9,10,4,5,3,],

    [12,1,10,15,9,2,6,8,00,13,3,4,14,7,5,11,
    10,15,4,2,7,12,9,5,6,1,13,14,00,11,3,8,
    9,14,15,5,2,8,12,3,7,00,4,10,1,13,11,6,
    4,3,2,12,9,5,15,10,11,14,1,7,6,00,8,13,],

    [4,11,2,14,15,00,8,13,3,12,9,7,5,10,6,1,
    13,00,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
    1,4,11,13,12,3,7,14,10,15,6,8,00,5,9,2,
    6,11,13,8,1,4,10,7,9,5,00,15,14,2,3,12,],

    [13,2,8,4,6,15,11,1,10,9,3,14,5,00,12,7,
    1,15,13,8,10,3,7,4,12,5,6,11,00,14,9,2,
    7,11,4,1,9,12,14,2,00,6,10,13,15,3,5,8,
    2,1,14,7,4,10,8,13,15,12,9,00,3,5,6,11,],

]

PC_1 = [57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4]

PC_2 = [14,17,11,24,1,5,3,28,
15,6, 21,10,23,19,12,4,
26,8, 16,7,27,20,13,2,
41,52,31,37,47,55,30,40,
51,45,33,48,44,49,39,56,
34,53,46,42,50,36,29,32]
    
# 将明文转化为二进制
def StrToBytes(message):
    res = ''
    for i in message:
        tmp = bin(ord(i))[2:]  # 将每个字符转化成二进制
        tmp = str('0' * (8 - len(tmp))) + tmp  # 补齐8位
        res += tmp
    if len(res) % 64 != 0:
        count = 64 - len(res) % 64  # 不够64位补充0
    else:
        count = 0
    res += '0' * count
    return res


# 将密钥转化为二进制
def KeyToBytes(key):
    res = ''
    for i in key:
        tmp = bin(ord(i))[2:]  # 将每个字符转化成二进制
        tmp = str('0' * (8 - len(tmp))) + tmp  # 补齐8位
        res += tmp
    if len(res) < 64:
        count = 64 - len(res) % 64  # 不够64位补充0
        res += '0' * count
    else:
        res = res[:64]
    return res


# IP盒处理
def IP_Change(str_bin):
    res = ''
    for i in IP_table:
        res += str_bin[i - 1]
    return res


# 生成子密钥
def Get_Keys(bin_key):
    key_list = []
    key1 = PC1_Change(bin_key)  # 秘钥的PC-1置换
    key_c = key1[:28]
    key_d = key1[28:]
    SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    for i in SHIFT:  # shift左移位数
        key_c = key_c[i:] + key_c[:i]  # 左移操作
        key_d = key_d[i:] + key_d[:i]
        key_output = PC2_Change(key_c + key_d)  # 秘钥的PC-2置换
        key_list.append(key_output)
    return key_list
 

# 秘钥的PC-1置换
def PC1_Change(my_key):
    res = ""
    for i in PC_1:  # PC_1盒上的元素表示位置    只循环64次
        res += my_key[i - 1]  # 将密钥按照PC_1的位置顺序排列，
    return res


# 秘钥的PC-2置换
def PC2_Change(my_key):
    res = ""
    for i in PC_2:
        res += my_key[i - 1]
    return res


# E盒置换
def E_Change(str_left):
    res = ""
    for i in E:
        res += str_left[i - 1]
    return res


def XOR(str1, str2):
    res = ""
    for i in range(0, len(str1)):
        xor_res = int(str1[i], 10) ^ int(str2[i], 10)  # 进行xor操作
        if xor_res == 1:
            res += '1'
        if xor_res == 0:
            res += '0'
    return res


def S_Change(my_str):
    res = ""
    c = 0
    for i in range(0, len(my_str), 6):  # 步长为6   表示分6为一组
        now_str = my_str[i:i + 6]  # 第i个分组
        row = int(now_str[0] + now_str[5], 2)  # 第r行
        col = int(now_str[1:5], 2)  # 第c列
        # 第几个s盒的第row*16+col个位置的元素
        num = bin(S[c][row * 16 + col])[2:]  # 利用了bin输出有可能不是4位str类型的值，所以才有下面的循环并且加上字符0
        for gz in range(0, 4 - len(num)):  # 补全4位
            num = '0' + num
        res += num
        c += 1
    return res


def P_Change(bin_str):
    res = ""
    for i in P:
        res += bin_str[i - 1]
    return res


def f(str_left, key):
    E_Change_output = E_Change(str_left)  
    xor_output = XOR(E_Change_output, key)  
    S_Change_output = S_Change(xor_output)
    res = P_Change(S_Change_output)
    return res


# IP逆盒处理
def IP_RE(bin_str):
    res = ""
    for i in IP_re_table:
        res += bin_str[i - 1]
    return res

'''
# 二进制转字符串
def BytesToStr(bin_str):
    res = ""
    tmp = re.findall(r'.{8}', bin_str)  # 每8位表示一个字符
    for i in tmp:
        res += chr(int(i, 2))
    return res
'''

'''
M = 'Crypto_is_so_easy'
K = 'bcbcbcbc'
a = StrToBytes(M)
bin_key = StrToBytes(K)

tmp = re.findall(r'.{64}', a) #Block
output = ''
for i in tmp:
    str_bin = IP_Change(a)  # IP置换
    key_lst = Get_Keys(bin_key)  # 生成16个子密钥

    str_left = str_bin[:32]
    str_right = str_bin[32:]
    for j in range(15):  
        f_res = f(str_right, key_lst[j])
        str_left = XOR(f_res, str_left)
        str_left, str_right = str_right, str_left

    f_res = f(str_right, key_lst[15])  
    str_left = XOR(str_left, f_res)

    str = (str_left+str_right)
    res = IP_RE(str)
    output = output + res
print(output)
'''

a1 = '\x1F\x1F\x1F\x1F\x0E\x0E\x0E\x0E'

key1 = StrToBytes(a1)
key2 = PC1_Change(key1)  

print(key1)
print(key2)

'''
b1 = StrToBytes(a1)



c1 = PC1_Change(b1)


d1 = Get_Keys(b1)


print(d1)
'''

