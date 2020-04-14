n = int(input())
x = list(map(int,input().split()))
w = list(map(int,input().split()))
sum_of_weight = 0
for i in w:
    sum_of_weight += i
i = 0
sum_of_product = 0
while(i<n):
    sum_of_product += (x[i]*w[i])
    i+=1

weighted_mean = round(sum_of_product/float(sum_of_weight),1)
print(weighted_mean)
