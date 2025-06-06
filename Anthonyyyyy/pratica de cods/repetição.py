import time
nomes = []
while True:
    nome = input("\nDigite uma nome(ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        time.sleep(1)
        print("\n\033[4mEncerrando adição de nomes...\033[0m")
        break
    nomes.append(nome)
    print("\nNome adicionado com sucesso")
    print("\n\033[3mVerificando os nomes\033[0m")
    print("\nNomes cadastrados: ")
    for nome in nomes:
        time.sleep(1)
        print(f"\033[3m - {nome}\033[0m")
