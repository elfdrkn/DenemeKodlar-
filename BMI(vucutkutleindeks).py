# Kullanıcıdan alınan verilerle vücut kitle indeksine göre değerlendirme gösteren programı yazacağız.

w = int(input("Please enter your weight in kg: "))
h = int(input("Please enter your height in cm: "))

result = round(w / ((h / 100) ** 2),2)
print(result)

if result < 18.5:
    body = "Underweight"
elif result < 25:
    body = "Normal"
elif result < 30:
    body = "Overweight"
elif result < 35:
    body = "Obese"
else:
    body = "Extremely Obese"      

print(f"Your BMI is: {result} and your body type is : {body}")          