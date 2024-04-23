# Create an algotrithm that asks to employee for weekly working hours and hourly wage information and ultimately calculates th employee's weekly salary.
# Note --> Work over 40 hours per week is paid 1.5 times the wage.

wh = int(input("Enter weekly working hour: "))  #work hours = wh
hw = int(input("Enter your hourly wage: "))  #hourly wage = hw

if wh > 40:
    ww = (wh - 40) * (1.5 * hw ) + 40 * hw  # weekly wage = ww

else:
    ww = wh * hw    

print(f" Your weekly wage is {ww}")    