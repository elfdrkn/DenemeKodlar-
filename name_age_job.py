# Write a Python program to display your details like name, age and job in three different lines.

# Example: 
# name : Elif
# age : 27
# job : engineer

per = input("Please enter your name, age and job seperating them with comma ").split(",")


print("name :", per[0])
print("age :", per[1])
print("job :", per[2])

# Tek satırda yazdırabilmek için:

print(f"name : {per[0]}\nage : {per[1]}\njob : {per[2]} ")