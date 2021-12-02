n = int(input("Input : "))
print("Output :")
for baris in range(n):
    for kolom in range(n):
        if kolom==(n-1) or baris==(n-1) or kolom+baris+1==n:
            print("*",end=" ")
        else:
            print(end="  ")
    print()