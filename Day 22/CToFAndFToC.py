def CtoF(c):
    print(F"{c} Celcius = {round(((c * 9/5) + 32), 2)} Fahrenheit")

def FToC(f):
    print(F"{f} Fahrenheit = {round(((f - 32) * 5/9), 2)} Celcius") 

def main():
    while True:
        print('\n')
        print("Pilih konversi")
        print("1. Celcius to Fahrenheit")
        print("2. Fahrenheit to Celcius")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            c = input("Masukkan nilai celcius: ")
            CtoF(int(c))
        elif choice == '2':
            f = input("Masukkan nilai fahrenheit: ")
            FToC(int(f))
        elif choice == '3':
            print("Terimakasih telah mencoba")
            break
        else:
            print("Silahkan masukkan sesuai dengan no di menu")

if __name__ == '__main__':
    main()


