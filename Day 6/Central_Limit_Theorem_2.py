import math
total = 250
n = 100
mean = 2.4*n
sd = math.sqrt(n)*2
def cumulative(mean,sd,total):
    return 0.5*(1+math.erf((total-mean)/(sd*(2**0.5))))

print(round(cumulative(mean,sd,total),4))
