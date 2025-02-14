print("Hello, world!")

#DEğişken isimleri harf veya _ ile başlar
#Değiş isimleri sayı ile başlamaz
#Türkçe karakter kullanılmaz. Türkçe de kullanılmaz.
#Büyük küçük harf duyarlılığı vardıır (filiz ile Filiz aynı şey değişdir.)
#Değişken tanımlamalrında boşluk kullanılmaz yerine _ kullanılır

isim = "Ahmet"
yas = 25
boy = 1.80
ogrenci_mi = True

isim = "Mehmet"

print(isim, "adlı kullanıcının yaşı:", yas)

ad = input("Adınızı Girin: ")
print("Merhaba " , ad)

dogum_yili = int(input("Doğum Tarihinizi Girin: "))
yas = 2025 - dogum_yili
print("Senin Yaşın: " , yas)

sayi1 = float(input("Birinci SAyıyı Gir"))
sayi2 = float(input("İkinci SAyıyı Gir"))
toplam = sayi1 + sayi2
print("Toplam: ", toplam)