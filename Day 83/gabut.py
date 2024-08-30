import time
import random
import string

print(random.__file__)

selamat_siang = [83,101,108,97,109,97,116,32,83,105,97,110,103,33]
random_kemunculan = 10

for huruf in selamat_siang:
    for i in range(random_kemunculan):
        huruf_acak = random.choice(string.ascii_letters + string.punctuation + string.digits)
        print(huruf_acak, end="", flush=True)
        time.sleep(0.05)
        print('\b', end="", flush= True)

    print(chr(huruf), end='', flush=True)
    time.sleep(0.1)

print()
