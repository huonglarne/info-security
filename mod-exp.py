# convert the exponent to binary
# return a list of its bits
def to_binary(n):
    return [int(i) for i in bin(n)[2:]] 

# x is the base
# e is the exponent
# n is the modulo
def sq_mul(x, e, n):
    result = x
    bin = to_binary(e)
    
    for i in bin[1:]: # ignore the first bit
        result = result**2 % n
        if i==1:
            result = result*x % n
    return result
    
x = 8
e = 1289
n = 27 

print(sq_mul(x, e, n))