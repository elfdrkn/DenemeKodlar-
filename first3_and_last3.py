# Kullanıcıdan alınan bir dizenin ilk  3 ve son 3 karakterinden oluşan bir dize döndüreceğiz. Eğer dize uzunluğu 3'ten az ise ekrana "empty string" yazacağız.

kelime = input("Lutfen bir kelime giriniz: ")

if len(kelime) >= 3:
    print(kelime[:3] + kelime[-3:])

else:
    print("Empty string")