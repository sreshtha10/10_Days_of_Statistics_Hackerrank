n = int(input())
elements = list(map(int,input().split()))
frequency = list(map(int,input().split()))
data = []
for i in range(int(len(elements))):
    x = 0
    while x < frequency[i]:
        data.append(elements[i])
        x+=1
data = sorted(data)
n = len(data)
def median(element,x):
    median = 0
    index = 0
    element = sorted(element)
    if (x)%2 != 0:
        index = (x+1)/2
        median = element[int(index-1)]
        return float(median)
    else:
        index = x/2
        median = element[int(index)]+element[int(index-1)]
        return (median/float(2))      
q1 =[]
q2 = []
if n%2 == 0:
    for i in range(0,int(n/2)):
        q1.append(data[i])
    Q1 = (median(q1,n/2))

    for i in range(int(n/2),int(n)):
        q2.append(data[i])
    Q3 = (median(q2,n/2))

else:
    for i in range(0,int((n+1)/2)-1):
        q1.append(data[i])
    Q1 =(median(q1,(n-1)/2))
    for i in range((int((n+1)/2)),n):
        q2.append(data[i])
    Q3 =(median(q2,(n-1)/2))

print(round((Q3-Q1),1))
