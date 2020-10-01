#No 1#
print ("No 1")
array = []
n = int(input("Masukkan banyaknya elemen array: "))
for x in range(n):
    nilai = float(input("Masukkan nilai ke-{} : ".format(x+1)))
    array.append(nilai)
print("Hasil nilai total adalah : {}".format(sum(array)))
print("Hasil rata-rata adalah : {}".format(sum(array)/n))

#No 2#
print ("No 2")
panjang = float(input("Masukan Panjang: "))
lebar = float(input("Masukan Lebar: "))

luas = panjang*lebar
keliling = 2*(panjang+lebar)

print("Luas Persegi Panjang adalah ",luas)
print("Keliling Persegi Panjang adalah ",keliling)

#No 3#
print ("No 3")
berat = float(input("Masukkan berat badan anda dalam satuan(kg): "))
tinggi = float(input("Masukkan tinggi badan anda dalam satuan(meter): "))

BMI = berat/(tinggi*tinggi)
print("BMI = " , BMI )

if BMI < 18.5 :
    print("Berat badan anda kurang, Makan yg banyak!!",)
elif 18.5 <= BMI < 22.9 :
    print("Berat badan anda normal ")
elif 23 < BMI < 29.9  :
    print ("Berat badan lebih (kecenderungan obesitas), dikurangi lagi berat badannya !!")
else :
    print ("obesitas, ayoooo diet !!!")

#No4#
print("No 4")    
nilai=[]
n = int(input("Masukkan banyak nilai : "))
for x in range (n) :
    banyaknilai=int(input("Masukkan nilai ke-{} :".format(x+1)))
    nilai.append(banyaknilai)


nilaiterkecil = min(nilai)
nilaiterbesar = max(nilai)


print('list: ', nilai)
print('nilai terbesar pada list: ',nilaiterbesar)
print('nilai terkecil pada list: ',nilaiterkecil)


#No5#
print ("No 5")
print("Menentukan validasi username dan password")
username="galuh"
password="pemdesk"

for i in range(3):
    x=3
    un=input("Username =")
    pw=input("Password =")
    if (un==username) and (pw==password) :
        print ("Selamat anda berhasil masuk")
    else:
        print("Maaf username/password anda salah, silahkan ulangi")


