# Kullanıcıdan iki veri istenecek. Eğer girilen iki değer de birer tamsayıysa, toplamlarını ekrana yazdıracak.

x = input("Bir değer giriniz : ")
y = input("Bir değer giriniz: ")

if x.isnumeric() and y.isnumeric():
    a = int(x) + int(y)
    print(f"Girilen degerler toplami : {a}.")
else:
          print("Girilen degerler tamsayi degildir.")          
