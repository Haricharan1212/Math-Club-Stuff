p = 3771116879
a = 7

K = 2210619214

i = 89291218
K_e = pow(a, i, p)
K_m = pow(K, i, p)

m = 234567
c = m * K_m % p

print(K_e)
print(c)