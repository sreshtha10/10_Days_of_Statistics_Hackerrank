#In poisson distribution mean and variance are equal
#var(x) = e(x^2)-(e(x)^2)
#e(x^2) = var(x)+(e(x)^2)

m1 = 0.88
m2 = 1.55
cA = 160+40*(m1+(m1**2))
cB = 128+40*(m2+(m2**2))
print(round(cA,3))
print(round(cB,3))
