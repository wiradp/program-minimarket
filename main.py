from tabulate import tabulate
import pandas as pd


class Pacmarket:
    """
    Class untuk simulasi toko Pacmarket.
    """

    def __init__(self):
        """
        Inisialisasi List Belanja

        Parameter
        ---------

        list_belanja = dict
        """
        self.list_belanja = {"Nama Barang": [], "Jumlah Barang": [
        ], "Harga Barang": [], "Total Harga": []}

    def masukkan_id(self):
        """
        Function untuk memasukkan ID Customer 

        Parameters
        ----------
        id_cust : str
            Input ID Customer.
        """
        while True:
            try:
                self.id_cust = input("Masukkan ID Anda : ")
                if not self.id_cust:
                    raise ValueError("ID tidak boleh kosong")
                break
            except ValueError as e:
                print(f"---> Error: {e}")

        pesan = f">>> Selamat datang {self.id_cust} di Pacmarket <<<"
        print("\n")
        print("-" * len(pesan))
        print(pesan)
        print("-" * len(pesan))

    def transaksi(self):
        """
        Function untuk melakukan transaksi

        Parameter
        --------

        Menu belanja = int [1,2,3,4,9]
            input menu_belanja
        """
        while True:
            confirm1 = input("\nApakah anda ingin berbelanja? (Y/N)")

            if confirm1.lower() == "n":
                self.selesai()
                break

            while confirm1.lower() == "y":
                print("\nKetik 1 Untuk Add Barang. \nKetik 2 Untuk Edit Barang. \nKetik 3 Untuk Delete Barang. \nKetik 4 Untuk Membatalkan Belanja.\nKetik 9 Untuk Check Out.")
                try:
                    menu_belanja = int(input("\nMasukkan pilihan anda: "))
                    if menu_belanja not in [1, 2, 3, 4, 9, 0]:
                        raise ValueError("Masukkan angka sesuai menu diatas")

                    if menu_belanja == 1:
                        self.tambah_barang()  # Panggil method tambah_barang

                    elif menu_belanja == 2:
                        self.edit_barang()  # Panggil method edit_barang

                    elif menu_belanja == 3:
                        self.hapus_barang()  # Panggil method hapus_barang

                    elif menu_belanja == 4:
                        self.list_belanja = self.reset_barang()  # Panggil method reset_barang

                    elif menu_belanja == 9:
                        self.check_out_barang()  # Panggil method check_out_barang
                        break

                except ValueError as e:
                    print(f"---> Error: {e}")

    def tambah_barang(self):
        """
        Function untuk melakukan penambahan barang

        Parameter
        ---------

        Nama Barang = str
            input = nama_barang
        Jumlah Barang = int
            input = jumlah_barang
        Harga Barang = int
            input = harga_barang
        """
        while True:
            nama_barang = input(
                "\nMasukkan nama barang (atau tekan Enter untuk selesai) = ")
            if not nama_barang:
                break

            jumlah_barang = self.input_nilai_positif(
                "Masukkan jumlah barang = ")
            harga_barang = self.input_nilai_positif(
                "Masukkan harga barang  = ")

            total_harga = jumlah_barang * harga_barang

            # Menambahkan barang ke dalam dictionary list belanja
            self.list_belanja["Nama Barang"].append(nama_barang)
            self.list_belanja["Jumlah Barang"].append(jumlah_barang)
            self.list_belanja["Harga Barang"].append(harga_barang)
            self.list_belanja["Total Harga"].append(total_harga)

            # Menjumlahkan Total Harga pada kolom "Total Harga"
            data_belanja = self.list_belanja.copy()
            df = pd.DataFrame(data_belanja)
            total_belanja = df["Total Harga"].sum()
            self.list_belanja = data_belanja

            # Tampilkan table list belanja
            print("\n")
            print(tabulate(self.list_belanja, headers=[
                  "Nama Barang", "Jumlah Barang", "Harga Barang", "Total Harga"], tablefmt="grid"))
            print(f"Total belanjaan anda = Rp. {total_belanja}")

    def edit_barang(self):
        """
        Method untuk melakukan perubahan data pada list belanja

        Parameters
        ----------

        Nama Barang = str
            input = nama_barang
        Jumlah Barang = int
            input = jumlah_barang
        Harga Barang = int
            input = int

        Returns
        -------

        dict
            Dictionary yang sudah di edit datanya
        """
        self.cek_dict()
        nama_barang = input("\nMasukkan nama barang yang ingin di edit = ")

        if nama_barang in self.list_belanja["Nama Barang"]:
            index_barang = self.list_belanja["Nama Barang"].index(nama_barang)
            nama_barang_baru = input(f"Masukkan nama barang yang baru = ")
            if not nama_barang_baru:
                return  # keluar looping
            self.list_belanja["Nama Barang"][index_barang] = nama_barang_baru

            jumlah_barang = self.input_nilai_positif(
                f"Masukkan jumlah barang baru '{nama_barang_baru}' = ")
            harga_barang = self.input_nilai_positif(
                f"Masukkan harga barang baru '{nama_barang_baru}' = ")

            total_harga = jumlah_barang * harga_barang
            self.list_belanja["Jumlah Barang"][index_barang] = jumlah_barang
            self.list_belanja["Harga Barang"][index_barang] = harga_barang
            self.list_belanja["Total Harga"][index_barang] = total_harga

            data_belanja = self.list_belanja.copy()
            df = pd.DataFrame(data_belanja)
            total_belanja = df["Total Harga"].sum()
            self.list_belanja = data_belanja

            print("\n")
            print(tabulate(self.list_belanja, headers=[
                  "Nama Barang", "Jumlah Barang", "Harga Barang", "Total Harga"], tablefmt="grid"))
            print(f"Total belanjaan anda = Rp. {total_belanja}")
        else:
            print(
                f"Barang dengan nama '{nama_barang}' tidak ada dalam list belanja")

        return self.list_belanja

    def cek_dict(self):
        """
        Function untuk mengecek data dalam Dictionary
        """
        if not self.list_belanja["Nama Barang"]:
            print("\n")
            print(tabulate(self.list_belanja, headers=[
                  "Nama Barang", "Jumlah Barang", "Harga Barang", "Total Harga"], tablefmt="grid"))
            print("\nList belanja anda masih kosong")
        else:
            print("\n")
            print(tabulate(self.list_belanja, headers=[
                  "Nama Barang", "Jumlah Barang", "Harga Barang", "Total Harga"], tablefmt="grid"))

    def input_nilai_positif(self, message):
        """
        Function untuk menerima input angka positif dari pengguna.

        Parameters
        ----------
        message : str
            Pesan untuk meminta input.

        Returns
        -------
        int
            Angka positif yang dimasukkan oleh pengguna.
        """
        while True:
            try:
                angka = int(input(message))
                if angka <= 0:
                    raise ValueError
                return angka
            except ValueError:
                print("---> Error: Nilai harus positif")

    def hapus_barang(self):
        """
        Method untuk melakukan penghapusan data dari list belanja

        Parameters
        ----------

        Nama Barang = str
            input nama_barang

        Returns
        -------

        dict
            Dictionary yang sudah di delete datanta
        """
        self.cek_dict()
        nama_barang = input("\nMasukkan nama barang yang ingin di hapus = ")

        # Cek apakah ada nama barang yang di input sesuai list belanja
        if nama_barang in self.list_belanja["Nama Barang"]:
            index_barang = [i for i, nama in enumerate(
                self.list_belanja["Nama Barang"]) if nama == nama_barang]

            # Mencari index semua barang dengan nama yang di input
            for idx in index_barang:
                for key in self.list_belanja:
                    del self.list_belanja[key][idx]

            # Update total belanjaan
            data_belanja = self.list_belanja.copy()
            df = pd.DataFrame(data_belanja)
            total_belanja = df["Total Harga"].sum()
            self.list_belanja = data_belanja

            # Tampilkan list belanja
            print("\n")
            print(tabulate(self.list_belanja, headers=[
                  "Nama Barang", "Jumlah Barang", "Harga Barang", "Total Harga"], tablefmt="grid"))
            print(f"Total belanjaan anda = Rp. {total_belanja}")
        else:
            print(
                f"Barang dengan nama {nama_barang} tidak ditemukan dalam list belanja")

        return self.list_belanja

    def reset_barang(self):
        """
        Method untuk melakukan reset list belanja

        Returns
        -------
        dict
            Dictionary yang sudah di reset
        """
        self.cek_dict()
        # Validasi reset list belanja
        hapus_belanja = input(
            "\nApakah anda ingin menghapus semua list belanja anda ? (Y/N)")
        if hapus_belanja.lower() == "y":
            self.list_belanja.clear()
            self.list_belanja = {"Nama Barang": [], "Jumlah Barang": [
            ], "Harga Barang": [], "Total Harga": []}

            print("\n")
            print(tabulate(self.list_belanja, headers=[
                  "Nama Barang", "Jumlah Barang", "Harga Barang", "Total Harga"], tablefmt="grid"))
            print("\nList belanja anda sudah dihapus")

        return self.list_belanja

    def check_out_barang(self):
        """
        Method untuk melakukan check out list belanja

        Returns
        -------
        dict
            Dictionary yang sudah di reset
        """
        self.cek_dict()
        # Hitung total belanja
        data_belanja = self.list_belanja.copy()
        df = pd.DataFrame(data_belanja)
        total_belanja = df["Total Harga"].sum()
        self.list_belanja = data_belanja

        print(f"Total belanjaan anda = Rp. {total_belanja}")

        # Ketentuaan diskon
        if (total_belanja >= 200000) and (total_belanja < 300000):
            diskon_5 = total_belanja * 0.05  # Diskon 5%
            harga_akhir = total_belanja - diskon_5
            print(f"Anda mendapatkan potongan 5% sebesar Rp. {diskon_5}")
            print(f"Total yang harus dibayar = Rp. {harga_akhir}")
            # print("\n>>> Terima Kasih Sudah Berbelanja <<<")
        elif (total_belanja >= 300000) and (total_belanja < 500000):
            diskon_8 = total_belanja * 0.08  # Diskon 8%
            harga_akhir = total_belanja - diskon_8
            print(f"Anda mendapatkan potongan 8% sebesar Rp. {diskon_8}")
            print(f"Total yang harus dibayar = Rp. {harga_akhir}")
            # print("\n>>> Terima Kasih Sudah Berbelanja <<<")
        elif total_belanja >= 500000:
            diskon_10 = total_belanja * 0.1  # Diskon 10%
            harga_akhir = total_belanja - diskon_10
            print(f"Anda mendapatkan potongan 10% sebesar Rp. {diskon_10}")
            print(f"Total yang harus dibayar = Rp. {harga_akhir}")

        # Tanpa diskon
        else:
            harga_akhir = total_belanja
            print(f"Total yang harus dibayar = Rp. {harga_akhir}")

        # Validasi check-out
        confirm2 = input("\nApakah anda yakin ingin check-out? (Y/N)")
        if confirm2.lower() == "y":
            self.list_belanja.clear()
            self.list_belanja = {"Nama Barang": [], "Jumlah Barang": [
            ], "Harga Barang": [], "Total Harga": []}
            print("\n>>> Terima Kasih Sudah Berbelanja <<<")

        return self.list_belanja

    def selesai(self):
        """
        Method untuk menampilkan pesan penutup
        """
        pesan1 = ">>> Terima Kasih Sudah Berkunjung <<<"
        print("\n")
        print('-' * len(pesan1))
        print(pesan1)
        print('-' * len(pesan1))


# Jalankan program
if __name__ == "__main__":
    pacmarket = Pacmarket()
    pacmarket.masukkan_id()
    pacmarket.transaksi()
