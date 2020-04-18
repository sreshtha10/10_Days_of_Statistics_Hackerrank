#A Poisson Process meets the following criteria (in reality many phenomena modeled as #Poisson processes don’t meet these exactly):
#Events are independent of each other. The occurrence of one event does not affect the #probability another event will occur.
#The average rate (events per time period) is constant.
#Two events cannot occur at the same time.
#Explanation :https://www.youtube.com/watch?v=jmqZG6roVqU
import math
mean = 2.5
x = 5
e = 2.71828
p = (mean**x)*(e**(-1*mean))/math.factorial(x)
print(round(p,3))
