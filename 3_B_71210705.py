kata = str(input("Input :"))
length = len(kata)
print("Output :")
for i in range(length):
    for j in range(length-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(kata[j],end=" ")
    print()
for i in range(length):
    for j in range(i):
        print(" ",end=" ")
    for j in range(length-i):
        print(kata[j],end=" ")
    print()