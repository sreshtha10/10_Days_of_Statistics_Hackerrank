dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1)*len(dice2)
total_possibilities = 0
sample_space = []
for i in dice1:
    for j in dice2:
        sample_space.append([i,j])
for i in range(len(dice1)):
    for j in  range(len(dice2)):
        if (dice1[i]+dice2[j]) <= 9:
            total_possibilities +=1
probability = total_possibilities/total
print(probability)
