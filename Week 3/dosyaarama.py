import os

if os.path.exists("dosya.txt"):
    os.remove("dosya.txt")
    print("Dosya silindi!")
else:
    print("Dosya Bulunamadı!")