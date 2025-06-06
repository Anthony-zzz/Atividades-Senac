conta= float(input("\033[3mdigite o valor da sua conta\033[0m: "))
quant_pessoas= int(input("\033[3mdigite a quantidade de pessoas\033[3m: "))
gorjeta= float(input("\033[3mdigite o valor da gorjeta(de forma inteira)\033[0m: ")) / 100
perc_gorjeta= conta * gorjeta
valor_total= (conta + perc_gorjeta) / quant_pessoas
print(f"o valor que cada pessoa terá que pagar é de: \033[4mR${valor_total}\033[0m")