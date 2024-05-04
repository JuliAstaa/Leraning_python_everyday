text = input("Masukkan kata yang mau di konversi ke biner: ")
biner = []
for char in text:
    biner.append(bin(ord(char))[2:])
print(" ".join(biner))