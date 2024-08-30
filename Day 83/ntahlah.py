import time
import random
import string

hello_world = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]

# Jumlah iterasi acak sebelum menampilkan huruf sebenarnya
random_iterations = 7

# Loop melalui setiap nilai ASCII dalam daftar
for num in hello_world:
    # Acak dan tampilkan beberapa huruf sebelum huruf sebenarnya
    for _ in range(random_iterations):
        random_char = random.choice(string.ascii_letters + string.punctuation + string.digits + ' ')
        print(random_char, end='', flush=True)
        time.sleep(0.05)
        print('\b', end='', flush=True)  # Hapus karakter yang baru saja ditampilkan

    # Tampilkan huruf sebenarnya
    print(chr(num), end='', flush=True)
    time.sleep(0.1)

print()  # Untuk memastikan kursor pindah ke baris baru setelah selesai

