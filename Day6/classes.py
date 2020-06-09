siswas = []


class Siswa:
    def __init__(self, name, age, alamat):
        self.name = name
        self.age = age
        self.alamat = alamat

        siswas.append(self)

    def perkenalan(self):
        print(self.name, self.age, self.alamat)

    @classmethod
    def new_siswa(cls):
        name = input("Masukkan Nama Siswa: ")
        age = input("Masukkan Umur Siswa: ")
        alamat = input("Masukkan Alamat Siswa: ")

        return cls(name, age, alamat)


siswa1 = Siswa("kenny", "17", "surga")
siswa1.perkenalan()

for x in range(3):
    Siswa = Siswa.new_siswa()

for siswa in siswas:
    print(siswa)
