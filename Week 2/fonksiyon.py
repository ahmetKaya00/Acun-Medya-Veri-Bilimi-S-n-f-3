def merhaba():
    print("Merhaba, Dünya!")

merhaba()

def selam_ver():
    print("merhaba")

selam_ver()

def selam_ver(isim="Misafir"):
    print(f"Selam {isim}")

selam_ver()

def toplama(a,b):
    print(f"Toplam: {a + b}")

toplama(5,3)

def kare_al(sayi):
    return sayi ** 2

print(kare_al(5))

def topla(*sayilar):
    return sum(sayilar)

print(topla(1,2,3,4,5,6,7,8,9))

def bilgiler(**kwargs):
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")

bilgiler(ad="Ahmet",soyad="Kaya",şehir="Mersin")

karesini_al = lambda x: x ** 2

print(karesini_al(8))

toplam = lambda x,y: x + y
print(toplam(5,6))

def faktoriyel(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    return n * faktoriyel(n - 1)

print(faktoriyel(0))