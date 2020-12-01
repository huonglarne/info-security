def gcd(p,q):
    '''
    Create the gcd of two positive integers.
    '''
    while q != 0:
        p, q = q, p%q
    return p

def key_gen(p, q, e=None, d=None):
    '''
    Generate RSA key pair
    :param p: prime number
    :param q: prime number
    :param e: public key, optional
    :param d: private key, optional
    :return:
        N: common key
        e: public key
        d: private key

    '''
    N = p * q
    phi_N = (p - 1) * (q - 1)

    if e==None and d==None:
        for i in range(phi_N):
            if i > 1 and gcd(i, N) == 1 and gcd(i, phi_N) == 1:
                for t in range(i, 50000):
                    if (i * t) % phi_N == 1 and t > i:
                        break
                break
    else:
        if e == None and d != None:
            i = d
        elif e != None and d == None:
            i = e
        t=0
        while True:
            if (i * t) % phi_N == 1 and t > i:
                break
            t+=1

    return N, i, t

if __name__ == '__main__':
    p = 227
    q = 58

    # print(key_gen(p=5, q=11))
    # print(key_gen(p=17, q=211, e=89))
    # print(key_gen(p=31, q=19, d=79))

    n, e, d = key_gen(p=31, q=19, d=79)
    m = 254 # message
    s = m**d %n # signature
    print((m == s**e %n)) # decrypted
