# Aula 12 - Mini Sistema de Notas (Revisão)
# Integra: Listas, Dicionários, Funções e Loops

alunos = []

def adicionar_aluno():
    nome = input("Nome: ")
    nota = float(input("Nota Final: "))
    alunos.append({"nome": nome, "nota": nota})
    print("Salvo!")

while True:
    print("\n--- Sistema Escolar ---")
    print("1. Novo Aluno | 2. Ver Relatório | 3. Sair")
    op = input("Opção: ")

    if op == "1":
        adicionar_aluno()
    elif op == "2":
        print("\n--- Relatório ---")
        for a in alunos:
            status = "Aprovado" if a['nota'] >= 7 else "Reprovado"
            print(f"{a['nome']}: {a['nota']} ({status})")
    elif op == "3":
        break