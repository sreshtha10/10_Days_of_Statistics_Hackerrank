p =0.3333
x = 5
#we need to find p(x = 5)
#for geometric distribution 2 conditions are required:
#1.x-1 cases should be a failure 2.xth case should be a success
#(1-p)^(x-1)*(p) as both conditions are independent.
p1 = ((1.0-p)**(x-1))*(p)
print(round(p1,3))
