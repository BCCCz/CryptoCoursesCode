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

a = countList(Ciphertext1)
print(a)