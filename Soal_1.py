
nama=["Farhan" , "Johan"]
nomor=["08123456789", "08987654321"]
p=len(nama)

def menu():
    print("Selamat Datang !")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

menu()

a= int(input("Pilih Menu = "))

if a==1 :
    print("Daftar Kontak: ")
    for x in range(p):
        print ("Nama: ", nama[x])
        print ("No Telepon: ", nomor[x])

elif a==2 :
    x= input("Nama= ")
    nama.append(x)
    y= input("No Telepon= ")
    nomor.append(y)
    print("Kontak Berhasil ditambahkan")

elif a==3 :
    print("Program selesai, sampai jumpa!")

else:
    print("Menu tidak tersedia")







