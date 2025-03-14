import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
puanlar = np.random.randint(0,101,1000)

print("ortalama: ", np.mean(puanlar))
print("en büyük: ", np.max(puanlar))
print("en küçük: ", np.min(puanlar))
print("standart sapma: ", np.std(puanlar))

gecenler = puanlar[puanlar >= 50]
kalanlar = puanlar[puanlar < 50]

print("Geçen Öğrenciler: ", len(gecenler))
print("Kalan Öğrenciler: ", len(kalanlar))

plt.figure(figsize=(10,5))
plt.hist(puanlar, bins=10, edgecolor="black",alpha=0.7)
plt.xlabel("Not Araliklari")
plt.ylabel("Ogrenci Sayisi")
plt.title("Ogrenci Not Dagilimi")
plt.grid=True
plt.show()

sirali_notlar = np.sort(puanlar)

dusuk_dilim = sirali_notlar[:100]
yuksek_dilim = sirali_notlar[-100:]

print("En Düşük %10'luk dilim ortalaması: ", np.mean(dusuk_dilim))
print("En Yüksek %10'luk dilim ortalaması: ", np.mean(yuksek_dilim))