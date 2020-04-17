import math
n = 6
x = 3
p = float(1.09/2.09)
def binomial(n,x,p):
    f = math.factorial
    comb = f(n)/(f(n-x)*f(x))
    return ((comb)*(p**x)*((1.0-p)**(n-x)))
    
t = 0
for i in range(x,7):
    t += binomial(n,i,p)

print(round(t,3))