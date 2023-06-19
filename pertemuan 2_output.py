#A. print biasa atau print dasar
print("Halo, selamat pagi!")
#print biasa menggunakan variabel
kelas_a = "Jumlah mahasiswa kelas a adalah 30 orang"
print(kelas_a)


#B. print menggunakan fungsi format
nama = "Aorinka"
print("Selamat Pagi {}".format(nama))

#menggunakan penghubung + maka
aorin = "Es Krim"
hanifa = "Martabak"
devrin = "Roti Bakar"
print("Makanan Favorit Aorin = "+ str(aorin)+ ", \nMakanan Favorit Hanifa= "+ 
      str(hanifa)+ ", \nMakanan Favorit Devrin = "+ str(devrin))

#menggunakan fungsi format
diva = "Es Krim"
aorin = "Martabak"
hanifa = "Roti Bakar"
print("Makanan Favorit Diva = {} \nMakanan Favorit Aorin = {} \
    \nMakanan Favorit Hanifa = {}".format(diva, aorin, hanifa))

#C.menggunakan f-string > lebih efisien digunakan daripada format
diva = "Nasi Goreng"
aorin = "Boba"
print(f"Makanan Favorit Diva = {diva} \nMakanan Favorit Aorin = {aorin}")

#D. menggabungkan text dan variabel menggunakan koma dan plus
#bisa menggunakan plus apabila tipe data sama, misal sama-sama string
#koma digunakan jika tipe datanya beda, misal string dan int
panjang = 10
lebar = 3
luas = panjang * lebar
print("Luas Persegi Panjang = ", luas)

