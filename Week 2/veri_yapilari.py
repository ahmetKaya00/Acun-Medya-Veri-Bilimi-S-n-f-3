meyveler = ["Elma","Armut","Muz","Kiraz"]
print(meyveler)

print(meyveler[2])
print(meyveler[-1])

meyveler[1] = "Karpuz"
print(meyveler)

meyveler.append("Çilek")
print(meyveler)
meyveler.insert(1, "Portakal")
print(meyveler)
meyveler.remove("Muz")
print(meyveler)

for meyve in meyveler:
    print(meyve)

demet = ("Elma","Armut","Muz")
print(demet)

#demet[1] = "Portakal"

ogrenci = {
    "ad": "Ali",
    "soyad": "Yılmaz",
    "yaş": 25
}

print(ogrenci["soyad"])

renkler = {"Kırmızı","Mavi","Sarı","Yeşil","Mavi"}
print(renkler)


ogrenciler = []

def ogrenci_ekle(ad, soyad,yas,dersler):
    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Yaş": yas,
        "Dersler": dersler
    }
    ogrenciler.append(ogrenci)
    print(f"Öğrenci eklendi: {ad} {soyad}")

def ogrenci_listele():
    for ogrenci in ogrenciler:
        print(f"{ogrenci['Ad']} {ogrenci['Soyad']} - Yaş: {ogrenci['Yaş']}")


ogrenci_ekle("Ahmet","Kaya",36,"Veri Bilimi")
ogrenci_ekle("Mehmet","Kaya",36,"Web Geliştirme")

ogrenci_listele()