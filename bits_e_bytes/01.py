# Converter bytes para bits
 
def bytes2bits(bytes: int): 
    return bytes * 8

# Converter bits para bytes

def bits2bytes (bits: int):
    return bits // 8


# Exemplos de usos:
intbytes = 4 
intbits = 64

print (f'{intbytes} bytes = {bytes2bits(intbytes)} bits')
print (f'{intbits} bits = {bits2bytes (intbits)} bytes')