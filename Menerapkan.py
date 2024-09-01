# Kelas yang hanya bertanggung jawab untuk menyimpan data pemesanan
class DataPemesanan:
    def __init__(self, nomor_penerbangan, nama_penumpang, kelas_duduk, harga_dasar, jumlah_tiket):
        self.nomor_penerbangan = nomor_penerbangan
        self.nama_penumpang = nama_penumpang
        self.kelas_duduk = kelas_duduk
        self.harga_dasar = harga_dasar
        self.jumlah_tiket = jumlah_tiket

# Kelas yang hanya bertanggung jawab untuk menghitung total harga
class PenghitungHarga:
    @staticmethod
    def hitung_total_harga(data_pemesanan):
        pengali_kelas = 1.0
        if data_pemesanan.kelas_duduk == "Bisnis":
            pengali_kelas = 1.5
        elif data_pemesanan.kelas_duduk == "First":
            pengali_kelas = 2.0
        
        total_harga = data_pemesanan.harga_dasar * pengali_kelas * data_pemesanan.jumlah_tiket
        return total_harga

# Kelas yang hanya bertanggung jawab untuk mencetak detail pemesanan
class PencetakPemesanan:
    @staticmethod
    def cetak_detail_pemesanan(data_pemesanan, total_harga):
        print(f"Nomor Penerbangan: {data_pemesanan.nomor_penerbangan}")
        print(f"Nama Penumpang: {data_pemesanan.nama_penumpang}")
        print(f"Kelas Duduk: {data_pemesanan.kelas_duduk}")
        print(f"Jumlah Tiket: {data_pemesanan.jumlah_tiket}")
        print(f"Total Harga: Rp{total_harga}")

# Kelas yang hanya bertanggung jawab untuk menyimpan dan mengelola data pemesanan
class RepositoryPemesanan:
    def __init__(self):
        self.pemesanan = []

    def simpan_pemesanan(self, data_pemesanan):
        self.pemesanan.append(data_pemesanan)

    def ambil_semua_pemesanan(self):
        return self.pemesanan


# Contoh Penggunaan
data_pemesanan = DataPemesanan("AB123", "Wisnu Parijata", "Bisnis", 5000000, 2)  # Membuat data pemesanan
penghitung_harga = PenghitungHarga()  # Menghitung harga
total_harga = penghitung_harga.hitung_total_harga(data_pemesanan)
PencetakPemesanan.cetak_detail_pemesanan(data_pemesanan, total_harga)  # Mencetak detail pemesanan

# Menyimpan pemesanan
repository_pemesanan = RepositoryPemesanan()
repository_pemesanan.simpan_pemesanan(data_pemesanan)
print(repository_pemesanan.ambil_semua_pemesanan())  # Mengambil semua pemesanan
