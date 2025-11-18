# Aula 03 - Verificador de Aprovação

nota = float(input("Digite a nota do aluno (0 a 10): "))

# Estrutura de decisão
if nota >= 7.0:
    print("Situação: APROVADO")
elif nota >= 5.0:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")