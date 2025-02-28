import json

def kullanici_ekle():
    ad = input("Adınızı girin: ")
    yas = input("Yaşınızı girin: ")
    kulllanici = {"ad": ad, "yaş": yas}
    with open("kullanicilar.json","a",encoding="utf-8") as dosya:
        json.dump(kulllanici,dosya,ensure_ascii=False,indent=4)
        dosya.write("\n")

kullanici_ekle()