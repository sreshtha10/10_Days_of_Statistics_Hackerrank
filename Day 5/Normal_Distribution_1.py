import math
mean  = 20.0
sd = 2.0
value1 = 19.5
def calc(mean,std,value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))
print(round(calc(mean,sd,value1),3))
print(round((calc(mean,sd,22)-calc(mean,sd,20)),3))
