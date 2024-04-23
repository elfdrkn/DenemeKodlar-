# 1'den 50'ye kadar tamsayıları yineleyen bir Python programı yazın. Üçün katları için sayı yerine "Big", yedinin katları için sayı yerine "Bang" yazın. Hem üçün hem de yedinin katı olan sayılar için "BigBang" yazdırın.

for i in range(1,51):
    if i % 3 == 0 and i % 7 == 0:
        print("BigBang")
    elif i % 3 == 0:
        print("Big")
    elif i % 7 == 0:
        print("Bang")
    else:
        print(i)            