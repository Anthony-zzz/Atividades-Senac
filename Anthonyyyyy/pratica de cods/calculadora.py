def calculadora():
    print("\nCalculadora Simples")
    print("Operações disponíveis:")
    print("+ : Soma")
    print("- : Subtração")
    print("* : Multiplicação")
    print("/ : Divisão")
    print("s : Sair")
    
    while True:
        # Obter a operação do usuário
        operacao = input("\nDigite a operação desejada (+, -, *, /) ou 's' para sair: ")
        
        # Verificar se o usuário quer sair
        if operacao.lower() == 's':
            print("Encerrando a calculadora...")
            break
        
        # Verificar se a operação é válida
        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida! Tente novamente.")
            continue
        
        try:
            # Obter os números do usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Realizar a operação selecionada
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: divisão por zero!")
                    continue
                resultado = num1 / num2
            
            # Exibir o resultado
            print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
            
        except ValueError:
            print("Erro: Digite apenas números válidos!")

# Executar a calculadora
calculadora()