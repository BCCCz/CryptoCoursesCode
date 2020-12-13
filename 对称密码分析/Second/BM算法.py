def Berlekamp_Massey_algorithm(sequence):
    global i
    N = len(sequence)
    s = sequence[:]
    for i in range(N):
        if s[i] == 1:
            break
    f = {i + 1, 0}

    D=[]
    print('fn:',f,'n=',i+1)
    l = i + 1
    for v in range(i):
        D.append(0)
    D.append(1)
    print('d:',D)
    print('-----------------------------------------------------------------------')
    g = {0}
    b = 0

    for n in range(i + 1, N):
        d = 0
        for ele in f:
            d = s[n-ele]^d
            #print(d)
       # print(d)
        D.append(d)
       # print(D)
       # print('****************************')
        if d == 0:
            b += 1
        else:


             b = b+1
             temp = f.copy()
             f = set([b + ele for ele in g]) ^ f
             l2 = l
             l = max(n + 1 - l,l)
             if(l2!=l):
                b = 0
                g = temp
        print('fn:', f, 'n=', n+1)
        #print(f)
        print('-----------------------------------------------------------------------')
    print('d:',D)
    return (poly(f), l)

# 输出多项式
def poly(polynomial):
    result = ''
    lis = sorted(polynomial, reverse=True)
    for i in lis:
        if i == 0:
            result += '1'
        else:
            result += 'x^%s' % str(i)
        if i != lis[-1]:
            result += ' + '
    return result

if __name__ == '__main__':
    #seq1 = (1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1)
   # seq2 = (0,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1)
    #seq3 = (1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0)
    sequence = (1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0)
    output = Berlekamp_Massey_algorithm(sequence)
    print(output)
