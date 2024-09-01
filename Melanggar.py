class PemesananPenerbangan:
    def __init__(self, nomor_penerbangan, nama_penumpang, kelas_tempat_duduk, harga_dasar, jumlah_tiket):
        self.nomor_penerbangan = nomor_penerbangan
        self.nama_penumpang = nama_penumpang
        self.kelas_tempat_duduk = kelas_tempat_duduk
        self.harga_dasar = harga_dasar
        self.jumlah_tiket = jumlah_tiket
        self.pemesanan = []

    def hitung_total_harga(self):
        pengali_kelas = 1.0
        if self.kelas_tempat_duduk == "Bisnis":
            pengali_kelas = 1.5
        elif self.kelas_tempat_duduk == "Pertama":
            pengali_kelas = 2.0
        
        total_harga = self.harga_dasar * pengali_kelas * self.jumlah_tiket
        return total_harga

    def cetak_rincian_pemesanan(self):
        print(f"Nomor Penerbangan: {self.nomor_penerbangan}")
        print(f"Nama Penumpang: {self.nama_penumpang}")
        print(f"Kelas Tempat Duduk: {self.kelas_tempat_duduk}")
        print(f"Jumlah Tiket: {self.jumlah_tiket}")
        print(f"Total Harga: Rp{self.hitung_total_harga()}")

    def simpan_pemesanan(self):
        self.pemesanan.append({
            'nomor_penerbangan': self.nomor_penerbangan,
            'nama_penumpang': self.nama_penumpang,
            'kelas_tempat_duduk': self.kelas_tempat_duduk,
            'harga_dasar': self.harga_dasar,
            'jumlah_tiket': self.jumlah_tiket
        })

    def dapatkan_semua_pemesanan(self):
        return self.pemesanan


pemesanan = PemesananPenerbangan("AB123", "Wisnu Parijata", "Bisnis", 5000000, 2) 
pemesanan.hitung_total_harga()
pemesanan.cetak_rincian_pemesanan()
pemesanan.simpan_pemesanan()
print(pemesanan.dapatkan_semua_pemesanan())
