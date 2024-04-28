# Write a Python dictionary function that takes a string from the user and matches each character in the string with an index number.

# input : "Elif" output : {0:'E' , 1: 'l' , 2: 'i' , 3: 'f'}

x = input("Enter a word: ")

dictionary_1 = {}
for i in range(len(x)):
    dictionary_1[i] = x[i]
print(dictionary_1)    

# or with enumarate function :

print(dict(enumerate("Elif",0)))