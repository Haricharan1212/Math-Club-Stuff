p = 3771116879
a = 7

d = 878785
K = pow(a, d, p)

K_e = 3183281641
c = 389566157

K_m = pow(K_e, d, p)

K_m_inv = pow(K_m, -1, p)

m = c * K_m_inv % p
print(m)
