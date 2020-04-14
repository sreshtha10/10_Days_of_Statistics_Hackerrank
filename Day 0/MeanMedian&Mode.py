n = int(input())
elements = list(map(int,input().split()))
#mean
s = 0
for i in elements:
    s += i  
print(round(s/float(n),1)) 
#median
median = 0
index = 0
elements = sorted(elements)
if (n)%2 != 0:
    index = (n+1)/2
    median = elements[int(index-1)]
    print(round(median,1))
else:
    index = n/2
    median = elements[int(index)]+elements[int(index-1)]
    print(median/float(2))
#mode
elements = sorted(elements)
mode=0
max_count = 0
for i in elements:
    current_count = elements.count(i)
    if(current_count > max_count):
        mode = i
        max_count = current_count  
print(mode)
