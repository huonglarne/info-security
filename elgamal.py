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

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

p = 151
print(is_prime(p))

g = 15 # generator
d = 149 # 1<d<p-2

B = g**d %p

# public key is (p,g,B) private is d

k = 7 # k and p-1 coprime

print(gcd(k, p-1))

m = 20 # message
r = g**k %p
s = (m - d*r)*modInverse(k,p-1) %(p-1) # signature gen

t = ((B**r) * (r**s)) % p
print((t == g**m %p)) # siginature verification




# p = 79
# g = 2 # generator
# a = 3 # 1 <= g <= p-1
#
# A = g**a %p
#
# # key is (p, g, A)
#
# k = 8 # 1 <= k <= p-1
# m = 28 # m is message
#
# c1 = g**k %p
# c2 = (m* A**k) %p
#
# # receive (c1, c2)
#
# x = c1**a %p
# x1 = modInverse(x, p)
# print((m == x1 * c2 %p))