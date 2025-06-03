valor = float(input("digite o valor que deseja sacar: "))

# Inicializa a quantidade de cada nota
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0
moedas_1 = 0

# Calcula as notas de 100
if valor >= 100:
    notas_100 = valor // 100
    valor = valor % 100

# Calcula as notas de 50
if valor >= 50:
    notas_50 = valor // 50
    valor = valor % 50

# Calcula as notas de 20
if valor >= 20:
    notas_20 = valor // 20
    valor = valor % 20

# Calcula as notas de 10
if valor >= 10:
    notas_10 = valor // 10
    valor = valor % 10

# Calcula as notas de 5
if valor >= 5:
    notas_5 = valor // 5
    valor = valor % 5

# Calcula as notas de 2
if valor >= 2:
    notas_2 = valor // 2
    valor = valor % 2

# Calcular moedas de 1
if valor >=1:
    moedas_1= valor //1
    valor = valor % 1

# Verifica se o valor restante é zero (se não, o valor não pode ser composto com as notas disponíveis)
if valor:
    print("Não é possível compor o valor exato com as notas disponíveis.")
else:
    print("\nQuantidade de notas necessárias:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de R$ 100")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de R$ 50")
    if notas_20 > 0:
        print(f"{notas_20} nota(s) de R$ 20")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de R$ 10")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de R$ 5")
    if notas_2 > 0:
        print(f"{notas_2} nota(s) de R$ 2")
    if moedas_1 > 0:
        print(f"{moedas_1} moedas de R$ 1")