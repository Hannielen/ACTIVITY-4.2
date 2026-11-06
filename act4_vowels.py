#Hannielen Faye Q. Caraig
#BMET 2101

sentence = input("Sentence: ")

vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")