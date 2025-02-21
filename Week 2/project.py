ogrenciler = []

def ogrenci_ekle():
    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin Soyadını Girin: ")
    yas = int(input("Öğrencinin Yaşını Girin: "))
    dersler = input("Öğrencinin aldığı dersleri aralarına virgül koyarak yazınız: ").split(",")

    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Yaş": yas,
        "Dersler": [ders.strip() for ders in dersler] 
    }

    ogrenciler.append(ogrenci)
    print(f"{ad} {soyad} başarıyla eklendi!")

def menu():
    while True:
        print("\nÖğrenci Yöneti Sistemi")
        print("1 - Öğrenci Ekle")
        print("6 - Çıkış")

        secim = input("Lütfen yapmak istediğiniz işlemi 1-6 arasında tuşlayınız: ")

        if secim == "1":
            ogrenci_ekle()
        elif secim == "6":
            print("Uygulamadan çıkılıyor....")
            break
        else:
            print("Lütfen 1-6 arasında bir sayı giriniz:")

menu()