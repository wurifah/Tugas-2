print("   Selamat Datang   ")
print("")
print("---Menu---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
print("")
menu = int(input("Pilih menu : "))
print("")
if menu == 1:
    print("Daftar kontak:")
    print("Nama         : Farhan")
    print("No Telepon   : 08123456789")
    print("Nama         : Joko")
    print("No Telepon   : 08987654321")
elif menu == 2:
    nama = []
    notelepon= []
    nama.append(input("Nama       : "))
    notelepon.append(input("No Telepon : "))
    print("")
    print("Kontak berhasil ditambahkan")
elif menu == 3:
    print("Program selesai, sampai jumpa!")
else:
    print("Menu tidak tersedia")