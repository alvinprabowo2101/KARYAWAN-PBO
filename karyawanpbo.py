class Karyawan:
    def __init__(self, id_karyawan, jabatan, kontrak, tahun_masuk):
        self.id = id_karyawan
        self.jabatan = jabatan
        self.kontrak = kontrak
        self.tahun_masuk = tahun_masuk

    def get_info(self):
        print(f"ID Karyawan : {self.id}")
        print(f"Jabatan     : {self.jabatan}")
        print(f"Kontrak     : {self.kontrak}")
        print(f"Tahun Masuk : {self.tahun_masuk}")
    
    def laporan_keuangan(self, gaji, pengeluaran, pemasukan):
        print("Laporan Keuangan Perusahaan")
        print("----------------------------")
        print(f"Total Gaji Karyawan : {gaji}")
        print(f"Total Pengeluaran   : {pengeluaran}")
        print(f"Total Pemasukan     : {pemasukan}")
    
    def jadwal_kerja(self, jadwal_masuk, jadwal_libur):
        print("Jadwal Kerja Karyawan")
        print("---------------------")
        print(f"Jadwal Masuk: {jadwal_masuk}")
        print(f"Jadwal Libur: {jadwal_libur}")
        print()
        print(f"*"*50)

# Objek 1
karyawan1 = Karyawan("K001", "Manajer", "Kontrak 2 tahun", 2018)
karyawan1.get_info()
karyawan1.laporan_keuangan(5000000, 2000000, 8000000)
karyawan1.jadwal_kerja("Senin-Jumat, 08:00-17:00", "Sabtu-Minggu")
print()

# Objek 2
karyawan2 = Karyawan("K002", "Marketing", "Kontrak 1 tahun", 2019)
karyawan2.get_info()
karyawan2.laporan_keuangan(3000000, 1500000, 6000000)
karyawan2.jadwal_kerja("Senin-Kamis, 09:00-18:00", "Jumat-Sabtu")
print()

# Objek 3
karyawan3 = Karyawan("K003", "IT Support", "Kontrak 3 tahun", 2020)
karyawan3.get_info()
karyawan3.laporan_keuangan(4000000, 2500000, 7000000)
karyawan3.jadwal_kerja("Senin-Jumat, 09:00-18:00", "Sabtu-Minggu")