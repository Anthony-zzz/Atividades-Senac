# Sistema de Gestão de Alunos

def main():
    alunos = []  # Lista para armazenar todos os alunos
    
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Cadastrar novo aluno")
        print("2. Listar todos os alunos")
        print("3. Calcular médias e resultados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            calcular_resultados(alunos)
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

def cadastrar_aluno(alunos):
    """Cadastra um novo aluno com nome, idade e 3 notas"""
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Nota {i+1} (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve estar entre 0 e 10!")
            except ValueError:
                print("Digite um valor numérico válido!")
    
    media = sum(notas) / 3
    
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas,
        "media": media
    }
    
    alunos.append(aluno)
    print(f"\nAluno {nome} cadastrado com sucesso!")
    print(f"Média: {media:.0f}")

def listar_alunos(alunos):
    """Lista todos os alunos cadastrados"""
    if not alunos:
        print("\nNenhum aluno cadastrado!")
        return
    
    print("\n--- LISTA DE ALUNOS ---")
    for i, aluno in enumerate(alunos, 1):
        print(f"\nAluno {i}:")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: {', '.join([str(n) for n in aluno['notas']])}")
        print(f"Média: {aluno['media']:.0f}")

def calcular_resultados(alunos):
    """Calcula médias e mostra quem está acima da média da turma"""
    if not alunos:
        print("\nNenhum aluno cadastrado!")
        return
    
    media_turma = 7.0  # Média definida como 7.0 conforme solicitado
    
    print("\n--- RESULTADOS FINAIS ---")
    print(f"\nMédia da turma: {media_turma:.1f}")
    
    print("\nMédias individuais:")
    for aluno in alunos:
        situacao = "APROVADO" if aluno['media'] >= media_turma else "REPROVADO"
        print(f"{aluno['nome']}: {aluno['media']:.1f} ({situacao})")
    
    aprovados = [aluno for aluno in alunos if aluno['media'] >= media_turma]
    
    if aprovados:
        print("\nAlunos acima da média da turma:")
        for aluno in aprovados:
            print(f"- {aluno['nome']} (Média: {aluno['media']:.1f})")
    else:
        print("\nNenhum aluno atingiu a média da turma.")

if __name__ == "__main__":
    main()