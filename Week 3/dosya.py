with open("dosya.txt","r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

with open("dosya.txt","w",encoding="utf-8") as dosya:
    dosya.write("Acun Medya Akademi Web Sınıfı\n")

with open("dosya.txt","a",encoding="utf-8") as dosya:
    dosya.write("Dersimiz saat 20:00 da başladı!\n")
    
