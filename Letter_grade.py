# Kullanıcıdan sınavdan aldığı notu isteyin ve notuna karşılık gelen harf notunu yazdırın.

s = int(input("Please enter your score: "))

if 0 <= s <= 100:
    if s >= 80:
        result = "A"
    elif s >= 65:
        result = "B"
    elif s >= 55:
        result = "C" 
    elif s >= 50:
        result = "D" 
    elif s < 50:
        result = "F"
    print(f"Your letter score is: {result}")
else:
    print("Invalid input")