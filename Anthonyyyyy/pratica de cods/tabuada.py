num=int(input("\033[3mdigite o número\033[0m: "))
print(f"\nTabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"\033[3m{num} x {i} = {resultado}\033[0m")