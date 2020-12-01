def key_exchange(p, g, a, b):
    '''
    Key exchange algorithm
    :param p: modulo, prime number
    :param g: base, primitive root of p
    :param a: secret number of person A
    :param b: secret number of person B
    :return:
    '''

    A = g**a%p
    B = g**b%p

    s1 = B**a%p
    s2 = A**b%p

    return (s1==s2), s1, s2

if __name__ == '__main__':
    print(key_exchange(23, 5, 4, 3))

    # g is a primitive root modulo n if
    # for every integer a coprime to n
    # there is an integer k such that gk ≡ a (mod n)