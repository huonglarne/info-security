def shift(x, type=None):
    new = [x[i-1] for i in range(len(x))]
    
    if type=='x':
        new_bit = new[18] ^ new[17] ^ new[16] ^ new[13]
    if type=='y':
        new_bit = new[21] ^ new[20]
    if type=='z':
        new_bit = new[22] ^ new[21] ^ new[20] ^ new[7]
        
    new[0] = new_bit
    return new

def key_gen(x,y,z,l):
    key = []
    for i in range(l):
        key.append(x[-1] ^ y[-1] ^ z[-1])
        clock = round((x[8] + y[10] + z[10])/3)

        if x[8]==clock:
            x = shift(x, 'x')
        if y[10]==clock:
            y = shift(y, 'y')
        if z[10]==clock:
            z = shift(z, 'z')
    print(x,y,z)
    return key

def split(string):
    return [int(char) for char in string]

x = split('0100010001000100010')
y = split('0011001100110011001111')
z = split('11100001111000011110000')

l = 3

key = key_gen(x,y,z,l)
print(key)