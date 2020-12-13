import scipy
from scipy.special import comb
import sys, time
import random
import re

an=[[0 for i in range(9)]for i in range(180)]
xn=[0 for i in range(4000000)]
assumeright=[0 for i in range(4000000)]


def ReadFile(filename):
    datafile=open(filename)
    try:
        text=datafile.read()
        return eval('['+text[4:-1]+']')
    finally:
        datafile.close()
def WriteFile(filename):
    try:
        file_object = open(filename, 'w')
        file_object.write('0.75\n'+str(xn).replace(' ','')[1:-1]+',')
    finally:
        file_object.close()


def CreatePoly(n):
    imax=0
    count=0
    a0 = [1, 4, 13, 23, 25, 44, 51, 57, 60]
    ai=[[1, 4, 13, 23, 25, 44, 51, 57, 60] for i in range(20)]
    while pow(2,imax)*60<4000000:
        for j in range(9):
            ai[imax][j] = pow(2, imax) * a0[j]
        imax=imax+1
    for i in range(imax):
        for j in range(9):
            offset=n-ai[i][j]
            if offset>=0:
                if ai[i][8]+offset>=4000000:
                    continue
                for z in range(9):
                    an[count][z]=ai[i][z]+offset
                count=count+1
    #print("成功生成",count,"个校验方程")
    #for i in range(count):
    #    print (an[i])
    return count

def CalusS(p,t):
    return (pow(2*p-1,t-1)*(p-0.5)+0.5)

def CalcuQ(p,M,h,S):
    Q=0
    #for 0 in range(H+1):
    for i in range(h,M+1):
        Q=comb(M,i)*(p*pow(S,i)*pow((1-S),M-i)+(1-p)*pow(1-S,i)*pow(S,M-i))+Q
    return Q

def CalcuT(p,M,h,S,Q):
    T=0
    for i in range(h,M+1):
        T=comb(M,i)*(p*pow(S,i)*pow((1-S),M-i))/Q+T
    return T

def findHmax(p,M,S):
    Hmax=0
    for i in range(M):
        #if CalcuT(p,M,i,S,CalcuQ(p,M,i,S))*4000000>=60:
        if CalcuQ(p,M,i,S)*4000000>=60:
            Hmax=i
    return Hmax

def GetEvenVerify(n):

    M=CreatePoly(n)
    #S = CalusS(0.75, 8)
    #Hmax = findHmax(0.75, M, S)
    currentnum=0
    for j in range(M):
        if data[an[j][0]]^data[an[j][1]]^data[an[j][2]]^data[an[j][3]]^data[an[j][4]]^\
                data[an[j][5]]^data[an[j][6]]^data[an[j][7]]^data[an[j][8]]==0:
            currentnum=currentnum+1
    #if currentnum>=Hmax:
     #   xn[n]=1
    if n%10000==0:
        print("checking", n, "th bit", currentnum, Hmax, M)
    xn[n]=currentnum
    #elif currentnum/Hmax<0.6 and random.random()>0.85:
    #    data[n] = 1 - data[n]
    #elif  random.random()>0.95:
    #    data[n] = 1 - data[n]



def FindSumMax():
    summax=0
    Sum=0
    Sum=sum(xn[:60])
    maxn=0
    for i in range(1,3999938):
        Sum=Sum-xn[i-1]+xn[i+59]
        if Sum>summax:
            summax=Sum
            maxn=i
            print("have max sum from n:",maxn)

def CheckResult():
    data = ReadFile("D:\CODE\CryptoCoursesCode\CryptoCoursesCode\对称密码分析\Third\data.txt")
    temp=assumeright[2026839:2026898]=data[2026839:2026898]
    rare = ReadFile("D:\CODE\CryptoCoursesCode\CryptoCoursesCode\对称密码分析\Third\data.txt")
    count=0
    changecount=0
    while count/(3999940-2026839)<0.7 or count/(3999940-2026839)>0.8:
        count = 0
        for i in range(2026839, 3999940):
            assumeright[i + 60] = assumeright[i + 1] ^ assumeright[i + 4] ^ assumeright[i + 13] ^ assumeright[i + 23] ^ \
                                  assumeright[i + 25] ^ assumeright[i + 44] ^ assumeright[i + 51] ^ assumeright[i + 57]
            if assumeright[i] == rare[i]:
                count = count + 1
        print(count/(3999940-2026839),changecount)
        assumeright[2026839:2026898]=temp
        assumeright[2026839+changecount]=1-assumeright[2026839+changecount]
        changecount=changecount+1





M=CreatePoly(1000000)
S=CalusS(0.75,8)
Q=CalcuQ(0.75,M,80,S)
T=CalcuT(0.75,M,80,S,Q)
print(M,Q,T)

#Hmax=findHmax(0.75,M,S)

#data = ReadFile("data-1.txt")
#print(data[2026839:2026898])
CheckResult()
#for i in range(3999999):
#    GetEvenVerify(i+1)
#FindSumMax()
#WriteFile("data-1 迭代后统计.txt")



