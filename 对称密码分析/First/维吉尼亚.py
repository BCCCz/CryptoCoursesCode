import vigenerecipher

#使用拟重合指数法确定秘钥长度：拟重合指数大于0.6为标志
def length(Ciphertext):
    #list列表 
    ListCiphertext=list(Ciphertext)
    #初始化密钥长度
    Keylength=1
    while True:
        #指数初始化为０
        CoincidenceIndex = 0
        #使用切片分组
        for i in range(Keylength):
            Numerator = 0
            PresentCipherList = ListCiphertext[i::Keylength]
            #使用集合去重，计算每一子密文组的拟重合指数
            for Letter in set(PresentCipherList):
                Numerator += PresentCipherList.count(Letter) * (PresentCipherList.count(Letter)-1)
            CoincidenceIndex += Numerator/(len(PresentCipherList) * (len(PresentCipherList)-1))
        #求各子密文组的拟重合指数的平均值
        Average=CoincidenceIndex / Keylength
        Keylength += 1
        #均值＞0.6即可退出循环
        if Average > 0.06:
            break
    Keylength -= 1
    return Keylength

# 根据密钥长度将密文分组
def textToList(Ciphertext,length): 
    textMatrix = [] #矩阵
    row = [] #行
    index = 0
    for ch in Ciphertext:
        row.append(ch)
        index += 1
        if index % length ==0:
            textMatrix.append(row)
            row = []
    return textMatrix

# 统计字母频度
def countList(lis): 
    li = []
    alphabet = [chr(i) for i in range(97,123)]
    for c in alphabet:
        count = 0
        for ch in lis:
            if ch == c:
                count+=1
        li.append(count/len(lis))
    return li

# 获取密钥 
def getKey(Ciphertext,length): 
    # 定义空白列表用来存密钥
    key = []
    #频率表
    alphaRate =[0.08167,0.01492,0.02782,0.04253,0.12705,0.02228,0.02015,0.06094,0.06996,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.0009,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.0015,0.01974,0.00074]
    matrix =textToList(Ciphertext,length)
    for i in range(length):
        w = [row[i] for row in matrix] #获取每组密文
        li = countList(w) 
        powLi = [] #算乘积
        for j in range(26):
            Sum = 0.0
            for k in range(26):
                Sum += alphaRate[k]*li[k]
            powLi.append(Sum)
            li = li[1:]+li[:1]#循环移位
        Abs = 100
        ch = ''
        for j in range(len(powLi)):
            if abs(powLi[j] -0.065546)<Abs: # 找出最接近英文字母重合指数的项
                Abs = abs(powLi[j] -0.065546) # 保存最接近的距离，作为下次比较的基准
                ch = chr(j+97)
        key.append(ch)
    return key


Ciphertext1 = 'krkpekmcwxtvknugcmkxfwmgmjvpttuflihcumgxafsdajfupgzzmjlkyykxd\
vccyqiwdncebwhyjmgkazybtdfsitncwdnolqiacmchnhwcgxfzlwtxzlvgqe\
cllhimbnudynagrttgiiycmvyyimjzqaxvkcgkgrawxupmjwqemiptzrtmqdc\
iakjudnnuadfrimbbuvyaeqwshtpuyqhxvyaeffldmtvrjkpllsxtrlnvkiaj\
fukycvgjgibubldppkfpmkkuplafslaqycaigushmqxcityrwukqdftkgrlst\
ncudnnuzteqjrxyafshaqljsljfunhwiqtehncpkgxspkfvbstarlsgkxfibf\
fldmerptrqlygxpfrwxtvbdgqkztmtfsqegumcfararhwerchvygczyzjaacg\
ntgvfktmjvlpmkflpecjqtfdcclbncqwhycccbgeanyciclxncrwxofqieqmc\
shhdccughsxxvzdnhwtycmcbcrttvmurqlphxnwddkopqtehzapgpfrlkkkcp\
gadmgxdlrchvygczkerwxyfpawefsawukmefgkmpwqicnhwlnihvycsxckf'

Ciphertext2 = 'cbkznkiyjsrofgnqadnzuqigscvxizgsjwucusrdkxuahgzrhywtvdjeiuwsr\
rtnpszbvpzncngztbvsrnzuqigscvfjwqgjwcytwdazuqigscvfjwqgjwjhkf\
dylmcbmhonbmbvdnvbmwbnacjaphhonbmbvdnvbmwbnaublsbdnjjneoroyfm\
xfhixpzpcozzuqigscvxcvhdmfgxmgovzsqmvzyvwyzmsczoajsejifoakdcr\
ehwhgdehvmtnmvvmesvzifutzfjzoalwqztunwvdvmfhesvzifutzfjzoalwq\
ztunpsnoyfleoxdetbwfsoyfjmfhjuxuagnarsfqydoyfjzsrzeujmfhjuubi\
hrjdfinwsnepcawdnkbobvnmzucmghijjmbscjejnapddehlmqddmfxncqbfp\
xwfejifpqzhikiyaiozimubwuzufazsdjwdiudzmztivcmgp'

key_length1 = length(Ciphertext1)
keyResult1 = getKey(Ciphertext1,key_length1)
keyResult1 = ''.join(keyResult1)
ClearText1 = vigenerecipher.decode(Ciphertext1,keyResult1)

key_length2 = length(Ciphertext2)
keyResult2 = getKey(Ciphertext2,key_length2)
keyResult2 = ''.join(keyResult2)
ClearText2 = vigenerecipher.decode(Ciphertext2,keyResult2)

print("密文1密钥长度: ",key_length1)
print("密文1key: ",keyResult1)
print("密文1明文：" , ClearText1)


print("密文2密钥长度: ",key_length2)
print("密文2key: ",keyResult2)
print("密文2明文：" , ClearText2)