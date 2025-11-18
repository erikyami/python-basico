# Aula 04 - Gerador de Tabuada

numero = int(input("Qual tabuada você quer ver? "))

print(f"\n--- Tabuada do {numero} ---")

# O range(1, 11) vai gerar números de 1 até 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("--- Fim ---")