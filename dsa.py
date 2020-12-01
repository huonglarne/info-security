def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

        # Make x positive
    if (x < 0):
        x = x + m0

    return x

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

p = 179
print(is_prime(p))

def find_q(p):
    for q in range(2, p):
        if p%q == 1 and is_prime(q):
            print(q, '- q \n')

find_q(p) # choose q from the above list, q is prime

q = 89

def find_g(p, q):
    for g in range(2,p):
        mod_list = []
        for i in range(2, p):
            t = g**i%p
            if t not in mod_list:
                mod_list.append(t)
        if len(mod_list) == q:
            print(g, ' - g')

find_g(p,q)

g = 125 # choose g from the above list

d = 20 # private 0<d<q
B = g**d % p

# key public is (p, q, g, B)

k = 38 # 0<k<q

r = (g**k %p)%q
m = 126
# m is SHA(message)

s = ((m + d*r)* modInverse(k,q)) % q
# if s==0, try with another k
# signature is (r,s)

w = modInverse(s, q) % q
u1 = w*m %q
u2 = w*r %q

v = ((g**u1) * (B**u2) %p) %q
print((v == r%q))


