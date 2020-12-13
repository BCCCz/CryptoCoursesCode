import scipy
import sys,time
from scipy.special import comb
import re
import math

N=4000000   #序列数
n=60    #级数
p=0.75   #相关概率
fx=[3,9,16,35,37,47,56,60]           #反馈多项式的系数
# fx=[1,2,3,5]
t=len(fx)                            #计算抽头数



#读取序列z
def ReadFile(filename):
    datafile=open(filename)
    try:
        text=datafile.read()
        return eval('['+text[4:-1]+']')
    finally:
        datafile.close()

def writeFile(filename):
    try:
        file_object = open(filename, 'w')
        file_object.write('0.75\n'+str(data).replace(' ','')[1:-1]+',')
    finally:
        file_object.close()


M=round(math.log(N/(2*n),2)*(t+1))   #计算每位平均需要校验方程数
imax=math.floor(math.log(N/n,2))
an = [[0 for i in range(t + 1)] for i in range(3 * M)]  # 用于存储最终校验多项式
# print(imax)
def CreatePoly(w):                          #w为检测第几位
    imax=math.floor(math.log(N/n,2))   #乘方的最大值
    count=0                #记录校验方程的个数
    a1=[[0 for i in range(t)]for i in range(imax+1)]     #用以保存校验方程的序号
    a1[0]=fx
    #生成倍式（第一行为原反馈多项式）
    for i in range(1,imax+1):
        for j in range(t):
            a1[i][j]=a1[0][j] * pow(2,i)
    # print(a1)
    #生成校验方程
    a2=[[0 for i in range(t+1)]for i in range(imax+1)]
    # print(a2)
    for column in range(imax+1):                         #将校验等式左边写进a2的最后一列
        a2[column][t]=a1[column][t-1]
    # print(a2)
    for i in range(imax+1):
        for j in range(t):
            a2[i][t-j-1]=a2[i][t]-a1[i][j]
    # print(a2)

    for i in range(imax+1):
        for j in range(t+1):
            if w>=a2[i][j]:
                offset=w-a2[i][j]
                if (offset+a2[i][t])>N:
                    continue
                else:
                    for k in range(t+1):
                        an[count][k]=offset+a2[i][k]
                    count=count+1

    return count            #返回校验方程总数



def findBite1():
    data = ReadFile("data-1.txt")
    for w in range(1000000):
        a=CreatePoly(w)
        if a>=92:
            for i in range(3*M):
                if data[an[i][0]]^data[an[i][1]]^data[an[i][2]]^data[an[i][3]]^data[an[i][4]]^\
                data[an[i][5]]^data[an[i][6]]^data[an[i][7]]==data[an[i][8]]:
                    f=open("test1.txt",'a')
                    f.write(str(an[i])+',')
                    print(an[i])
                    f.close()

def findBite2():
    f = open("test2.txt")
    a = f.read()
    data = eval(a)
    f.close()
    b = len(data)
    an = [[0 for i in range(60)]]
    for i in range(60):
        count = 0
        for k in range(10000):
            for j in range(9):
                if data[k][j] == 12800 + i:
                    an[i] = 12800 + i
                    count = count + 1
                    print("找到", count, "个了")
                    break

    print(an)


#step 1:
M=round(math.log(N/(2*n),2)*(t+1))   #计算每位平均需要校验方程数

#step 2:
def S(p,t):
    if t==1:
        return p
    return p*S(p,t-1)+(1-p)*(1-S(p,t-1))

#step 3:

def Q(p,M,h):
   q=0
   for i in range(h,M+1):
       q=comb(M,i)*(p*pow(S(p,t),i)*pow((1-S(p,t)),M-i)+(1-p)*pow(1-S(p,t),i)*pow(S(p,t),M-i))+q
   return q

# print(Q(p,M,1))

#step 4:
def V(p,M,h):
    v=0
    for i in range(h, M + 1):
        v = comb(M, i) * (p * pow(S(p,i), i) * pow((1 - S(p,i)), M - i)) + v
    return v

def T(p,M,h):
    t=V(p,M,h)/Q(p,M,h)
    return t

#step 5:
def findHmax():
    hmax=0
    for h in range(1,M+1):
        if Q(p,M,h)*N>=n:
            hmax=h
    return hmax

def calR():
    r=(1-T(p,M,h=92))*n
    return r

#step 6:
def findBite():
    findBite()




#从python下标为n的位的连续60个数组
def Prospective(n,zn_temp2):
    point=n
    #print(zn_temp)
    zn_temp=zn_temp2.copy()
    while point:
        temp=zn_temp[3]^zn_temp[12]^zn_temp[22]^zn_temp[24]^zn_temp[43]^zn_temp[50]^zn_temp[56]^zn_temp[59]
        zn_temp.insert(0,temp)
        zn_temp.pop()
        point=point-1
    #print(zn_temp)
    return zn_temp

def LastCheck(zn_temp):
    count_right=0
    point=60
    while point<=4000000-1:
        temp =zn_temp[0]^ zn_temp[4] ^ zn_temp[13] ^ zn_temp[23] ^ zn_temp[25] ^ zn_temp[44] ^ zn_temp[51] ^ zn_temp[57]
        zn_temp.append(temp)
        zn_temp=zn_temp[1:]
        if(zn_temp[59]==zn[point]):
            count_right=count_right+1
        point=point+1
    return count_right/(4000000-60)

def ChangeHaming(zn_temp):
    flag=1
    count=0
    zn_temp_copy=zn_temp.copy()
    while flag and count<=59:
        Pros_zn=Prospective(12800, zn_temp_copy)
        result=LastCheck(Pros_zn)
        print(result,count)
        print('开头序列',Pros_zn)
        print('选取序列',zn_temp_copy)
        if result>0.8 or result<0.70:
            zn_temp_copy=zn_temp.copy()
            zn_temp_copy[count]=zn_temp_copy[count]^1
            count=count+1
        else:
            flag=0




zn=ReadFile('D:\CODE\CryptoCoursesCode\CryptoCoursesCode\对称密码分析\Third\data.txt')
#zn_temp=Prospective(12800,zn[n:n+60])
ChangeHaming(zn[n:n+60])