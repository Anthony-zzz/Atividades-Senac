Cap_inicial= float(input("digite seu capital inicial: "))
Taxa_juros= float(input("Juros\033[3m escreva inteiro ex(35% = 35)\033[0m: ")) /100
tempo= float(input("Quantidade de mmeses: "))
montante= Cap_inicial * (1 + Taxa_juros * tempo)
print(f"seu montante é de \033[4m{montante}\033[0m")  