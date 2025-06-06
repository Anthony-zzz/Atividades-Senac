num= int(input("digite um número: "))
while True:
    if num != 0:
        dobro= num * 2
        triplo= num * 3
        raiz= num ** (1/2)
        print(f"\no dobro do seu número é {dobro} \no triplo é {triplo} \na raiz quadrada é {raiz}")
    else:
        print("cabo a brincandeira...")
        break
