for i in range(5):
    print(i)

toplam = 0
for i in range(1,11):
    toplam += i
print("Toplam:", toplam)


sayi = 1
while sayi <= 5:
    print(sayi)
    sayi += 1

dogru_sifre = "1234"
girilen_sifre = ""

while girilen_sifre != dogru_sifre:
    girilen_sifre = input("Şifreyi tekrar girin:")

print("Giriş Başarılı!")

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Sayı Pozitiftir")
elif sayi < 0:
    print("Sayı Negatiftir")
else:
    print("SAyı sıfırdır")