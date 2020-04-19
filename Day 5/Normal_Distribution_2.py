import math
def cumulative(mean,std,value):
    return 0.5*(1+math.erf((value-mean)/(std*(2**0.5))))
print(round((1-cumulative(70,10,80))*100,2))
print(round((1-cumulative(70,10,60))*100,2))
print(round((cumulative(70,10,60))*100,2))
