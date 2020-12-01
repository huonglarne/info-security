N = 8

S = [i for i in range(N)]
key = [3, 1, 4, 1, 5]
K = [key[i%len(key)] for i in range(N)]

print('K: ', K)


# key scheduling
j = 0

for i in range(N):
    j = (j + S[i] + K[i]) % N

    x = S[i]
    S[i] = S[j]
    S[j] = x

print('New S:', S)

# stream generation

i = j = 0

# P = [6, 1, 3, 8]
# len(P)+1
stream = []
for t in range(20): # 20 is desired length of the stream
    i = (i+1) % N
    j = (j + S[i]) % N

    x = S[i]
    S[i] = S[j]
    S[j] = x

    t = (S[i] + S[j]) % N
    stream.append(S[t])

print('Stream: ',stream)

