p =0.3333
p1 = 0
for x in range(1,6):
    p1 += ((1.0-p)**(x-1))*(p)

print(round(p1,3))
