n = int(input())
elements = list(map(int,input().split()))
data = sorted(elements)
def median(element,n):
    median = 0
    index = 0
    element = sorted(element)
    if (n)%2 != 0:
        index = (n+1)/2
        median = element[int(index-1)]
        return int(median)
    else:
        index = n/2
        median = element[int(index)]+element[int(index-1)]
        return int(median/2)      
q1 =[]
q2 = []
if n%2 == 0:
    for i in range(0,int(n/2)):
        q1.append(data[i])
    print(median(q1,n/2))
    print(median(data,n))
    for i in range(int(n/2),int(n)):
        q2.append(data[i])
    print(median(q2,n/2))

else:
    for i in range(0,int((n+1)/2)-1):
        q1.append(data[i])
    print(median(q1,(n-1)/2))
    print(median(data,n))
    for i in range((int((n+1)/2)),n):
        q2.append(data[i])
    print(median(q2,(n-1)/2))
