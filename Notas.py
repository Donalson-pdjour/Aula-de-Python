Alunos = []
cont = 0
while cont < 10:
    print(f"Aluno {cont + 1}")
    
    while True:
        nome = input("Digite o nome do aluno: ")
        if len(nome) >= 3:
            nome = nome.upper()  # Converte para maiúsculas
            break
        else:
            print("Erro de nome, o nome deve ter pelo menos 3 caracteres.")
    
    idade = int(input("Digite a idade do aluno: "))
    if idade >= 18:
        status_idade = "maior de idade"
    else:
        status_idade = "menor de idade"
                
    notas = []
    i = 0
    while i < 3:
        print(f"Nota {i + 1}")
        while True:
            nota = float(input("Digite a nota do aluno: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Erro de nota, a nota deve estar entre 0 e 10.")
        i += 1
    
    media = sum(notas) / 3
    if media >= 7:
        status = "aprovada"
    else:
        status = "reprovada"
    
    # Exibe o resultado
    print(f"{nome} tem {idade} anos, é considerado {status_idade} e está {status}, com média {media:.2f}.")
                        
    # Guardando os dados do aluno em um dicionário e adicionando à lista de alunos
    Alunos.append({
        "nome": nome,
        "idade": idade,
        "status_idade": status_idade,
        "notas": notas,
        "media": media,
        "status": status
    })
    
    cont += 1

# Após coletar todos os alunos, exibe os dados
for aluno in Alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Status de idade: {aluno['status_idade']}")
    print("Notas:")
    for i, nota in enumerate(aluno['notas'], start=1):
        print(f"Nota {i}: {nota}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Status: {aluno['status']}")
    print()