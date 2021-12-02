nama = str(input("Masukkan nama : "))

a = [] 
b = []

while nama != "STOP" : 
    nomor = ("Masukkan nama kursi" + nama + ":") 
    inputnomor = input(nomor) 
    if inputnomor not in a : 
        a.append(inputnomor) 
        b.append(nama) 
    else : 
        print("Mohon maaf kursi tersebut telah terisi !")
    nama = str(input("Masukkan nama : ")) 
print("List kursi yang telah terisi : ")
for c in range (len(a)) : 
    print("kursi nomor %s telah diisi oleh %s" %(a[c],b[c]))