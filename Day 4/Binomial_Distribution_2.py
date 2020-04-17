import math
n = 10
p = 0.12
def combination(n,x):
    f = math.factorial
    return f(n)/f(x)/f(n-x)
def binomial(n,x,p):
    return combination(n,x)*(p**x)*((1-p)**(n-x))
#At most two rejects
p1 = 0
for i in range(0,3):
    p1 += binomial(n,i,p)
p2 = 0
#At least 2 rejects
for i in range(2,11):
    p2 += binomial(n,i,p)
print(round(p1,3))
print(round(p2,3))
