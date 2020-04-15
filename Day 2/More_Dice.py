dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice2)*len(dice1)
total_possibilities = 0
for i in dice1:
    for j in dice2:
        if i+j == 6 and i != j:
            total_possibilities +=1

probability = total_possibilities/total
print(probability)
