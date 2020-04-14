n = int(input())
elements = list(map(int,input().split()))
s = 0
for i in elements:
    s += i
mean = s/float(n)
squared_diff = []
i = 0
while(i<n):
    x = pow(elements[i]-mean,2)
    squared_diff.append(x)
    i+=1

standard_deviation = pow(sum(squared_diff)/float(n),0.5)
print(round(standard_deviation,1))

