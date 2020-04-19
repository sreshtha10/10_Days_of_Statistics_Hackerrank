#Since 9800 >>> 49, therefore for 49 boxes it approaches normal distribution.
#where the new mean  = 49 * mean
#and new standard deviation = sqrt(49) * sd
import math
n = 9800
x = 49
mean = 205.0
sd = 15.0
def cumulative(mean,sd,x):
    return 0.5*(1+math.erf((n-mean)/(sd*(2**0.5))))
mean = x*mean
sd = math.sqrt(x)*sd
print(round(cumulative(mean,sd,x),4))
