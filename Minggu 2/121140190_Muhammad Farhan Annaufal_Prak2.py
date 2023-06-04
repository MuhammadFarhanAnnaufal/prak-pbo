class Biodata:
    def __init__(self, nama, nim, kelas_siakad, jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.kelas_siakad = kelas_siakad
        self.jumlah_sks = jumlah_sks
    
    def data_saya(self):
        print("Nama : ", self.nama)
        print("NIM : ", self.nim)
        print("Kelas Siakad : ", self.kelas_siakad)
        print("Jumlah SKS : ", self.jumlah_sks)
    
    def tentang_saya(self):
        print("Saya berumur 19 Tahun. Saya menyukai olahraga. Hitam adalah warna kesukaan saya.")
        print("Harapan saya sekarang adalah dapat melaksanakan proses perkuliahan dengan lancar dan dapat lulus tepat waktu")
    
Saya = Biodata("Muhammad Farhan Annaufal", "121140190", "RD", "4")

Saya.data_saya()
Saya.tentang_saya()
