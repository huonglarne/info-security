import math

# function to shift bits to the left
def rotation(x, times):
    if times == 0:
        return [t for t in x]
    else:
        temp = x[0]
        new = [x[i + 1] for i in range(len(x)-1)]
        new.append(temp)
        return rotation(new, times-1)

# function to convert string to list of 0 and 1
def split(string):
    return [int(char) for char in string]

string_k = ['5A827999', '6ED9EBA1', '8F1BBCDC', 'CA62C1D6']

# k for each stage
k1 = [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
k2 = [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1]
k3 = [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
k4 = [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]

# function to convert string binary to list of 0 and 1
def bin_to_list(string):
    t = "{0:08b}".format(int(string, 16))
    list = [int(each) for each in t]
    while len(list)<32:
        list.insert(0,0)
    return list

# function to add 2 lists of 0 and 1 as 2 binary number
# returns a list
def add_bin(list1, list2):
    a=''.join(str(x) for x in list1)
    b=''.join(str(x) for x in list2)
    sum = int(a, 2) + int(b, 2)
    return bin_to_list(bin(sum))

# W is a 512 bit block
# W is consisted of 16 words, each has 32 bits
W = [[0 for i in range(32)] for t in range(15)]
W16 = [0 for i in range(31)]
W16.append(1)
W.append(W16)

# function to extend W from 16 words to 80 words
def extend(W):
    for j in range(16, 80):
        temp = [a^b for a,b in zip(W[j-16],W[j-14])]
        temp = [a^b for a,b in zip(temp,W[j-8])]
        temp = [a^b for a,b in zip(temp,W[j-3])]
        W.append(rotation(temp, 1))

extend(W)

# initial hash values
A = [0 for i in range(32)]
B = [0 for i in range(32)]
C = [0 for i in range(32)]
D = [0 for i in range(32)]
E = [0 for i in range(32)]

# iterations of the main loop
# Dr. Huong may only ask for the result of the 1st iteration
# print and pause the loop to your liking
for i in range(0, 79):
    if 0<=i and i<=19:
        f = [((b&c) | (~b&d)) for b,c,d in zip(B,C,D)]
        k = k1
    elif 20<=i and i<=39:
        f = [b^c^d for b,c,d in zip(B,C,D)]
        k = k2
    elif 40<=i and i<=59:
        f = [((b&c) | (b&d) | (c&d)) for b,c,d in zip(B,C,D)]
        k = k3
    else:
        f = [b^c^d for b,c,d in zip(B,C,D)]
        k = k4
    temp = add_bin(rotation(A, 5), f)
    temp = add_bin(temp, E)
    temp = add_bin(temp, k)
    temp = add_bin(temp, W[i])
    E = D
    D = C
    D = rotation(B, 30)
    B = A
    A = temp
    

