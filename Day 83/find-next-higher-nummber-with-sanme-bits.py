""" 
Your task is to find the next higher number (int) with the same number of '1'- Bits.

I.e. as many 1 bits as before and output next higher than input. Input is always an int between 1 and 1<<30 (possibly inclusive). No bad cases or special tricks...

Some easy examples:
Input: 129  => Output: 130 (10000001 => 10000010)
Input: 127 => Output: 191 (01111111 => 10111111)
Input: 1 => Output: 2 (01 => 10)
Input: 323423 => Output: 323439 (1001110111101011111 => 1001110111101101111)
"""

def next_higher(n):
    c = n
    c0 = c1 = 0

    # Hitung bit 0 di paling kanan (c0) dan bit 1 setelahnya (c1)

    while ((c & 1) == 0 ) and (c != 0):
        c0 += 1
        c>>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>=1

    #Jika semua bit adalah 1 dan 0, maka tidak ada angka yang lebih besar

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1
    
    #Temukan posisi bit yang akan di geser
    position = c0 + c1

    #setel bit 0 pada posisi tersebut menjadi 1
    n |= (1 << position)

    #hapus semua bit di kanan posisi ini
    n &= ~((1 << position) - 1)

    #tambhak  kembali bit 1 yang telah dipindahkan

    n|= (1 << (c1 -1) ) -1

    return n

print(next_higher(129))

x = 5
result = x << 3
print(bin(x)[2:])
print(bin(result)[2:])