# j -> numero imaginario
# w = 0.1 - 0.1j
w = 0.8 - 0.9j

z = 0
z1 = z**2 + w
z2 = z1**2 + w
z3 = z2**2 + w
z4 = z3**2 + w
z5 = z4**2 + w

# zn = z(n-1)**2 + w
i = 0
""" for i in range(5):
  zn = (i-1)**2 + w

print(zn) """

print({z1, z2, z3, z4, z5})

# Sequencia de Fibonnaci
""" n=int(input('Quantos termos? '))
a, b = 1, 1
k=1
while k <= n:
  print(a, end=' ')
  a, b = b, a+b
  k=k+1 """