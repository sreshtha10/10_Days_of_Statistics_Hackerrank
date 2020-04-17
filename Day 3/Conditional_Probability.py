#Let 1 denotes boy and 0 denotes girl
sample_space = [[1,0],[0,1],[1,1],[0,0]]
#p(a) denotes probabilty that one of them is boy
#p(a and b) denotes that both are boys  = p(c)
#p(b/a) denotes both are boys given that one of them is a boy = p(d)

pA = 3/4
pC = 1/4
pD = pC/pA
print(pD)
