#Hannielen Faye Q. Caraig
#BMET 2101

count = int(input("Students: "))

total = 0
highest = None 

for i in range(1, count + 1):
    score = int(input(f"Score {i}: "))
    total += score
    if highest is None or score > highest:
        highest = score

if count > 0:
    average = total / count
    print(f"total: {total} average: {average:.2f}")
    print(f"Highest: {highest}")

else:
    print("No students entered.")