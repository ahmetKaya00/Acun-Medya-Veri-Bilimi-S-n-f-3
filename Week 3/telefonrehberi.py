def kisi_ekle():
    ad = input("Kişinin adını girin: ")
    telefon = input("Kişinin telefon numarasını girin: ")
    with open("telefonrehberi.txt","a",encoding="utf-8") as dosya:
        dosya.write(f"{ad}: {telefon}\n")
    print("Telefon numarası başarılı bir şekilde eklendi!")

def rehberi_goruntule():
    with open("telefonrehberi.txt","r",encoding="utf-8") as dosya:
        print("Telefon Rehberi:\n" + dosya.read())



rehberi_goruntule()