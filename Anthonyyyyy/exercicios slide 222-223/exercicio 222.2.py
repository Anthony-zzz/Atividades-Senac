import random
numero= random.randint(1,100)
while True:
    tentativa= int(input("digite um número: "))
    if tentativa == numero:
        print(f"parabéns vc acertou, seu sem vida o número era {numero}")
        break
    elif tentativa > numero:
        print("é um número menor")
    elif tentativa < numero:
        print("é um número maior")
    else:
        print("tente novamente")
