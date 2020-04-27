n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

def mean(x):
    return float(sum(x)/len(x))
def sd(x):
    squared_diff = []
    for values in x:
        squared_diff.append(pow(values-mean(x),2)) 
    return float(pow(sum(squared_diff)/len(x),0.5))

def covariance(x,y):
    diff = []
    for i in range(n):
        a = (x[i]-mean(x))*(y[i]-mean(y))
        diff.append(a)
    return sum(diff)

pearson = covariance(x,y)/n/sd(x)/sd(y)

print(round(pearson,3))
