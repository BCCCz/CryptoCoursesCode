def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j
    return x, y


# 明文和密钥的输入
plaintext = input('Enter plaintext::')
plaintext = plaintext.upper();
keyword = input('Enter keyword::')
keyword = keyword.upper()
message = []
for plain in plaintext:
    message.append(plain)


# 5*5KeyWord矩阵生成
matrix = []
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for e in keyword.upper():
    if e not in matrix:
        matrix.append(e)
# print('KeyWord', matrix)
for e in alpha:  #填补剩余空间
    if e not in matrix and e != 'J':
        matrix.append(e)
keyword_matrix = []
for e in range(5):
    keyword_matrix.append('')
keyword_matrix[0] = matrix[0:5]
keyword_matrix[1] = matrix[5:10]
keyword_matrix[2] = matrix[10:15]
keyword_matrix[3] = matrix[15:20]
keyword_matrix[4] = matrix[20:25]
print('KeyWord Matrix 5*5(KEY)::', keyword_matrix)
print('(PLAINTEXT)::', message)


# 明文两两分组
i = 0
l = len(message)
new_message = []                     #存放两两分组
while True:
    if message[i] == message[i + 1]: #若组内的字母相同
        message.insert(i + 1, 'X')
    new_message.append(message[i:i + 2])
    i = i + 2
    if i+2 > l:
        break
if len(message) % 2 == 1:             #长度为奇数时，末尾补上X
    message.append("X")
new_message.append(message[i:i + 2])
# print(new_message)


# 明文加密
q = 0;
cipher_matrix = []
for e in new_message:
    p1, q1 = find_position(keyword_matrix, e[0])
    p2, q2 = find_position(keyword_matrix, e[1])

    if p1 == p2:     #行相同
        if q1 == 4:
            q1 = -1
        if q2 == 4:
            q2 = -1
        cipher_matrix.append(keyword_matrix[p1][q1 + 1])
        cipher_matrix.append(keyword_matrix[p1][q2 + 1])
    elif q1 == q2:   #列相同
        if p1 == 4:
            p1 = -1;
        if p2 == 4:
            p2 = -1;
        cipher_matrix.append(keyword_matrix[p1 + 1][q1])
        cipher_matrix.append(keyword_matrix[p2 + 1][q2])
    else:           #两个字母不同行也不同列
        cipher_matrix.append(keyword_matrix[p1][q2])
        cipher_matrix.append(keyword_matrix[p2][q1])
print("(CIPHERTEXT)::",str(cipher_matrix))

#密文解密
i = 0
new_cipher_matrix = []
while i < len(cipher_matrix):
    new_cipher_matrix.append(cipher_matrix[i:i + 2])
    i = i + 2
# print(new_cipher_matrix)  #对密文两两分组

omessage = []
for e in new_cipher_matrix:
    p1, q1 = find_position(keyword_matrix, e[0])
    p2, q2 = find_position(keyword_matrix, e[1])
    if p1 == p2:
        if q1 == 0:
            q1 = 5
        if q2 == 0:
            q2 = 5
        omessage.append(keyword_matrix[p1][q1 - 1])
        omessage.append(keyword_matrix[p1][q2 - 1])
    elif q1 == q2:
        if p1 == 0:
            p1 = 5;
        if p2 == 0:
            p2 = 5;
        omessage.append(keyword_matrix[p1 - 1][q1])
        omessage.append(keyword_matrix[p2 - 1][q2])
    else:
        omessage.append(keyword_matrix[p1][q2])
        omessage.append(keyword_matrix[p2][q1])

if "X" in omessage:
	omessage.remove("X")
print("(Oringal Message)::")
print(omessage)
