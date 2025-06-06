import random

def mega_sena():
    #Sorteia 6 números únicos entre 1 e 60
    numeros = random.sample(range(1, 61), 6)
    return sorted(numeros)

# Sorteio e exibição
print("Números da Mega Sena:")
print(*mega_sena(), sep='  -  ')