cpf=input("digite seu cpf: ")
print(f"\033[4m{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\033[0m")