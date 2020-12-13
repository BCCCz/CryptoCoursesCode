from Crypto.Util.number import inverse
import copy

def Attack_BM(b):
	a=[]  #表示输入的序列
	for i in range(len(b)):
		if b[i]=='1':
			a.append(1)
		else:
			a.append(0)

	Fnx=[] #Fnx表示多项式的二元列表,Fnx中的列表表示幂次从小到大的多项式  Fnx=c0+c1*pow(x,l0)+c2*pow(x,l1)+.......---
	ln=[]#ln表示多项式各项的幂次
	#初始化 f0(x)=1 l0=0
	F0x=[1]
	l0=0
	#添加进
	ln.append(l0)
	Fnx.append(F0x)
	k=0
	flag=0   #用来判断l0,l1,l2,..ln是否相等的flag

    #计算d
	while k<len(a):
		d=0 #用来表示第n步的差值
		for i in range(ln[k]+1):
			d+=Fnx[k][i]*a[k-ln[k]+i]  #d=c0*a_n+c1*a_n-1+c2*a_n-2+.....
		d=d%2 #模2加 ->d=0或d=1

        #根据d的取证分类讨论
		#下面分两种大情况讨论 d=0
		if d==0: #F_n+1(x)=F_n(x),l_n+1=l_n
			Fnx.append(Fnx[k])
			ln.append(ln[k])
			k+=1

        #d=1
		else: # 再分两种小情况：l0=l1=l2=..... / 存在m使得 lm<lm+1=lm+2=...=ln
			flag+=1
			if flag==1:
				ln.append(k+1) #ln=n+1
				#Fn+1(x)=1+pow(x,n+1)
				Fx=[0]*(k+2)
				Fx[0]=1
				Fx[k+1]=1
				Fnx.append(Fx)
				k+=1
			else:
				#找到m使得 lm<lm+1=lm+2=...=ln
				for i in range(k+1):
					if ln[k]>ln[k-i]:
						m=k-i
						break

				#参考ppt BM攻击 p25
				if m-ln[m]>=k-ln[k]: #取fn+1(x)=fn(x)-....
					fnx1=copy.deepcopy(Fnx[k])
					fnx2=copy.deepcopy(Fnx[m])
					for i in range(m-ln[m]-k+ln[k]):
						fnx2.insert(0,0)
					for j in range(len(fnx2)):
						fnx1[j]=(fnx1[j]+fnx2[j])%2
					Fnx.append(fnx1)
					ln.append(ln[k])
					k+=1
				else: #k-lk>m-lm 取fn+1(x)=x......
					fnx1=copy.deepcopy(Fnx[k])
					for i in range(k-ln[k]-m+ln[m]):
						fnx1.insert(0,0)
					fnx2=copy.deepcopy(Fnx[m])
					for j in range(len(fnx2)):
						fnx1[j]=(fnx1[j]+fnx2[j])%2
					Fnx.append(fnx1)
					ln.append(len(fnx1)-1)
					k+=1
	return Fnx[-1]


def output(res):
	for i in range(len(res)-1):
		if(res[i]==1):
			print("x^"+str(i)+'+',end='')
	print("x^"+str(len(res)-1))

if __name__ == "__main__":
	b = ['10010000111101000011100000011','00001110110101000110111100011','10101111010001001010111100010']
	for i in b:
		res = Attack_BM(i)
		print(i+'的最短LFSR的特征多项式为:',end = '')
		output(res)
