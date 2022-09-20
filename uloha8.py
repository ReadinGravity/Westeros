x=int(input("zadaj mi ciselko: "))
ones=x%10
tens=x%100//10
if (ones+tens)%2==0:
    print("posledne 2 cifry su parne")
else:
    print("posledne 2 cifry su neparne")

