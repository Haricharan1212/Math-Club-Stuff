p = 3771116879
a = 7

K = 1836227909

i = 42

# ephemeral key
K_e = pow(a, i, p)

# masking key
K_m = pow(K, i, p)

print(K_e)

m = 123456
c = (m * K_m) % p

print(c)
