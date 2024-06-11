class Produk:
    """Kelas abstrak untuk produk."""

    def __init__(self, nama, harga_satuan):
        self.nama = nama
        self.harga_satuan = harga_satuan

    def hitung_diskon(self, diskon):
        """Metode abstrak untuk menghitung diskon produk."""
        raise NotImplementedError

    def get_harga_diskon(self, diskon):
        """Metode untuk mendapatkan harga produk setelah diskon."""
        harga_diskon = self.hitung_diskon(diskon)
        return self.harga_satuan - harga_diskon

class Buku(Produk):
    """Kelas untuk produk buku."""

    def hitung_diskon(self, diskon):
        if diskon >= 10:
            return self.harga_satuan * diskon / 100
        else:
            return 0

class Baju(Produk):
    """Kelas untuk produk baju."""

    def hitung_diskon(self, diskon):
        if diskon >= 20:
            return self.harga_satuan * diskon / 100
        else:
            return 0
