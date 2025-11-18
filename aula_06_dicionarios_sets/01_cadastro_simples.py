# Aula 06 - Cadastro com Dicionário

# Dicionário vazio
aluno = {}

aluno['nome'] = input("Nome do aluno: ")
aluno['matricula'] = int(input("Matrícula: "))
aluno['curso'] = "BICT"

print("\n--- Dados Cadastrados ---")
# Acessando valores pela chave
print(f"Aluno: {aluno['nome']}")
print(f"Matrícula: {aluno['matricula']}")
print(f"Curso: {aluno['curso']}")