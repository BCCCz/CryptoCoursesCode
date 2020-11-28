def Berlekamp_Massey_algorithm(sequence):
    N = len(sequence)
    s = sequence[:]
    for k in range(N):
        if s[k] == 1:
            break
    f = set([k + 1, 0])
    l = k + 1
    g = set([0])
    a = k
    b = 0
    for n in range(k + 1, N):
        d = 0
        for ele in f:
            d ^= s[ele + n - l]
        if d == 0:
            b += 1
        else:
            if 2 * l > n:
                f ^= set([a - b + ele for ele in g])
                b += 1
            else:
                temp = f.copy()
                f = set([b - a + ele for ele in f]) ^ g
                l = n + 1 - l
                g = temp
                a = b
                b = n - l + 1
    return (print_poly(f), l)

# output the polynomial
def print_poly(polynomial):
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
    seq1 = (1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1)
    seq2 = (0,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1)
    seq3 = (1,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0)

    output1 = Berlekamp_Massey_algorithm(seq1)
    output2 = Berlekamp_Massey_algorithm(seq2)
    output3 = Berlekamp_Massey_algorithm(seq3)
    print(output1)
    print(output2)
    print(output3)
