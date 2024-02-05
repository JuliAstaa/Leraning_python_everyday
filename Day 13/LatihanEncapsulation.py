"""

Tentu, berikut adalah sebuah contoh soal tentang encapsulation:

Soal:

Buatlah sebuah kelas Car yang merepresentasikan sebuah mobil dengan atribut brand, model, dan speed. Implementasikan encapsulation untuk memastikan bahwa nilai speed hanya dapat diakses dari dalam kelas Car dan tidak dapat diubah secara langsung dari luar kelas. Berikan juga metode accelerate() untuk meningkatkan kecepatan mobil.

Instruksi:

1. Buat kelas Car dengan atribut brand, model, dan speed. Pastikan nilai speed tidak bisa diakses secara langsung dari luar kelas.
2. Berikan metode accelerate() untuk meningkatkan nilai speed sebesar 10 setiap kali dipanggil.
3. Uji kelas Car dengan membuat objek mobil, menampilkan informasi tentang mobil tersebut, dan mempercepat mobil beberapa kali.
"""

class Car: 
    def __init__(self, brand: str, model:str, speed: int):
        self.brand = brand
        self.model = model
        self.__speed = speed
    
    def CarInformation(self):
        print(F"Brand: {self.brand}")
        print(F"Model: {self.model}")
        print(F"Speed: {self.__speed}")
        print()
    
    def accelerate(self):
        self.__speed += 10
        print("Accelerate")
        print(F"Speed: {self.__speed}KM/H")
        print()
    
Ford = Car(brand='Ford', model='Mustang', speed=0)
Ford.CarInformation()

Ford.accelerate()
Ford.accelerate()
Ford.accelerate()