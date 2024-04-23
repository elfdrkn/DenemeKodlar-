# Verilen bir dizede, aranan kelimenin kaç kez geçtiğini bulan program yazacağız.
# Örnek metin = 23 Nisan 1920'de Ankara'da TBMM'nin açılmasıyla Türkiye Cumhuriyeti'nin kuruluşu müjdelenmiştir. Meclisin Türk Kurtuluş Savaşı'nı başarıyla yönetmesi, yeni Türk devletinin kuruluşunu hızlandırdı.

ornek_metin = "23 Nisan 1920'de Ankara'da TBMM'nin açılmasıyla Türkiye Cumhuriyeti'nin kuruluşu müjdelenmiştir. Meclisin Türk Kurtuluş Savaşı'nı başarıyla yönetmesi, yeni Türk devletinin kuruluşunu hızlandırdı."

x = ornek_metin.count("Türk")

print(f" 'Türk' kelimesi, verilen metinde {x} kez geçiyor.")

# Bir diğer yazış biçimi ise :
print(" 'Türk' kelimesi, verilen metinde {} kez geçiyor.".format(x))