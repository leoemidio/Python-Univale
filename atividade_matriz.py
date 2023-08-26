mport numpy as np

dieimes_matriz = np.array([[3,4,1], [3,2,1]])

soma = 0
for linha in dieimes_matriz:
    for elemento in linha:
        soma += elemento

print(soma)