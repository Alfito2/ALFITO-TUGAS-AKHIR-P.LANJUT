from produk import Produk, Buku, Baju

class TokoOnline:
    """Kelas untuk toko online."""

    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_produk = []

    def add_produk(self, produk):
        """Metode untuk menambahkan produk ke toko."""
        self.daftar_produk.append(produk)

    def hitung_total_pembelian(self):
        """Metode untuk menghitung total pembelian."""
        total = 0
        for produk in self.daftar_produk:
            total += produk.get_harga_diskon(10)  # Diskon 10% untuk semua produk
        return total

def main():
    """Fungsi utama untuk menjalankan program."""

    toko1 = TokoOnline("Toko Alfito")

    buku1 = Buku("Buku Pemrograman Python", 100000)
    baju1 = Baju("Kaos nike", 50000)
    baju2 = Baju("kaos adidas", 100000)
    buku2 = Buku("buku agama", 10000)

    toko1.add_produk(buku1)
    toko1.add_produk(baju1)
    toko1.add_produk(baju2)
    toko1.add_produk(buku2)

    total_pembelian = toko1.hitung_total_pembelian()
    print(f"nama produk: {baju1.nama}:" )
    print(f"Total pembelian di {toko1.nama_toko}: Rp{50000:,}")
    print(f"nama produk: {baju2.nama}" )
    print(f"Total pembelian di {toko1.nama_toko}: Rp{100000:,}")


if __name__ == "__main__":
    main()
